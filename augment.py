#!/usr/bin/env python3
"""
Python Tutorial: From Basics to Advanced

This file serves as a comprehensive tutorial covering Python from basic to advanced concepts,
including the latest features from Python 3.10 through 3.14 (as of July 2025).

Each section contains executable code examples with detailed comments explaining the concepts.
The tutorial is regularly updated to include the most current Python features and best practices.

Version Coverage:
- Python 3.10: Pattern matching, improved error messages
- Python 3.11: Performance improvements, exception groups, Self type
- Python 3.12: F-string enhancements, new generics syntax
- Python 3.13: Free-threading, JIT compiler, mobile support, new REPL
- Python 3.14: JIT improvements, threading enhancements (in development)
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
#    - Python 3.11: Performance Improvements, Exception Groups, Self Type
#    - Python 3.12: F-string Improvements, New Type Annotation Syntax
#    - Python 3.13: Free-Threading, JIT Compiler, Mobile Support, New REPL
#    - Python 3.14: JIT Maturation, Threading Enhancements (in development)
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
    try:
        # Create a pool of worker processes
        with multiprocessing.Pool(processes=3) as pool:
            # Map the function to the inputs
            results = pool.map(cpu_bound_task, [1000000, 2000000, 3000000])
            print(f"Pool results: {results}")
    except Exception as e:
        print(f"Multiprocessing encountered an error: {e}")
        print("Continuing with the rest of the tutorial...")

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
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Asyncio main() encountered an error: {e}")
        print("Continuing with the rest of the tutorial...")

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
    try:
        asyncio.run(use_async_resource())
    except Exception as e:
        print(f"Async context manager encountered an error: {e}")
        print("Continuing with the rest of the tutorial...")

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
# SECTION 4: MODERN PYTHON FEATURES (3.10-3.14)
##############################################################################

print("\n=== SECTION 4: MODERN PYTHON FEATURES (3.10-3.14) ===")

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
print("\n--- Python 3.13 Features (Released October 2024) ---")

# Free-threaded CPython (PEP 703) - Most significant feature
print("🚀 Free-threaded CPython (PEP 703) - EXPERIMENTAL")
print("- Removes the Global Interpreter Lock (GIL) when built with --disable-gil")
print("- Enables true parallel execution of Python threads")
print("- Requires special interpreter build: python3.13t")
print("- Significant performance gains for multi-threaded CPU-bound tasks")
print("- Still experimental - use with caution in production")

# Example: CPU-bound task that benefits from free-threading
import threading
import time
import sys

def cpu_intensive_task(n: int, result_list: list, index: int) -> None:
    """A CPU-intensive task that benefits from parallel execution."""
    total = 0
    for i in range(n):
        total += i ** 2
    result_list[index] = total

def demonstrate_free_threading():
    """Demonstrate potential benefits of free-threading in Python 3.13."""
    print("\nFree-threading demonstration:")
    
    # Check if we're running with free-threading enabled
    gil_enabled = sys._is_gil_enabled() if hasattr(sys, '_is_gil_enabled') else True
    print(f"GIL enabled: {gil_enabled}")
    
    # Run CPU-intensive tasks
    n_tasks = 4
    n_iterations = 1000000
    results = [0] * n_tasks
    
    # Measure time with threading
    start_time = time.time()
    threads = []
    
    for i in range(n_tasks):
        thread = threading.Thread(target=cpu_intensive_task, args=(n_iterations, results, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    threading_time = time.time() - start_time
    print(f"Threading time: {threading_time:.3f}s")
    print(f"Results sum: {sum(results)}")
    
    if not gil_enabled:
        print("✅ Running with free-threading - true parallelism achieved!")
    else:
        print("ℹ️ Running with GIL - threads run sequentially for CPU-bound tasks")

demonstrate_free_threading()

# JIT Compiler - Experimental
print("\n⚡ Experimental JIT Compiler (Copy-and-Patch)")
print("- Highly experimental just-in-time compiler")
print("- Uses copy-and-patch compilation technique") 
print("- Must be enabled explicitly (not default)")
print("- Can provide significant speedups for certain workloads")
print("- Still in early development - expect changes")

def fibonacci_jit_demo(n: int) -> int:
    """Function that could benefit from JIT compilation."""
    if n <= 1:
        return n
    return fibonacci_jit_demo(n-1) + fibonacci_jit_demo(n-2)

# Demonstrate potential JIT benefits (conceptual)
print("\nJIT Compiler demonstration:")
print("To enable JIT in Python 3.13:")
print("  python3.13 -X jit your_script.py")
print("Or set environment variable: PYTHON_JIT=1")

# Simple benchmark function that could benefit from JIT
def jit_benchmark_function(iterations: int) -> float:
    """Function with tight loops that benefits from JIT."""
    total = 0.0
    for i in range(iterations):
        total += (i * 2.5) ** 0.5
    return total

result = jit_benchmark_function(100000)
print(f"Benchmark result: {result:.2f}")
print("Note: With JIT enabled, this function could run significantly faster")

# New Interactive REPL
print("\n🎯 New Interactive Interpreter (PyREPL)")
print("- Complete rewrite of the interactive shell")
print("- Syntax highlighting with color support")
print("- Improved multiline editing capabilities")
print("- Enhanced tab completion and introspection")
print("- Command history with search functionality")
print("- Better error handling and display")

# Demonstrate REPL features (conceptual since we can't show interactive features in a script)
print("\nPyREPL features demonstration:")
print("1. Syntax highlighting: Keywords, strings, and numbers are colored")
print("2. Better multiline editing: Improved indentation and bracket matching")
print("3. Enhanced tab completion: More intelligent suggestions")
print("4. History search: Ctrl+R for reverse search through command history")

# iOS and Android Support
print("\n📱 Mobile Platform Support")
print("- Official support for iOS and Android platforms")
print("- PEP 730: iOS support in the standard library")
print("- PEP 738: Android support improvements")
print("- Enhanced mobile app development capabilities")
print("- Better integration with mobile development workflows")

# Example: Platform detection for mobile platforms
import platform

def detect_mobile_platform():
    """Detect if running on mobile platform (Python 3.13+)."""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    # Check for iOS
    if system == 'darwin' and ('iphone' in machine or 'ipad' in machine):
        return 'iOS'
    elif system == 'ios':  # Direct iOS detection in Python 3.13+
        return 'iOS'
    
    # Check for Android
    if 'android' in system or hasattr(sys, 'getandroidapilevel'):
        return 'Android'
    
    return 'Desktop/Server'

mobile_platform = detect_mobile_platform()
print(f"Detected platform: {mobile_platform}")

# Mobile-specific code example
if mobile_platform != 'Desktop/Server':
    print(f"Running on {mobile_platform} - can use mobile-specific features")
    # Example: Access mobile-specific APIs (conceptual)
    print("- Access to device sensors")
    print("- Integration with mobile notifications")
    print("- Touch event handling")

# Enhanced Error Messages
print("\n🔍 Enhanced Error Messages")
print("- More precise error location indicators")
print("- Better suggestions for fixing common errors")
print("- Improved traceback formatting and context")
print("- More helpful hints for beginners")

# Example: Enhanced error message demonstration
def demonstrate_enhanced_errors():
    """Show improved error messages in Python 3.13."""
    try:
        # This will show enhanced error information in Python 3.13+
        data = {'name': 'Alice', 'age': 30}
        # Intentionally access a non-existent key
        # print(data['address'])  # Would show: "Did you mean 'age'?"
        
        # Intentionally use wrong method
        numbers = [1, 2, 3, 4, 5]
        # result = numbers.append(6).sort()  # Would suggest chaining fix
        
        print("Error message improvements (examples commented to avoid actual errors):")
        print("- KeyError now suggests similar keys")
        print("- AttributeError shows available methods")
        print("- SyntaxError points to exact problematic character")
        print("- TypeError includes helpful suggestions")
        
    except Exception as e:
        print(f"Enhanced error: {e}")

demonstrate_enhanced_errors()

# Typing Improvements
print("\n📝 Typing System Enhancements")
print("- Type parameter defaults (PEP 696)")
print("- Improved support for variadic generics")
print("- Better generic type inference")
print("- Enhanced runtime type checking capabilities")

# Type parameter defaults (PEP 696)
from typing import TypeVar, Generic, List

# Default type parameters in Python 3.13+
T = TypeVar('T')  # In Python 3.13+, can specify default=str

class Container(Generic[T]):  # Compatible syntax
    """Generic container with type parameter."""
    def __init__(self, value: T) -> None:
        self.value = value
    
    def get(self) -> T:
        return self.value
    
    def set(self, value: T) -> None:
        self.value = value

# Usage examples
container_str = Container[str]("hello")  # T explicitly set to str
container_int = Container[int](42)       # T explicitly set to int

print(f"String container: {container_str.get()}")
print(f"Int container: {container_int.get()}")

# Note: In Python 3.13+, you can use the new syntax:
# class Container[T = str]:  # Default type parameter
# T = TypeVar('T', default=str)  # Default type variable

# Improved variadic generics
from typing import TypeVarTuple, Unpack

# Variadic generics for functions with variable arguments
Ts = TypeVarTuple('Ts')

def process_args(*args: Unpack[Ts]) -> tuple[Unpack[Ts]]:
    """Function that preserves argument types."""
    return args

# Type-safe variable arguments
result1 = process_args(1, "hello", 3.14)  # Returns tuple[int, str, float]
result2 = process_args(True, [1, 2, 3])   # Returns tuple[bool, list[int]]

print(f"Variadic result 1: {result1}")
print(f"Variadic result 2: {result2}")

# Security and Performance
print("\n🔒 Security and Performance Improvements")
print("- Enhanced security features and CVE fixes")
print("- Memory usage optimizations")
print("- Startup time improvements")
print("- Better garbage collection performance")

# Performance monitoring example
import gc
import tracemalloc

def demonstrate_performance_improvements():
    """Show performance monitoring capabilities."""
    # Start memory tracing
    tracemalloc.start()
    
    # Create some objects to demonstrate memory usage
    large_list = [i * i for i in range(10000)]
    large_dict = {f"key_{i}": f"value_{i}" for i in range(5000)}
    
    # Get current memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
    
    # Garbage collection statistics
    gc_stats = gc.get_stats()
    print(f"GC collections: {sum(stat['collections'] for stat in gc_stats)}")
    
    tracemalloc.stop()

demonstrate_performance_improvements()

# Standard Library Updates
print("\n📚 Standard Library Updates")
print("- pathlib improvements for better path handling")
print("- Enhanced warnings system with new filters")
print("- Improved docstring parsing capabilities")
print("- Various module updates and bug fixes")

# Enhanced pathlib features
from pathlib import Path
import warnings

def demonstrate_stdlib_improvements():
    """Show standard library improvements in Python 3.13."""
    
    # Enhanced pathlib operations
    current_path = Path(".")
    print(f"Current directory: {current_path.resolve()}")
    
    # Better path manipulation (Python 3.13+ improvements)
    temp_path = Path("/tmp") / "example.txt"
    print(f"Constructed path: {temp_path}")
    
    # Enhanced warnings system
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter("always")
        
        # Trigger a warning
        warnings.warn("This is a test warning", UserWarning)
        
        if warning_list:
            w = warning_list[0]
            print(f"Caught warning: {w.message}")
            print(f"Warning category: {w.category.__name__}")
    
    # Improved docstring handling
    def example_function():
        """
        This is an example function.
        
        Returns:
            None: This function doesn't return anything.
        """
        pass
    
    # In Python 3.13+, docstring parsing is more robust
    print(f"Function docstring: {example_function.__doc__}")

demonstrate_stdlib_improvements()

# ===== Python 3.14 Features =====
print("\n--- Python 3.14 Features (Expected October 2025) ---")
print("🔮 Note: As of July 2025, Python 3.14 is in development/beta")

# JIT Compiler Improvements
print("\n⚡ JIT Compiler Maturation")
print("- Copy-and-patch JIT compiler is more stable")
print("- Better optimization heuristics")
print("- Reduced compilation overhead")
print("- Improved compatibility with existing code")
print("- May become enabled by default in certain scenarios")

# Enhanced JIT examples (conceptual for Python 3.14)
def demonstrate_jit_improvements():
    """Demonstrate expected JIT improvements in Python 3.14."""
    print("\nJIT Compiler Improvements in Python 3.14:")
    
    # Example: Function that benefits from JIT optimization
    def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        """Matrix multiplication that benefits from JIT compilation."""
        rows_a, cols_a = len(a), len(a[0])
        rows_b, cols_b = len(b), len(b[0])
        
        if cols_a != rows_b:
            raise ValueError("Incompatible matrix dimensions")
        
        result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]
        
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += a[i][k] * b[k][j]
        
        return result
    
    # Small matrices for demonstration
    matrix_a = [[1.0, 2.0], [3.0, 4.0]]
    matrix_b = [[5.0, 6.0], [7.0, 8.0]]
    
    result = matrix_multiply(matrix_a, matrix_b)
    print(f"Matrix multiplication result: {result}")
    print("✨ In Python 3.14, this computation would be JIT-compiled for better performance")
    
    # JIT compilation status check (conceptual)
    print("\nJIT Status (Python 3.14 features):")
    print("- Automatic JIT compilation for hot code paths")
    print("- Better integration with type hints for optimization")
    print("- Reduced compilation latency")
    print("- Improved memory usage during compilation")

demonstrate_jit_improvements()

# Further GIL Improvements
print("\n🔄 Free-Threading Enhancements")
print("- More libraries compatible with free-threaded mode")
print("- Better performance in free-threaded builds")
print("- Reduced overhead when GIL is disabled")
print("- Improved debugging tools for threaded code")

# Enhanced free-threading examples
import concurrent.futures
import asyncio
from typing import Callable, Any

def demonstrate_enhanced_free_threading():
    """Show improved free-threading capabilities in Python 3.14."""
    print("\nEnhanced Free-Threading in Python 3.14:")
    
    # Better thread pool performance
    def parallel_task(n: int) -> int:
        """CPU-intensive task that benefits from true parallelism."""
        return sum(i ** 2 for i in range(n))
    
    # Using ThreadPoolExecutor with improved free-threading
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        tasks = [1000, 2000, 3000, 4000]
        futures = [executor.submit(parallel_task, task) for task in tasks]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    
    print(f"Parallel task results: {sorted(results)}")
    print("✨ In Python 3.14 with free-threading, these tasks run truly in parallel")
    
    # Enhanced debugging for threaded code
    print("\nImproved Threading Debugging (Python 3.14):")
    print("- Better thread state introspection")
    print("- Enhanced deadlock detection")
    print("- Improved thread performance profiling")
    print("- Better integration with debuggers")

demonstrate_enhanced_free_threading()

# Performance Improvements
print("\n🚀 Performance Optimizations")
print("- Further interpreter optimizations")
print("- Improved memory management")
print("- Faster startup times")
print("- Better optimization of common patterns")

# Performance optimization examples
def demonstrate_performance_optimizations():
    """Show performance improvements expected in Python 3.14."""
    print("\nPerformance Optimizations in Python 3.14:")
    
    # Optimized comprehensions
    large_range = 100000
    
    # List comprehension with better optimization
    squared_evens = [x ** 2 for x in range(large_range) if x % 2 == 0]
    print(f"Generated {len(squared_evens)} squared even numbers")
    
    # Dictionary comprehension with improved performance
    number_mapping = {i: f"number_{i}" for i in range(1000)}
    print(f"Created dictionary with {len(number_mapping)} entries")
    
    # Set operations with better optimization
    set_a = {i for i in range(5000)}
    set_b = {i for i in range(2500, 7500)}
    intersection = set_a & set_b
    print(f"Set intersection size: {len(intersection)}")
    
    print("✨ All these operations are faster in Python 3.14 due to:")
    print("  - Better memory allocation strategies")
    print("  - Optimized bytecode for common patterns")
    print("  - Improved garbage collection algorithms")

demonstrate_performance_optimizations()

# Language Features
print("\n🔧 Language Enhancements")
print("- Potential new syntax features (TBD)")
print("- Enhanced pattern matching capabilities")
print("- Improved comprehension performance")
print("- Better support for modern Python idioms")

# Enhanced language features (conceptual)
def demonstrate_language_enhancements():
    """Show potential language enhancements in Python 3.14."""
    print("\nLanguage Enhancements in Python 3.14:")
    
    # Enhanced pattern matching (building on Python 3.10)
    def process_data_enhanced(data: Any) -> str:
        """Enhanced pattern matching with more features."""
        match data:
            case int(x) if x > 100:
                return f"Large integer: {x}"
            case int(x) if x > 0:
                return f"Positive integer: {x}"
            case str(s) if len(s) > 10:
                return f"Long string: {s[:10]}..."
            case str(s):
                return f"Short string: {s}"
            case list([first, *rest]) if len(rest) > 5:
                return f"Long list starting with {first}"
            case list(items):
                return f"List with {len(items)} items"
            case dict(data) if "priority" in data:
                return f"Priority data: {data['priority']}"
            case _:
                return f"Unknown data type: {type(data)}"
    
    # Test enhanced pattern matching
    test_cases = [
        150,
        5,
        "This is a very long string for testing",
        "short",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 2, 3],
        {"priority": "high", "task": "complete"},
        {"normal": "data"},
        3.14
    ]
    
    for case in test_cases:
        result = process_data_enhanced(case)
        print(f"  {case} -> {result}")
    
    # Improved comprehension syntax (conceptual)
    print("\nImproved comprehensions (potential Python 3.14 features):")
    
    # Better error handling in comprehensions
    def safe_divide(a: float, b: float) -> float | None:
        return a / b if b != 0 else None
    
    numbers = [1, 2, 0, 4, 5]
    safe_results = [result for x in numbers if (result := safe_divide(10, x)) is not None]
    print(f"Safe division results: {safe_results}")

demonstrate_language_enhancements()

# Standard Library Evolution
print("\n📖 Standard Library Updates")
print("- Continued pathlib enhancements")
print("- New modules for modern development")
print("- Deprecated module removals")
print("- Better integration with external tools")

# Enhanced standard library features
def demonstrate_stdlib_evolution():
    """Show standard library evolution in Python 3.14."""
    print("\nStandard Library Evolution in Python 3.14:")
    
    # Enhanced pathlib with more methods
    from pathlib import Path
    import tempfile
    import json
    
    # Better path operations (conceptual Python 3.14 features)
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Enhanced file operations
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        sample_data = {"version": "3.14", "features": ["JIT", "free-threading"]}
        json.dump(sample_data, f)
        temp_path = Path(f.name)
    
    # Better path manipulation (enhanced in 3.14)
    print(f"Temporary file: {temp_path}")
    print(f"File size: {temp_path.stat().st_size} bytes")
    
    # Clean up
    temp_path.unlink()
    
    # New modules for modern development (conceptual)
    print("\nNew standard library modules (Python 3.14):")
    print("- Enhanced async utilities")
    print("- Better data validation tools")
    print("- Improved debugging modules")
    print("- Modern web development helpers")

demonstrate_stdlib_evolution()

# Developer Experience
print("\n👩‍💻 Developer Experience")
print("- Enhanced debugging capabilities")
print("- Better profiling tools")
print("- Improved IDE integration")
print("- More helpful development warnings")

# Enhanced developer experience
def demonstrate_developer_experience():
    """Show improved developer experience in Python 3.14."""
    print("\nDeveloper Experience Improvements in Python 3.14:")
    
    # Better debugging with enhanced tracebacks
    def nested_function_call():
        def inner_function():
            def deepest_function():
                # In Python 3.14, this would show enhanced stack traces
                data = {"key": "value"}
                return data["nonexistent_key"]  # This would cause KeyError
            return deepest_function()
        return inner_function()
    
    try:
        # nested_function_call()  # Commented to avoid actual error
        pass
    except KeyError:
        print("Enhanced traceback would show:")
        print("  - Exact line numbers with context")
        print("  - Variable values at each frame")
        print("  - Suggested fixes for common errors")
        print("  - Better formatting for readability")
    
    # Improved profiling capabilities
    import cProfile
    import pstats
    import io
    
    def sample_function():
        """Function to profile."""
        return sum(i ** 2 for i in range(1000))
    
    # Enhanced profiling (conceptual Python 3.14 features)
    print("\nEnhanced Profiling in Python 3.14:")
    profiler = cProfile.Profile()
    profiler.enable()
    
    result = sample_function()
    
    profiler.disable()
    
    # Better profiling output
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s)
    ps.print_stats()
    
    print(f"Function result: {result}")
    print("✨ Python 3.14 profiling improvements:")
    print("  - Better memory profiling integration")
    print("  - Enhanced call graph visualization")
    print("  - Improved IDE integration")
    print("  - Real-time performance monitoring")

demonstrate_developer_experience()

print("\n📅 Note: Python 3.14 features are subject to change during development")
print("Check the official Python documentation for the latest updates")

# Preparing for Python 3.14
print("\n🔮 Preparing for Python 3.14:")
print("1. Start experimenting with Python 3.13 free-threading")
print("2. Profile your code to identify JIT optimization opportunities")
print("3. Update type hints for better optimization")
print("4. Consider thread-safe design patterns")
print("5. Stay updated with Python Enhancement Proposals (PEPs)")

# Version Summary
print("\n=== Python Version Summary ===")
print("🐍 Python 3.10: Pattern matching, better error messages")
print("🐍 Python 3.11: 25% performance boost, exception groups, Self type")
print("🐍 Python 3.12: F-string improvements, new type syntax, generics")
print("🐍 Python 3.13: Free-threading, JIT compiler, mobile support, new REPL")
print("🐍 Python 3.14: JIT maturation, threading improvements (in development)")
print("\n💡 Recommendation: Use Python 3.11+ for production, 3.13+ for experimentation")

##############################################################################
# SECTION 5: PYDANTIC AND PYDANTIC AI
##############################################################################

print("\n=== SECTION 5: PYDANTIC AND PYDANTIC AI ===")

# ===== Pydantic Basics =====
print("\n--- Pydantic Basics ---")

# Pydantic is a data validation and settings management library
# It uses Python type annotations to validate data and manage configurations
try:
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

except ImportError:
    print("Pydantic is not installed. To install it, run: pip install pydantic")
    print("The Pydantic section has been skipped.")
    print("\nPydantic is a data validation and settings management library using Python type annotations.")
    print("It would be demonstrated here if installed.")
except Exception as e:
    print(f"Error in Pydantic section: {e}")
    print("Continuing with the rest of the tutorial...")

##############################################################################
# CONCLUSION
##############################################################################

print("\n=== CONCLUSION ===")
print("\nThis tutorial has covered Python from basic to advanced concepts, including:")
print("- Basic syntax, data types, and control structures")
print("- Object-oriented programming with classes and inheritance")
print("- Advanced features like threading, asyncio, and generators")
print("- Modern Python features from versions 3.10 through 3.14")
print("- Data validation and AI integration with Pydantic and Pydantic AI")

print("\nPython continues to evolve rapidly with new features and improvements in each version.")
print("Recent developments like free-threading and JIT compilation show Python's commitment")
print("to performance and modern computing paradigms. The language's readability, extensive")
print("standard library, and vibrant ecosystem make it an excellent choice for beginners and")
print("experts alike.")

print("\n🔮 Looking Forward:")
print("- Python 3.14 (October 2025) will bring JIT and threading maturation")
print("- Mobile development support continues to improve")
print("- Performance remains a key focus with ongoing optimizations")
print("- The ecosystem continues to grow with modern tools and libraries")

print("\nHappy coding!")
