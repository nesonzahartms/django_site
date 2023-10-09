"""
Lesson CELERY
"""
import dataclasses
import os
import time
import operator
from typing import Any
from celery import Celery

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

    # return result
    return dataclasses.asdict(CalculationResult(
        left=x,
        right=y,
        operation=operation_name,
        result=result
    )
        )


c = calculate(2, 12, 'truediv')
print(c)

'''
# Shell
from my_site.celery_tasks import calculate
import operator
operation = operator.add
op_name = operation.__qualname__
op_name
r = calculate.delay(20, 30, op_name)
r
r.ready()
'''

'''
How many cores
import os
os.cpu_count()
'''
