import time

#Timer

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def add(a, b):
    return a + b

@timer
def greet(name):
    return f"Hello {name}"

add(3, 4)
greet("Wasir")

#uppercase

def upp(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@upp
def show(a):
    return a

x = show("hello bulbul")
print(x)

#repeat(n)

def rep(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@rep(3)
def hi():
    print("Hi")

hi()            