from functools import partial

def my_func(name: str, age: str, gender: str) -> str:
    return f"Hi I'm {name}, {age}, my gender is {gender}"

def fn1(name: str, age: str):
    fn = partial(my_func, name=name, age=age)
    return fn

def fn2(gender: str, fn: callable):
    return fn(gender=gender)

res1 = fn1('Zahar', 18)
res2 = fn2('M', fn=res1)
print(res2)
