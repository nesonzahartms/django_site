import asyncio
import operator
import time

import asyncache
import cachetools.keys
from cachetools import TTLCache


# for caching the standard functions use @cachetools.cache decorator
@cachetools.cached(cache=TTLCache(ttl=60 * 5, maxsize=10_000))
def my_sync_func(arg: int) -> dict[str, dict[str, int]]:
    print("Called my_sync_func")
    time.sleep(arg)
    print("Awakening!")
    print("---------------------")
    return {"response": {"data": arg}}


# for caching the Coroutines functions use @cachetools.cache decorator
@asyncache.cached(cache=TTLCache(ttl=60 * 5, maxsize=10_000))
async def my_async_func(arg: int) -> dict[str, dict[str, int]]:
    print("Called my_sync_func")
    await asyncio.sleep(arg)
    print("Awakening!")
    print("---------------------")
    return {"response": {"data": arg}}


class MyPerson:
    def __init__(self):
        self._name = "Alex"


class MyClass:
    _CACHE = TTLCache(ttl=60 * 5, maxsize=10_000)

    def __init__(self):
        self._person = MyPerson()
        self._some = [1, 2, 3]

    # for caching the instance's non-async methods use @cachetools.cachedmethod decorator
    @cachetools.cachedmethod(operator.attrgetter("_CACHE"))
    def my_sync_method(self, arg: int) -> dict[str, dict[str, int]]:
        print("Called my_sync_method")
        time.sleep(arg)
        print("Awakening!")
        print("---------------------")
        return {"response": {"data": arg}}

    # for caching the instance's async methods use @asyncache.cachedmethod decorator,
    # BUT we also need to specify the 'key' argument as 'cachetools.keys.methodkey',
    # otherwise the cache will not work for different instances of MyClass!
    @asyncache.cachedmethod(
        cache=operator.attrgetter("_CACHE"),
        key=cachetools.keys.methodkey
    )
    async def my_async_method(self, arg: int) -> dict[str, dict[str, int]]:
        print("Called my_async_method")
        await asyncio.sleep(arg)
        print("Awakening!")
        print("---------------------")
        return {"response": {"data": arg}}


def check_sync_function_cache():
    counter = value = 0
    while True:
        if counter > 10:
            break

        response = my_sync_func(value)  # call 'my_sync_func' with same value many times
        print(f"Response is received: {response}")
        time.sleep(0.5)
        counter += 1


async def check_async_function_cache():
    counter = value = 0
    while True:
        if counter > 10:
            break

        response = await my_async_func(value)  # call 'my_async_func' with same value many times
        print(f"Response is received: {response}")
        await asyncio.sleep(0.5)
        counter += 1


def check_sync_method_cache():
    counter = value = 0
    while True:
        if counter > 10:
            break

        my_obj = MyClass()  # intentionally create new MyClass instance on each iteration
        response = my_obj.my_sync_method(value)  # call 'my_sync_method' with same value many times
        print(f"Response 1 is received: {response}")
        time.sleep(0.5)
        counter += 1


async def check_async_method_cache():
    counter = value = 0
    while True:
        if counter > 10:
            break

        my_obj = MyClass()  # intentionally create new MyClass instance on each iteration
        response = await my_obj.my_async_method(value)  # call 'my_async_method' with same value many times
        print(f"Response is received: {response}")
        await asyncio.sleep(0.5)
        counter += 1


# Run it one by one
# check_sync_function_cache()
# asyncio.run(check_async_function_cache())
# check_sync_method_cache()
asyncio.run(check_async_method_cache())


