"""
Lesson CELERY
"""
import dataclasses
import os
import time
import operator
from typing import Any, Callable
from celery import Celery
from functools import partial

from frozendict import frozendict
from pydantic import BaseModel

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')

app = Celery('my_site', broker='pyamqp://guest@localhost//', backend='rpc://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@dataclasses.dataclass
class CalculationResult:
    operation: str
    left: int | float
    right: int | float
    result: int | float


_AVAILABLE_OPERATIONS = frozendict(
    {
        operator.add.__qualname__: operator.add,
        operator.sub.__qualname__: operator.sub,
        operator.truediv.__qualname__: operator.truediv,
        operator.floordiv.__qualname__: operator.floordiv,
        operator.mul.__qualname__: operator.mul,
    }
)


@app.task
def calculate(x: int, y: int, operation_name: str):
    time.sleep(x)

    if not (method := _AVAILABLE_OPERATIONS.get(operation_name)):
        raise ValueError(
            f'{operation_name} should be one '
            f'of {_AVAILABLE_OPERATIONS}'
        )

    result = method(x, y)

    return result
    # return dataclasses.asdict(CalculationResult(
    #     left=x,
    #     right=y,
    #     operation=operation_name,
    #     result=result
    # )
    #     )






def my_func(name: str, age: int, gender: str) -> str:
    return f"Hi! I'm {name}, {age}, my gender is {gender}"


def fn1(name: str, age: int, fn: Callable):
    return fn(my_func, name=name, age=age)


def fn2(gender: str):
    return partial(my_func, gender=gender)


if __name__ == '__main__':
    c = calculate(2, 12, 'truediv')
    print(c)

    # Shell

    from my_site.celery_tasks import calculate
    import operator

    operation = operator.add
    op_name = operation.__qualname__
    op_name
    r = calculate.delay(20, 30, op_name)

    r.ready()
    f = calculate.signature((10, 10, operator.mul.__qualname__))
    r = f.delay().get()
    f = calculate.signature((1, 10, operator.mul.__qualname__), countdown=10)
    result = f.delay().get()
    f = calculate.s(1, 10)
    result = f.delay(operator_name=operator.mul.__qualname__).get()
    from celery import group

    group(calculate.s(i, i, operator.add.__qualname__) for i in range(10))
    my_group = group(calculate.s(i, i, operator.add.__qualname__) for i in range(10))
    ", ".join(str(i) for i in range(10))
    from celery import chain

    s1 = calculate.s(10, 10, operator.add.__qualname__)
    s2 = calculate.s(5, operator.mul.__qualname__)
    chained = chain(s1 | s2)
    result = chained().get()
    '''

    '''
    'How many cores'
    import os

    os.cpu_count()