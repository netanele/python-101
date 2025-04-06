# This file is a comprehensive guide to learning Python, covering basics to advanced topics,
# including new features up to Python 3.13 (as of April 6, 2025). Each section includes examples
# and comments to explain the concepts clearly.

# -----------------------------------
# Section 1: Python Basics
# -----------------------------------

# Variables are dynamically typed in Python.
x = 5  # integer
y = 3.14  # float
name = "Alice"  # string
is_active = True  # boolean
print(type(x))  # <class 'int'>

# Operators: arithmetic, comparison, logical
sum_result = x + y
is_greater = x > y
logical_and = is_active and True
print(sum_result, is_greater, logical_and)  # 8.14 True True

# Control Structures: if, for, while
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

for i in range(5):  # Loops from 0 to 4
    print(i)

counter = 0
while counter < 3:
    print(f"While loop: {counter}")
    counter += 1

# Functions: reusable blocks of code
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))  # Hello, World!

# Modules: importing external functionality
import math
print(math.pi)  # 3.141592653589793

# File I/O: reading and writing files
with open("example.txt", "w") as f:
    f.write("Hello, file!")

with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # Hello, file!

# Exception Handling: managing errors
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# -----------------------------------
# Section 2: Advanced Python Features
# -----------------------------------

# Object-Oriented Programming: classes, inheritance, polymorphism
class Animal:
    def __init__(self, name):
        self.name = name  # Instance variable

    def speak(self):
        pass  # Placeholder method

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Woof! (Inheritance and polymorphism in action)

# Decorators: modifying function behavior
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # Before function, Hello!, After function

# Generators: memory-efficient iteration with yield
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)  # 5, 4, 3, 2, 1

# Context Managers: resource management with 'with'
class Resource:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with Resource() as r:
    print("Inside context")

# Asyncio: asynchronous programming with async/await
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("World")

asyncio.run(main())  # Hello, (1-second delay), World

# Threading: concurrent execution
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()  # Wait for thread to finish

# Abstract Base Classes: defining interfaces
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # 78.5

# Pydantic: data validation with type annotations
# Note: Requires 'pip install pydantic' to run this section
try:
    from pydantic import BaseModel

    class User(BaseModel):
        id: int
        name: str
        email: str

    user = User(id=1, name="Alice", email="alice@example.com")
    print(user)  # id=1 name='Alice' email='alice@example.com'
except ImportError:
    print("Pydantic not installed. Install with 'pip install pydantic' to use this section.")

# PydanticAI Mention: framework for Generative AI
# PydanticAI is a framework for building Generative AI applications, built on Pydantic.
# For more info, see https://ai.pydantic.dev/. Not included as code due to external dependency.

# -----------------------------------
# Section 3: New Features in Python 3.10
# -----------------------------------

# Structural Pattern Matching: match/case statements (PEP 634)
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:  # Union of values
            return "Not allowed"
        case 404:
            return "Not found"
        case _:
            return "Unknown error"

print(http_error(404))  # Not found

# -----------------------------------
# Section 4: New Features in Python 3.11
# -----------------------------------

# Exception Groups and except*: handling multiple exceptions (PEP 654)
try:
    raise ExceptionGroup("group", [ValueError("error1"), TypeError("error2")])
except* ValueError as e:
    print("Caught ValueError")
except* TypeError as e:
    print("Caught TypeError")

# -----------------------------------
# Section 5: New Features in Python 3.12
# -----------------------------------

# Type Parameter Syntax: compact generics (PEP 695)
from typing import TypeVar

T = TypeVar('T')

def first(container: list[T]) -> T:
    return container[0]

numbers = [1, 2, 3]
print(first(numbers))  # 1

# Improved f-strings: more flexible expressions (PEP 701)
name = "World"
print(f"Hello, {name!r}")  # Hello, 'World'

# -----------------------------------
# Section 6: New Features in Python 3.13
# -----------------------------------

# New Interactive Interpreter: multiline editing, color support
# Use python3.13 for these features; no code example as it's interactive.
print("New REPL in 3.13 supports multiline editing and color prompts.")

# Free-threaded CPython: experimental GIL-free mode (PEP 703)
# Requires python3.13t executable; no code example as it's a build option.
print("Free-threaded CPython (python3.13t) disables GIL for better concurrency.")

# Experimental JIT: performance boost (PEP 744)
# Enable with --enable-experimental-jit; no code example as it's a build flag.
print("Experimental JIT in 3.13 can be enabled for speedups.")

# -----------------------------------
# Conclusion
# -----------------------------------
# This file covers Python from basics to advanced features, including updates through 3.13.
# Experiment with each section in your IDE to deepen your understanding!