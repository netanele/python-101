#!/usr/bin/env python3
"""
Python Tutorial: From Basics to Advanced

This file serves as a comprehensive tutorial covering Python from basic to advanced concepts,
including the latest features from Python 3.10 through 3.13.

Each section contains executable code examples with detailed comments explaining the concepts.
"""

# Table of Contents:
# 1. Basic Python Concepts
#    - Variables, Data Types, and Operators
#    - Control Flow (if/else, loops)
#    - Functions and Scope
#    - Data Structures (lists, dictionaries, sets, tuples)
#    - File I/O
# 2. Intermediate Python Concepts
#    - Classes and OOP
#    - Inheritance and Interfaces
#    - Exception Handling
#    - Modules and Packages
#    - Decorators and Context Managers
# 3. Advanced Python Concepts
#    - Threading and Multiprocessing
#    - Asyncio and Asynchronous Programming
#    - Type Hints and Annotations
#    - Generators and Iterators
#    - Functional Programming Concepts
# 4. Modern Python Features
#    - Python 3.10: Structural Pattern Matching, Improved Error Messages
#    - Python 3.11: Performance Improvements, Exception Groups
#    - Python 3.12: F-string Improvements, New Type Annotation Syntax
#    - Python 3.13: JIT Compiler, Free-Threaded Mode, New REPL
# 5. Pydantic and Pydantic AI

##############################################################################
# SECTION 1: BASIC PYTHON CONCEPTS
##############################################################################

print("\n=== SECTION 1: BASIC PYTHON CONCEPTS ===")

# ===== Variables, Data Types, and Operators =====
print("\n--- Variables, Data Types, and Operators ---")

# Variables in Python don't need explicit type declarations
# Python is dynamically typed - the type is determined at runtime
x = 10                # Integer
y = 3.14              # Float
name = "Python"       # String
is_awesome = True     # Boolean

print(f"x = {x}, type: {type(x)}")
print(f"y = {y}, type: {type(y)}")
print(f"name = {name}, type: {type(name)}")
print(f"is_awesome = {is_awesome}, type: {type(is_awesome)}")

# None type represents the absence of a value
z = None
print(f"z = {z}, type: {type(z)}")

# Basic Operators
# Arithmetic operators
print(f"Addition: {x + 5}")             # 15
print(f"Subtraction: {x - 5}")          # 5
print(f"Multiplication: {x * 2}")       # 20
print(f"Division: {x / 3}")             # 3.3333...
print(f"Floor Division: {x // 3}")      # 3 (integer division, rounded down)
print(f"Modulus: {x % 3}")              # 1 (remainder of division)
print(f"Exponentiation: {x ** 2}")      # 100 (x squared)

# Comparison operators
print(f"Equal: {x == 10}")              # True
print(f"Not equal: {x != 5}")           # True
print(f"Greater than: {x > 5}")         # True
print(f"Less than: {x < 15}")           # True
print(f"Greater or equal: {x >= 10}")   # True
print(f"Less or equal: {x <= 10}")      # True

# Logical operators
a, b = True, False
print(f"AND: {a and b}")                # False
print(f"OR: {a or b}")                  # True
print(f"NOT: {not a}")                  # False

# Identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2: {list1 is list2}")       # False (different objects)
print(f"list1 is list3: {list1 is list3}")       # True (same object)
print(f"list1 is not list2: {list1 is not list2}") # True

# Membership operators
print(f"2 in list1: {2 in list1}")              # True
print(f"5 not in list1: {5 not in list1}")      # True

# ===== Control Flow =====
print("\n--- Control Flow ---")

# if-elif-else statements
age = 25

if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior")

# Ternary operator (conditional expression)
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# while loop
print("\nWhile loop example:")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# for loop with range
print("\nFor loop with range example:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"i: {i}")

# for loop with step
print("\nFor loop with step example:")
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(f"i: {i}")

# for loop with iterable
print("\nFor loop with iterable example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# break and continue
print("\nBreak example:")
for i in range(10):
    if i == 5:
        break  # Exit the loop
    print(f"i: {i}")

print("\nContinue example:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"i: {i}")

# ===== Functions and Scope =====
print("\n--- Functions and Scope ---")

# Basic function definition
def greet(name):
    """This is a docstring. It describes what the function does."""
    return f"Hello, {name}!"

print(greet("World"))  # Hello, World!

# Function with default parameters
def greet_with_default(name="Stranger"):
    return f"Hello, {name}!"

print(greet_with_default())        # Hello, Stranger!
print(greet_with_default("Friend"))  # Hello, Friend!

# Function with multiple parameters
def calculate_rectangle_area(length, width):
    return length * width

print(f"Rectangle area: {calculate_rectangle_area(5, 3)}")  # 15

# Function with arbitrary number of arguments
def sum_all(*args):
    """Sum all the arguments passed to the function."""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")  # 15

# Function with keyword arguments
def person_info(**kwargs):
    """Print information about a person."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Alice", age=30, city="New York")

# Variable scope
x = 100  # Global variable

def test_scope():
    y = 200  # Local variable
    print(f"Inside function - x: {x}, y: {y}")

test_scope()
print(f"Outside function - x: {x}")
# print(f"y: {y}")  # This would raise a NameError: name 'y' is not defined

# Modifying global variables
def modify_global():
    global x
    x = 500
    print(f"Inside function after modification - x: {x}")

modify_global()
print(f"Outside function after modification - x: {x}")

# ===== Data Structures =====
print("\n--- Data Structures ---")

# Lists - ordered, mutable collections
print("\nLists:")
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# List methods
fruits.append("orange")  # Add to the end
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")  # Insert at specific position
print(f"After insert: {fruits}")

fruits.remove("banana")  # Remove by value
print(f"After remove: {fruits}")

popped_fruit = fruits.pop()  # Remove and return the last item
print(f"Popped fruit: {popped_fruit}")
print(f"After pop: {fruits}")

fruits.sort()  # Sort in place
print(f"After sort: {fruits}")

# List comprehensions - concise way to create lists
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Original numbers: {numbers}")
print(f"Squares: {squares}")

even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Tuples - ordered, immutable collections
print("\nTuples:")
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked - X: {x}, Y: {y}")

# Dictionaries - key-value pairs, unordered, mutable
print("\nDictionaries:")
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")
print(f"Name: {person['name']}")

# Dictionary methods
person["email"] = "alice@example.com"  # Add new key-value pair
print(f"After adding email: {person}")

# Get with default value
phone = person.get("phone", "Not available")
print(f"Phone: {phone}")

# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print(f"Squared numbers: {squared_numbers}")

# Sets - unordered collections of unique elements
print("\nSets:")
fruits_set = {"apple", "banana", "cherry", "apple"}  # Duplicate is removed
print(f"Fruits set: {fruits_set}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Union: {set1 | set2}")  # Elements in either set
print(f"Intersection: {set1 & set2}")  # Elements in both sets
print(f"Difference: {set1 - set2}")  # Elements in set1 but not in set2
print(f"Symmetric difference: {set1 ^ set2}")  # Elements in either set but not in both

# ===== File I/O =====
print("\n--- File I/O ---")

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("Python is awesome!\n")

print("File written successfully.")

# Reading from a file
print("\nReading the entire file:")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("\nReading line by line:")
with open("example.txt", "r") as file:
    for line in file:
        print(f"Line: {line.strip()}")  # strip() removes the newline character

# Appending to a file
with open("example.txt", "a") as file:
    file.write("This line was appended.\n")

print("\nFile after appending:")
with open("example.txt", "r") as file:
    print(file.read())

##############################################################################
# SECTION 2: INTERMEDIATE PYTHON CONCEPTS
##############################################################################

print("\n=== SECTION 2: INTERMEDIATE PYTHON CONCEPTS ===")

# ===== Classes and Object-Oriented Programming =====
print("\n--- Classes and Object-Oriented Programming ---")

# Basic class definition
class Person:
    """A simple class representing a person."""

    # Class attribute (shared by all instances)
    species = "Homo sapiens"

    # Constructor (initialization) method
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    # Instance method with parameters
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday! {self.name} is now {self.age} years old."

# Creating instances of the class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(f"Person 1: {person1.name}, {person1.age}")
print(f"Person 2: {person2.name}, {person2.age}")
print(f"Both are: {Person.species}")

print(person1.greet())
print(person2.greet())

print(person1.celebrate_birthday())
print(f"Person 1's new age: {person1.age}")

# Class with special (dunder) methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation for developers
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # String representation for users
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Addition operator overloading
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Equality operator overloading
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)

print(f"p1: {p1}")  # Uses __str__
print(f"p1 + p2: {p1 + p2}")  # Uses __add__ and then __str__
print(f"p1 == p2: {p1 == p2}")  # Uses __eq__
print(f"repr(p1): {repr(p1)}")  # Uses __repr__

# ===== Inheritance and Interfaces =====
print("\n--- Inheritance and Interfaces ---")

# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

    def introduce(self):
        return f"I am {self.name}, and I can {self.speak()}."

# Derived class (child class)
class Dog(Animal):
    def speak(self):
        return "bark"

    # Additional method specific to Dog
    def wag_tail(self):
        return f"{self.name} is wagging tail."

# Another derived class
class Cat(Animal):
    def speak(self):
        return "meow"

    # Additional method specific to Cat
    def purr(self):
        return f"{self.name} is purring."

# Creating instances of derived classes
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.introduce())
print(cat.introduce())
print(dog.wag_tail())
print(cat.purr())

# Multiple inheritance
class A:
    def method(self):
        return "Method from A"

class B:
    def method(self):
        return "Method from B"

    def another_method(self):
        return "Another method from B"

# C inherits from both A and B
# Method Resolution Order (MRO) determines which method is called
class C(A, B):
    pass

class D(B, A):
    pass

c = C()
d = D()

print(f"C.method(): {c.method()}")  # From A (first in inheritance list)
print(f"D.method(): {d.method()}")  # From B (first in inheritance list)
print(f"C.another_method(): {c.another_method()}")  # From B

# Method Resolution Order (MRO)
print(f"C's MRO: {[cls.__name__ for cls in C.__mro__]}")
print(f"D's MRO: {[cls.__name__ for cls in D.__mro__]}")

# Abstract Base Classes (ABC) - Python's way of defining interfaces
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# shape = Shape()  # This would raise TypeError: Can't instantiate abstract class
rectangle = Rectangle(5, 3)
circle = Circle(2)

print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area():.2f}, perimeter: {circle.perimeter():.2f}")

# ===== Exception Handling =====
print("\n--- Exception Handling ---")

# Basic try-except
try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero!")

# try-except-else-finally
try:
    x = 10 / 2  # This will not raise an exception
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    print(f"Division successful, result: {x}")  # This runs if no exception occurs
finally:
    print("This always executes, regardless of exceptions")  # Cleanup code

# Handling multiple exceptions
try:
    # Could raise different exceptions
    value = int("abc")  # ValueError
    result = 10 / value  # Potential ZeroDivisionError
except ValueError:
    print("Error: Invalid conversion!")
except ZeroDivisionError:
    print("Error: Division by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")

# Creating custom exceptions
class CustomError(Exception):
    """A custom exception class."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise CustomError("Age is unrealistically high", 1001)
    return age

try:
    validate_age(200)
except ValueError as e:
    print(f"ValueError: {e}")
except CustomError as e:
    print(f"CustomError (code {e.code}): {e.message}")

# ===== Modules and Packages =====
print("\n--- Modules and Packages ---")

# Importing standard library modules
import math
import random
from datetime import datetime, timedelta

print(f"Pi: {math.pi}")
print(f"Random number: {random.randint(1, 100)}")
print(f"Current date and time: {datetime.now()}")
print(f"Tomorrow: {datetime.now() + timedelta(days=1)}")

# Creating a module (normally this would be in a separate file)
# For demonstration, we'll use a string with code and exec()
module_code = """
# This would be in a file named my_module.py

def greet(name):
    return f"Hello, {name}!"

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Variables in the module
PI = 3.14159
"""

# Execute the module code to simulate importing it
namespace = {}
exec(module_code, namespace)

# Now we can use the module's components
greet_func = namespace["greet"]
Calculator = namespace["Calculator"]
PI = namespace["PI"]

print(f"From module - greet: {greet_func('World')}")
print(f"From module - Calculator.add: {Calculator.add(5, 3)}")
print(f"From module - PI: {PI}")

# ===== Decorators and Context Managers =====
print("\n--- Decorators and Context Managers ---")

# Basic decorator
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

# Applying the decorator
@simple_decorator
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

say_hello("Alice")

# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    return f"Hi, {name}!"

print(say_hi("Bob"))

# Class as a decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call count: {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_bye(name):
    return f"Bye, {name}!"

print(say_bye("Charlie"))
print(say_bye("David"))

# Context managers with class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exceptions, False to propagate them
        return False

# Using the context manager
with FileManager("example.txt", "r") as file:
    content = file.read()
    print(f"First 10 characters: {content[:10]}...")

# Context manager with contextlib
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# Using the contextlib-based context manager
with file_manager("example.txt", "r") as file:
    content = file.read()
    print(f"First 10 characters (using contextlib): {content[:10]}...")

##############################################################################
# SECTION 3: ADVANCED PYTHON CONCEPTS
##############################################################################

print("\n=== SECTION 3: ADVANCED PYTHON CONCEPTS ===")

# ===== Threading and Multiprocessing =====
print("\n--- Threading and Multiprocessing ---")

# Threading - useful for I/O-bound tasks
import threading
import time

def worker(name, delay):
    """A simple worker function that sleeps for a specified amount of time."""
    print(f"Worker {name} starting")
    time.sleep(delay)
    print(f"Worker {name} finished after {delay} seconds")

# Creating and starting threads
print("\nStarting threads:")
threads = []
for i in range(3):
    # Create a thread
    t = threading.Thread(target=worker, args=(f"Thread-{i}", i))
    threads.append(t)
    # Start the thread
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads completed")

# Thread with a class
class WorkerThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Worker {self.name} starting")
        time.sleep(self.delay)
        print(f"Worker {self.name} finished after {self.delay} seconds")

# Creating and starting class-based threads
print("\nStarting class-based threads:")
threads = []
for i in range(3):
    t = WorkerThread(f"ClassThread-{i}", i)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All class-based threads completed")

# Thread synchronization with Lock
print("\nThread synchronization with Lock:")
counter = 0
counter_lock = threading.Lock()

def increment_counter(amount, repeats):
    global counter
    for _ in range(repeats):
        with counter_lock:  # Acquire the lock
            # Critical section (only one thread can execute this at a time)
            current = counter
            time.sleep(0.001)  # Simulate some work
            counter = current + amount
        # Lock is released here

# Create threads that increment the counter
threads = []
for i in range(5):
    t = threading.Thread(target=increment_counter, args=(1, 10))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Final counter value: {counter}")

# Multiprocessing - useful for CPU-bound tasks
import multiprocessing

def cpu_bound_task(number):
    """A CPU-bound task that calculates the sum of squares up to a number."""
    result = sum(i * i for i in range(number))
    print(f"Task with input {number} result: {result}")
    return result

# Using a process pool to execute tasks in parallel
if __name__ == "__main__":  # This guard is important for multiprocessing
    print("\nMultiprocessing with Pool:")
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=3) as pool:
        # Map the function to the inputs
        results = pool.map(cpu_bound_task, [1000000, 2000000, 3000000])
        print(f"Pool results: {results}")

# ===== Asyncio and Asynchronous Programming =====
print("\n--- Asyncio and Asynchronous Programming ---")

# Asyncio - for concurrent I/O-bound tasks
import asyncio

# Coroutine definition with async/await
async def async_worker(name, delay):
    """A coroutine that simulates an I/O-bound task."""
    print(f"Async worker {name} starting")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"Async worker {name} finished after {delay} seconds")
    return f"{name} result"

# Running a coroutine
async def main():
    print("\nRunning a single coroutine:")
    result = await async_worker("Coroutine-1", 1)
    print(f"Result: {result}")

    # Running multiple coroutines concurrently
    print("\nRunning multiple coroutines concurrently:")
    tasks = [
        async_worker(f"Coroutine-{i}", i) for i in range(1, 4)
    ]
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")

# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())

# Async context manager
class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource asynchronously")
        await asyncio.sleep(1)  # Simulate async acquisition
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource asynchronously")
        await asyncio.sleep(0.5)  # Simulate async release

    async def use_resource(self):
        print("Using resource")
        await asyncio.sleep(0.5)  # Simulate async usage

# Using async context manager
async def use_async_resource():
    print("\nUsing async context manager:")
    async with AsyncResource() as resource:
        await resource.use_resource()
    print("Done with async resource")

# Run the async context manager example
if __name__ == "__main__":
    asyncio.run(use_async_resource())

# ===== Type Hints and Annotations =====
print("\n--- Type Hints and Annotations ---")

# Basic type hints
from typing import List, Dict, Tuple, Optional, Union, Any, Callable

def greet_with_types(name: str) -> str:
    """Greet a person by name with type hints."""
    return f"Hello, {name}!"

print(greet_with_types("World"))

# Type hints for collections
def process_items(items: List[int]) -> List[int]:
    """Process a list of integers and return a new list."""
    return [item * 2 for item in items]

print(f"Processed items: {process_items([1, 2, 3])}")

# Type hints for dictionaries and tuples
def process_data(data: Dict[str, int], config: Tuple[str, int]) -> Dict[str, float]:
    """Process data with configuration."""
    result = {}
    for key, value in data.items():
        result[key] = value * config[1] + 0.5
    return result

data = {"a": 1, "b": 2}
config = ("multiply", 2)
print(f"Processed data: {process_data(data, config)}")

# Optional and Union types
def maybe_process(value: Optional[int] = None) -> Union[int, str]:
    """Process a value that might be None."""
    if value is None:
        return "No value provided"
    return value * 2

print(f"Maybe process (with value): {maybe_process(5)}")
print(f"Maybe process (without value): {maybe_process()}")

# Type aliases
Vector = List[float]
Matrix = List[Vector]

def dot_product(v1: Vector, v2: Vector) -> float:
    """Calculate the dot product of two vectors."""
    return sum(x * y for x, y in zip(v1, v2))

print(f"Dot product: {dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0])}")

# Function type hints
Callback = Callable[[int, int], int]

def apply_operation(a: int, b: int, operation: Callback) -> int:
    """Apply an operation to two integers."""
    return operation(a, b)

def add(a: int, b: int) -> int:
    return a + b

print(f"Apply operation: {apply_operation(5, 3, add)}")

# Type checking with mypy
# To check types: mypy your_file.py
# This will catch type errors statically

# ===== Generators and Iterators =====
print("\n--- Generators and Iterators ---")

# Basic generator function
def count_up_to(limit):
    """Generate numbers from 0 up to limit."""
    count = 0
    while count < limit:
        yield count
        count += 1

print("Generator example:")
for number in count_up_to(5):
    print(number, end=" ")
print()  # Newline

# Generator expression (similar to list comprehension)
squares_gen = (x**2 for x in range(5))
print("Generator expression:")
for square in squares_gen:
    print(square, end=" ")
print()  # Newline

# Infinite generator
def infinite_counter():
    """An infinite generator that counts up from 0."""
    count = 0
    while True:
        yield count
        count += 1

print("Infinite generator (limited to 5 items):")
counter = infinite_counter()
for _ in range(5):
    print(next(counter), end=" ")
print()  # Newline

# Generator with send method
def echo_generator():
    """A generator that echoes values sent to it."""
    value = yield "Ready"  # Initial yield
    while True:
        value = yield f"Echo: {value}"

print("Generator with send:")
echo = echo_generator()
print(next(echo))  # Start the generator
print(echo.send("Hello"))  # Send a value
print(echo.send("World"))  # Send another value

# Custom iterator class
class Countdown:
    """An iterator that counts down from n to 0."""
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # Return an iterator (self in this case)
        return self

    def __next__(self):
        # Return the next item or raise StopIteration
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

print("Custom iterator:")
for num in Countdown(5):
    print(num, end=" ")
print()  # Newline

# ===== Functional Programming Concepts =====
print("\n--- Functional Programming Concepts ---")

# Lambda functions (anonymous functions)
add = lambda a, b: a + b
print(f"Lambda function: {add(5, 3)}")

# Higher-order functions that take functions as arguments
def apply_twice(func, value):
    """Apply a function twice to a value."""
    return func(func(value))

print(f"Apply twice: {apply_twice(lambda x: x * 2, 3)}")  # 3 -> 6 -> 12

# Map, filter, reduce
numbers = [1, 2, 3, 4, 5]

# Map: Apply a function to each item in an iterable
squared = list(map(lambda x: x**2, numbers))
print(f"Map result: {squared}")

# Filter: Filter items based on a function
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter result: {even}")

# Reduce: Reduce an iterable to a single value
from functools import reduce
sum_all = reduce(lambda a, b: a + b, numbers)
print(f"Reduce result: {sum_all}")

# Function composition
def compose(f, g):
    """Compose two functions: compose(f, g)(x) = f(g(x))."""
    return lambda x: f(g(x))

# Example functions
to_upper = lambda s: s.upper()
add_exclamation = lambda s: s + "!"

# Compose them
shout = compose(add_exclamation, to_upper)
print(f"Function composition: {shout('hello')}")

# Partial functions
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a partial function with base=2
square = partial(power, 2)
print(f"Partial function (square): {square(3)}")  # 2^3 = 8

# Create a partial function with exponent=2
square_of = partial(power, exponent=2)
print(f"Partial function (square_of): {square_of(3)}")  # 3^2 = 9

# Immutable data structures
# Python's built-in immutable types: int, float, str, tuple, frozenset

# Example with tuples for immutable data
def add_to_tuple(t, item):
    """Return a new tuple with the item added (doesn't modify the original)."""
    return t + (item,)

t1 = (1, 2, 3)
t2 = add_to_tuple(t1, 4)
print(f"Original tuple: {t1}")
print(f"New tuple: {t2}")

# Recursion
def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Tail recursion optimization (not built into Python, but can be simulated)
def factorial_tail(n, accumulator=1):
    """Calculate factorial with tail recursion."""
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

print(f"Factorial of 5 (tail recursion): {factorial_tail(5)}")

##############################################################################
# SECTION 4: MODERN PYTHON FEATURES (3.10-3.13)
##############################################################################

print("\n=== SECTION 4: MODERN PYTHON FEATURES (3.10-3.13) ===")

# ===== Python 3.10 Features =====
print("\n--- Python 3.10 Features ---")

# Structural Pattern Matching (match/case) - similar to switch/case in other languages
def check_status(status):
    """Check the status using structural pattern matching."""
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:  # Default case (wildcard pattern)
            return "Unknown Status"

print(f"Status 200: {check_status(200)}")
print(f"Status 404: {check_status(404)}")
print(f"Status 999: {check_status(999)}")

# Pattern matching with complex data structures
def process_command(command):
    """Process a command using structural pattern matching with data structures."""
    match command:
        case ["quit"]:
            return "Exiting program"
        case ["load", filename]:
            return f"Loading file: {filename}"
        case ["save", filename, content]:
            return f"Saving content to file: {filename}"
        case ["search", *keywords] if keywords:  # Guard pattern with condition
            return f"Searching for: {', '.join(keywords)}"
        case _:
            return "Unknown command"

print(f"Command ['quit']: {process_command(['quit'])}")
print(f"Command ['load', 'data.txt']: {process_command(['load', 'data.txt'])}")
print(f"Command ['search', 'python', 'tutorial']: {process_command(['search', 'python', 'tutorial'])}")

# Pattern matching with class instances
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

def describe_shape(shape):
    """Describe a shape using pattern matching with classes."""
    match shape:
        case Point(x=0, y=0):
            return "Point at origin"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"
        case Circle(center=Point(x=0, y=0), radius=r):
            return f"Circle at origin with radius {r}"
        case Circle():
            return f"Circle at ({shape.center.x}, {shape.center.y}) with radius {shape.radius}"
        case Rectangle(top_left=Point(x=x1, y=y1), bottom_right=Point(x=x2, y=y2)):
            return f"Rectangle from ({x1}, {y1}) to ({x2}, {y2})"
        case _:
            return "Unknown shape"

print(f"Point(0, 0): {describe_shape(Point(0, 0))}")
print(f"Point(1, 2): {describe_shape(Point(1, 2))}")
print(f"Circle with center at origin: {describe_shape(Circle(Point(0, 0), 5))}")

# Improved error messages in Python 3.10
try:
    # This would show more precise error location in Python 3.10+
    # x = {1: 'a', 2: 'b'}[3]
    pass  # Commented out to avoid actual error
except KeyError:
    print("In Python 3.10+, the error message would point to the exact location")

# Union types with | operator (PEP 604)
def process_data(data: int | float | str) -> str:
    """Process data that can be int, float, or str."""
    return f"Processed: {data}"

print(f"Process int: {process_data(42)}")
print(f"Process float: {process_data(3.14)}")
print(f"Process str: {process_data('hello')}")

# ===== Python 3.11 Features =====
print("\n--- Python 3.11 Features ---")

# Exception groups and except* syntax
try:
    # In Python 3.11, you can raise multiple exceptions at once using ExceptionGroup
    # raise ExceptionGroup("Multiple errors", [
    #     ValueError("Invalid value"),
    #     TypeError("Invalid type"),
    #     KeyError("Missing key")
    # ])
    print("ExceptionGroup demonstration (commented out to avoid actual error)")
except* ValueError as e:
    print(f"Would catch ValueError: {e}")
except* TypeError as e:
    print(f"Would catch TypeError: {e}")
except* Exception as e:
    print(f"Would catch other exceptions: {e}")

# Performance improvements in Python 3.11
# - Faster startup
# - Faster runtime
# - Optimized string operations
# - More efficient memory usage
print("Python 3.11 includes significant performance improvements (25% faster on average)")

# Enhanced error messages with better tracebacks
try:
    # This would show more detailed traceback in Python 3.11+
    # 1 / 0
    pass  # Commented out to avoid actual error
except ZeroDivisionError:
    print("In Python 3.11+, error tracebacks are more detailed and helpful")

# Self type for methods returning instances of their class
from typing import Self  # New in Python 3.11

class Builder:
    def __init__(self, value: int = 0) -> None:
        self.value = value

    def increment(self, amount: int) -> Self:  # Returns instance of the same class
        self.value += amount
        return self

    def decrement(self, amount: int) -> Self:  # Returns instance of the same class
        self.value -= amount
        return self

    def get_value(self) -> int:
        return self.value

# Method chaining with Self type
builder = Builder(10)
result = builder.increment(5).decrement(3).increment(2).get_value()
print(f"Builder result: {result}")

# ===== Python 3.12 Features =====
print("\n--- Python 3.12 Features ---")

# F-string improvements
name = "Python"
version = 3.12

# In Python 3.12, you can use multiple quotes in f-strings
print(f"Using quotes in f-strings: {name = }, {version = }")

# In Python 3.12, you can use backslashes in f-string expressions
long_calculation = 1 + 2 + \
                  3 + 4
print(f"Result of long calculation: {long_calculation}")

# Type parameter syntax (PEP 695)
# In Python 3.12, you can define generic classes and functions more easily

# Old way (before Python 3.12)
from typing import TypeVar, Generic, List

T = TypeVar('T')

class OldStack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# New way in Python 3.12
class Stack[T]:  # Type parameter directly in the class definition
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Using the generic classes
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(f"Popped from int_stack: {int_stack.pop()}")

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(f"Popped from str_stack: {str_stack.pop()}")

# New 'type' statement for type aliases
# In Python 3.12, you can use the 'type' statement for type aliases
type Point2D = tuple[float, float]  # Type alias using the new syntax

def distance(p1: Point2D, p2: Point2D) -> float:
    import math
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

point1: Point2D = (0.0, 0.0)
point2: Point2D = (3.0, 4.0)
print(f"Distance between points: {distance(point1, point2)}")

# ===== Python 3.13 Features =====
print("\n--- Python 3.13 Features ---")

# JIT (Just-In-Time) compiler
print("Python 3.13 introduces an experimental JIT compiler")
print("- Automatically optimizes hot code paths")
print("- Can significantly improve performance for CPU-bound code")
print("- No code changes required to benefit from it")

# Free-threaded mode (PEP 703)
print("\nPython 3.13 introduces experimental free-threaded mode")
print("- Removes the Global Interpreter Lock (GIL)")
print("- Allows true parallel execution of Python threads")
print("- Can be enabled with a command-line flag")
print("- Improves performance for multi-threaded CPU-bound tasks")

# New interactive interpreter (REPL)
print("\nPython 3.13 includes a new interactive interpreter (REPL)")
print("- Syntax highlighting")
print("- Better multiline editing")
print("- Improved tab completion")
print("- Command history with search")

# Enhanced error messages
print("\nPython 3.13 further improves error messages")
print("- More precise error locations")
print("- Better suggestions for fixing errors")
print("- More helpful context in tracebacks")

# Improved typing features
print("\nPython 3.13 includes typing improvements")
print("- Type parameter defaults")
print("- Better support for variadic generics")
print("- More precise type checking")

##############################################################################
# SECTION 5: PYDANTIC AND PYDANTIC AI
##############################################################################

print("\n=== SECTION 5: PYDANTIC AND PYDANTIC AI ===")

# ===== Pydantic Basics =====
print("\n--- Pydantic Basics ---")

# Pydantic is a data validation and settings management library
# It uses Python type annotations to validate data and manage configurations
from pydantic import BaseModel, Field, ValidationError, validator
from typing import List, Optional, Dict, Union
from datetime import datetime
import uuid

# Basic model definition
class User(BaseModel):
    """A Pydantic model representing a user."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)  # Auto-generated UUID
    username: str
    email: str
    full_name: Optional[str] = None  # Optional field with default None
    age: int = Field(gt=0, lt=120)  # Field with validation constraints
    is_active: bool = True  # Field with default value
    created_at: datetime = Field(default_factory=datetime.now)  # Auto-generated timestamp
    tags: List[str] = []  # List field with default empty list

# Creating a model instance
try:
    # Valid data
    user = User(
        username="johndoe",
        email="john@example.com",
        full_name="John Doe",
        age=30,
        tags=["developer", "python"]
    )
    print(f"User created: {user}")

    # Access fields
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Age: {user.age}")

    # Convert to dictionary
    user_dict = user.model_dump()
    print(f"User as dict: {user_dict}")

    # Convert to JSON
    user_json = user.model_dump_json()
    print(f"User as JSON: {user_json}")

    # Invalid data (will raise ValidationError)
    invalid_user = User(
        username="alice",
        email="invalid-email",  # Invalid email format
        age=-5  # Invalid age (must be > 0)
    )
except ValidationError as e:
    print(f"Validation error: {e}")

# Custom validators
class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)  # Price must be greater than 0
    tags: List[str] = []

    # Custom validator for name field
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.title()  # Convert to title case

    # Custom validator for tags field
    @validator('tags')
    def tags_must_be_unique(cls, v):
        if len(v) != len(set(v)):
            raise ValueError('Tags must be unique')
        return v

try:
    # Valid product
    product = Product(id=1, name="laptop", price=999.99, tags=["electronics", "computers"])
    print(f"\nProduct created: {product}")

    # Invalid product (empty name)
    invalid_product = Product(id=2, name="", price=10.99)
except ValidationError as e:
    print(f"Product validation error: {e}")

# Nested models
class Address(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str

class Customer(BaseModel):
    id: int
    name: str
    addresses: List[Address]  # List of Address models
    primary_address: Optional[Address] = None  # Optional nested model

# Create a customer with nested address models
address1 = Address(street="123 Main St", city="New York", country="USA", postal_code="10001")
address2 = Address(street="456 Elm St", city="San Francisco", country="USA", postal_code="94107")

customer = Customer(
    id=1,
    name="Jane Smith",
    addresses=[address1, address2],
    primary_address=address1
)

print(f"\nCustomer created: {customer}")
print(f"Primary address city: {customer.primary_address.city}")

# ===== Pydantic AI =====
print("\n--- Pydantic AI ---")

# Pydantic AI is an extension of Pydantic for working with AI models
# It provides tools for structured extraction from LLM outputs

print("Pydantic AI is a framework for building AI agents with structured data")
print("Key features include:")
print("1. Structured extraction from LLM outputs")
print("2. Function calling and tool usage")
print("3. Agent frameworks for complex workflows")
print("4. Type safety and validation")

# Example of a Pydantic AI model (conceptual, not runnable without actual AI backend)
class MovieReview(BaseModel):
    """A model for extracting structured movie review data from text."""
    title: str = Field(description="The title of the movie")
    director: str = Field(description="The director of the movie")
    year: int = Field(description="The year the movie was released")
    rating: float = Field(description="Rating from 0-10", ge=0, le=10)
    review: str = Field(description="A brief review of the movie")
    genres: List[str] = Field(description="List of genres for the movie")

# In a real application with Pydantic AI, you would use it like this:
# (This is just an example and won't run without the actual library)
'''
from pydantic_ai import AI

# Initialize AI with your API key
ai = AI(api_key="your_api_key")

# Extract structured data from text
text = "I watched The Shawshank Redemption directed by Frank Darabont. \
        This 1994 drama is a masterpiece that deserves a solid 9.5/10. \
        It tells the story of a man's experience in prison and his eventual escape. \
        It's both a drama and a crime film with elements of friendship and hope."

# Extract structured data using the MovieReview model
result = ai.extract(text, MovieReview)
print(f"Extracted movie review: {result}")
'''

print("\nExample of what extracted data might look like:")
print('''
{
    "title": "The Shawshank Redemption",
    "director": "Frank Darabont",
    "year": 1994,
    "rating": 9.5,
    "review": "A masterpiece that tells the story of a man's experience in prison and his eventual escape.",
    "genres": ["Drama", "Crime"]
}
''')

# Function calling with Pydantic AI
print("\nPydantic AI also supports function calling:")

class SearchQuery(BaseModel):
    query: str = Field(description="The search query")
    max_results: int = Field(description="Maximum number of results to return", default=5)

class WeatherQuery(BaseModel):
    location: str = Field(description="The location to get weather for")
    unit: str = Field(description="Temperature unit (celsius/fahrenheit)", default="celsius")

# Example code (not runnable without the actual library):
'''
# Define functions that can be called by the AI
def search(query: SearchQuery) -> List[str]:
    # In a real application, this would call a search API
    return [f"Result {i} for {query.query}" for i in range(query.max_results)]

def get_weather(query: WeatherQuery) -> Dict[str, Union[str, float]]:
    # In a real application, this would call a weather API
    return {
        "location": query.location,
        "temperature": 22.5 if query.unit == "celsius" else 72.5,
        "condition": "Sunny",
        "unit": query.unit
    }

# Register functions with the AI
ai.register_function(search)
ai.register_function(get_weather)

# Let the AI decide which function to call based on user input
user_input = "What's the weather like in New York?"
result = ai.run(user_input)
print(f"AI response: {result}")
'''

print("Example of what a function call result might look like:")
print('''
{
    "location": "New York",
    "temperature": 22.5,
    "condition": "Sunny",
    "unit": "celsius"
}
''')

# Agent frameworks with Pydantic AI
print("\nPydantic AI provides agent frameworks for complex workflows:")
print("- Agents can use tools and make decisions")
print("- Chain multiple steps together")
print("- Handle complex reasoning tasks")
print("- Maintain state across interactions")

# Example of a simple agent (conceptual, not runnable)
'''
from pydantic_ai import Agent, Tool

# Define tools the agent can use
search_tool = Tool(search, description="Search for information")
weather_tool = Tool(get_weather, description="Get weather information")

# Create an agent with the tools
agent = Agent(tools=[search_tool, weather_tool])

# Run the agent with a user query
result = agent.run("I'm planning a trip to Paris next week. What's the weather forecast and what are some must-see attractions?")
print(f"Agent response: {result}")
'''

print("\nPydantic AI is particularly useful for:")
print("1. Building chatbots with structured responses")
print("2. Creating AI assistants that can take actions")
print("3. Extracting structured data from unstructured text")
print("4. Implementing complex decision-making workflows")
print("5. Ensuring type safety in AI applications")

##############################################################################
# CONCLUSION
##############################################################################

print("\n=== CONCLUSION ===")
print("\nThis tutorial has covered Python from basic to advanced concepts, including:")
print("- Basic syntax, data types, and control structures")
print("- Object-oriented programming with classes and inheritance")
print("- Advanced features like threading, asyncio, and generators")
print("- Modern Python features from versions 3.10 through 3.13")
print("- Data validation and AI integration with Pydantic and Pydantic AI")

print("\nPython continues to evolve with new features and improvements in each version.")
print("The language's readability, extensive standard library, and vibrant ecosystem")
print("make it an excellent choice for beginners and experts alike.")

print("\nHappy coding!")
