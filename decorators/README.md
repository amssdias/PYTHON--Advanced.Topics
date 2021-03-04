# Decorators

Fundamentally, a decorator is just a function, or more generally a callable.

Decorators are special functions, because they take in some other function and they give us back a new function which can do something more than the function we passed in.

Decorators are very useful, because they allow us to very easily provide some additional functionality to many functions in our application. Due to their power and flexibility, they're used quite extensively in both the standard library modules, and third party libraries.

#### Example

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def say_goodbye(*args, **kwargs):
    	print("Welcome...")
        return func(*args, **kwargs)
    return say_goodbye
    
    
@decorator
def say_hello(name):
    print(f"Hello, {name}!")
    
say_hello("Dias") # Welcome... Hello, Dias!
 ```
 
 #### Links to more examples and explanation:
 - [How to write decorators in Python](https://blog.tecladocode.com/decorators-in-python/)
 - [Decorators](https://blog.tecladocode.com/python-30-day-29-decorators/)