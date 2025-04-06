# -*- coding: utf-8 -*-
"""
Comprehensive Python Learning Script (Updated for Python ~3.13 Features)

This script covers Python basics, intermediate concepts, and advanced features,
including additions and changes up to approximately Python 3.13.
It's designed as a single-file learning resource with extensive comments.

Run this file using: python comprehensive_python_script.py

Current Date Context: Sunday, April 6, 2025
Latest Python Version Context: Stable is likely 3.13, with 3.12 widely used.
"""

# ==============================================================================
# Section 0: Imports (Grouped for clarity)
# ==============================================================================
import sys
import math
import os
import random
import time
import threading
import asyncio
import abc
import functools
import typing # For older type hints & specific tools like TypeVar pre-3.12
import tomllib # Added in Python 3.11
from contextlib import contextmanager
from datetime import datetime

# Attempt to import Pydantic (optional external library)
try:
    from pydantic import BaseModel, Field, ValidationError, EmailStr, HttpUrl
    PYDANTIC_INSTALLED = True
except ImportError:
    PYDANTIC_INSTALLED = False
    # Define dummy classes if Pydantic is not installed to avoid NameErrors later
    class BaseModel: pass
    class Field: pass
    class ValidationError(Exception): pass
    class EmailStr(str): pass
    class HttpUrl(str): pass

# Import typing features introduced across versions
try:
    from typing import Self # Added in Python 3.11
except ImportError:
    Self = typing.TypeVar('Self') # Basic fallback for older versions

# Check Python version for features
PYTHON_VERSION = sys.version_info

# ==============================================================================
# Section 1: Python Basics
# ==============================================================================

print("=== Section 1: Python Basics ===")
print(f"Running on Python Version: {PYTHON_VERSION.major}.{PYTHON_VERSION.minor}.{PYTHON_VERSION.micro}")

# --- 1.1 Comments ---
# Single-line comment.
"""Multi-line comment (docstring)."""

# --- 1.2 Variables and Data Types ---
age: int = 30          # Integer (type hint added)
price: float = 19.99   # Float
name: str = "Alice"    # String
is_active: bool = True # Boolean
result: None = None    # NoneType

print(f"Age: {age} ({type(age)})")
print(f"Price: {price} ({type(price)})")
print(f"Name: {name} ({type(name)})")
print(f"Is Active: {is_active} ({type(is_active)})")
print(f"Result: {result} ({type(result)})")

# --- 1.3 Basic Operators ---
# Arithmetic: +, -, *, /, // (floor), % (modulus), ** (exponent)
# Comparison: ==, !=, >, <, >=, <=
# Logical: and, or, not
# Assignment: =, +=, -=, *=, /=, etc.
a, b = 10, 3
print(f"\nOperators Example (a={a}, b={b}):")
print(f"a + b = {a + b}, a // b = {a // b}, a ** b = {a ** b}")
print(f"a > b = {a > b}, a == b = {a == b}")
print(f"True and False = {True and False}, not True = {not True}")
count = 0
count += 1
print(f"Count after += 1: {count}")

# --- 1.4 Input and Output ---
# print(...) for output
# input(...) for user input (returns string)
# try:
#     user_name = input("Enter your name: ")
#     print(f"Hello, {user_name}!")
#     user_age_str = input("Enter your age: ")
#     user_age_int = int(user_age_str) # Convert string to int
#     print(f"Next year you'll be {user_age_int + 1}.")
# except ValueError:
#     print("Invalid number entered for age.")
# except EOFError:
#     print("\nInput stream ended unexpectedly (maybe running non-interactively?).")


# --- 1.5 String Formatting ---
item = "Laptop"
cost = 1200.50

# f-strings (Python 3.6+) - Recommended
print(f"\nString Formatting (f-string): The {item} costs ${cost:.2f}.")

# f-string Enhancements (Python 3.12+)
# More flexible expressions inside {}: reuse quotes, multi-line, comments etc.
if PYTHON_VERSION >= (3, 12):
    print(" demonstrating f-string enhancements (Python 3.12+)...")
    print(f"Item details: {{'name': '{item.upper()}', 'price': {cost * 1.1:.2f} }}") # Reusing quotes
    print(f"""Multi-line f-string:
    Item: {item}
    Cost: {cost # This is a comment inside f-string
         * 1.0}""")
else:
    print(" (Skipping f-string enhancements demo, requires Python 3.12+)")

# .format() method
print(f"String Formatting (.format()): The {item} costs ${cost:.2f}.".format(item=item, cost=cost))

# % operator (Older style)
print("String Formatting (%% operator): The %s costs $%.2f." % (item, cost))


# ==============================================================================
# Section 2: Control Flow
# ==============================================================================

print("\n=== Section 2: Control Flow ===")

# --- 2.1 Conditional Statements (if, elif, else) ---
score = 75
print(f"\nConditional Statements (score={score}):")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D or F"
print(f"Grade: {grade}")

# --- 2.2 Loops ---
# For Loops (iterate over sequences)
print("\nFor Loop Examples:")
for i in range(3): print(f" Iteration {i}", end="")
print()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits): print(f" Index {index}: {fruit}", end="")
print()

# While Loops (repeat while condition is True)
print("\nWhile Loop Example:")
attempts = 2
while attempts > 0:
    print(f" Attempts remaining: {attempts}", end="")
    attempts -= 1
else: # Executes if loop finishes without 'break'
    print(" -> Loop finished normally.")

# Loop Control: break (exit loop), continue (skip iteration)
print("Loop Control:")
for num in range(5):
    if num == 1: continue
    if num == 3: break
    print(f" Processed {num}", end="")
else:
     print(" (Loop did not break)", end="") # This won't print if break is hit
print(" -> Loop ended.")

# --- 2.3 Structural Pattern Matching (match/case - Python 3.10+) ---
print("\nStructural Pattern Matching (match/case - Python 3.10+):")
if PYTHON_VERSION >= (3, 10):
    def process_command(command_data):
        match command_data:
            case "start":
                print(" Processing 'start' command.")
            case ("load", filename): # Match tuple structure, bind filename
                print(f" Processing 'load' command for file: {filename}")
            case {"action": "update", "id": item_id, "value": val}: # Match dict structure
                print(f" Processing 'update' action for item {item_id} with value {val}")
            case [x, y] if isinstance(x, int) and isinstance(y, int): # Match list + guard
                print(f" Processing point coordinates: ({x}, {y})")
            case _: # Wildcard: Matches anything not caught above
                print(" Unknown command format.")

    process_command("start")
    process_command(("load", "data.csv"))
    process_command({"action": "update", "id": 101, "value": "New Data"})
    process_command([5, 10])
    process_command("unknown")
    process_command({"action": "delete"}) # Matches wildcard
else:
    print(" (Skipping match/case demo, requires Python 3.10+)")

# ==============================================================================
# Section 3: Data Structures
# ==============================================================================

print("\n=== Section 3: Data Structures ===")

# --- 3.1 Lists ---
# Ordered, mutable, allow duplicates. []
my_list = [1, "hello", 3.14, True, 1]
my_list.append("new")
my_list[1] = "world"
print(f"\nList: {my_list}")
print(f"Slice [1:3]: {my_list[1:3]}")
squares = [x**2 for x in range(5)] # List comprehension
print(f"List Comprehension (squares): {squares}")

# --- 3.2 Tuples ---
# Ordered, immutable, allow duplicates. ()
my_tuple = (1, "hello", 3.14)
print(f"\nTuple: {my_tuple}")
print(f"First element: {my_tuple[0]}")
# my_tuple[0] = 5 # TypeError: 'tuple' object does not support item assignment

# --- 3.3 Dictionaries ---
# Key-value pairs, mutable. Keys immutable & unique. {}
# Ordered since Python 3.7.
student = {"name": "Bob", "age": 25, "courses": ["Math", "Physics"]}
student["age"] = 26
student["city"] = "New York"
print(f"\nDictionary: {student}")
print(f"Student name: {student.get('name')}") # Safe access with .get()
print(f"Keys: {list(student.keys())}")
squared_dict = {x: x**2 for x in range(4)} # Dict comprehension
print(f"Dict Comprehension: {squared_dict}")

# --- 3.4 Sets ---
# Unordered, mutable, no duplicates. {} or set()
my_set = {1, 2, 3, "hello", 3, 2} # {1, 2, 3, 'hello'}
my_set.add(4)
print(f"\nSet: {my_set}")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Is 3 in set_a? {3 in set_a}") # Fast membership check

# ==============================================================================
# Section 4: Functions
# ==============================================================================

print("\n=== Section 4: Functions ===")

# --- 4.1 Defining and Calling Functions ---
def greet(name: str) -> None: # Added type hints
    """Greets a person by name."""
    print(f"Hello, {name}!")

greet("Charlie")

def add(x: float, y: float) -> float: # Added type hints
    """Adds two numbers."""
    return x + y

result_add = add(5.5, 4.5)
print(f"add(5.5, 4.5) = {result_add}")

# --- 4.2 Function Arguments ---
# Positional, Keyword, Default, *args (tuple of extra positional), **kwargs (dict of extra keyword)
def func_args(a, b=10, *args, **kwargs):
    print(f" a={a}, b={b}, args={args}, kwargs={kwargs}")

func_args(1)                       # a=1, b=10, args=(), kwargs={}
func_args(1, 20, 100, 200, x=1, y=2) # a=1, b=20, args=(100, 200), kwargs={'x': 1, 'y': 2}

# --- 4.3 Scope ---
# LEGB Rule: Local, Enclosing function locals, Global, Built-in
global_var = "I'm global"
def scope_test():
    local_var = "I'm local"
    print(f" Inside: {local_var}, {global_var}")
scope_test()
print(f" Outside: {global_var}") # Can't access local_var here

# --- 4.4 Lambda Functions ---
# Small anonymous functions: lambda arguments: expression
multiply = lambda x, y: x * y
print(f"\nLambda multiply(5, 4): {multiply(5, 4)}")
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(f"Map with lambda (squared): {squared}")

# --- 4.5 Type Hinting (PEP 484 and newer) ---
print("\nType Hinting Examples:")

# Simple type hints (already used above)

# Using Union types (Python 3.10+ | syntax preferred)
def process_item(item: int | str) -> None: # Use | for Union
    print(f"Processing item: {item} (type: {type(item).__name__})")

process_item(100)
process_item("hello")

# Optional types (equivalent to Union[T, None])
def find_user(user_id: int) -> str | None: # Use | None for Optional
    if user_id == 1:
        return "Alice"
    return None

user = find_user(1)
print(f"Found user (ID 1): {user}")
user = find_user(2)
print(f"Found user (ID 2): {user}")

# Type hints for collections
def print_names(names: list[str]) -> None: # Use list[str], not List[str] (3.9+)
    if not names:
        print("No names provided.")
        return
    for name in names:
        print(f"- {name}")

print_names(["Alice", "Bob"])

# Using typing.Self (Python 3.11+) - See Section 5.6

# Using Generic Type Syntax (PEP 695 - Python 3.12+)
print("\nGeneric Type Syntax (PEP 695 - Python 3.12+):")
if PYTHON_VERSION >= (3, 12):
    # Define a generic function
    def get_first[T](container: list[T] | tuple[T, ...]) -> T | None:
        """Returns the first element of a list or tuple, or None if empty."""
        if not container:
            return None
        return container[0]

    # Define a generic class
    class Box[T]:
        def __init__(self, content: T):
            self._content = content
        def get_content(self) -> T:
            return self._content
        def __repr__(self) -> str:
            return f"Box({self._content!r})" # !r calls repr()

    int_list = [1, 2, 3]
    str_tuple = ("a", "b", "c")
    empty_list: list[float] = []

    first_int = get_first(int_list)
    first_str = get_first(str_tuple)
    first_empty = get_first(empty_list)
    print(f"First element of {int_list}: {first_int}")
    print(f"First element of {str_tuple}: {first_str}")
    print(f"First element of {empty_list}: {first_empty}")

    int_box = Box(100)
    str_box = Box("hello")
    print(f"Int box: {int_box}, Content: {int_box.get_content()}")
    print(f"Str box: {str_box}, Content: {str_box.get_content()}")
else:
    print(" (Skipping PEP 695 Generics demo, requires Python 3.12+)")
    # Fallback using older typing.TypeVar for conceptual understanding
    T_fallback = typing.TypeVar('T_fallback')
    def get_first_fallback(container: typing.Sequence[T_fallback]) -> T_fallback | None:
         if not container: return None
         return container[0]
    print(" (Using older TypeVar fallback for generics concept)")
    print(f" Fallback get_first([1,2,3]): {get_first_fallback([1,2,3])}")


# ==============================================================================
# Section 5: Object-Oriented Programming (OOP)
# ==============================================================================

print("\n=== Section 5: Object-Oriented Programming (OOP) ===")

# --- 5.1 Classes and Objects ---
class Dog:
    species = "Canis familiaris" # Class attribute
    def __init__(self, name: str, age: int):
        self.name = name # Instance attribute
        self.age = age
    def bark(self): print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", 3)
print(f"\nClass/Object: {dog1.name} is {dog1.age}, Species: {Dog.species}")
dog1.bark()

# --- 5.2 Inheritance ---
class Animal:
    def __init__(self, name: str): self.name = name
    def speak(self): raise NotImplementedError("Subclass must implement")

class Cat(Animal):
    def speak(self): print(f"{self.name} says Meow!") # Override method

cat1 = Cat("Whiskers")
cat1.speak()

# --- 5.3 Polymorphism ---
# Different objects responding to the same method call.
def make_speak(animal_obj: Animal): animal_obj.speak()

# make_speak(dog1) # Would fail if Dog doesn't inherit Animal or have speak()
make_speak(cat1) # Works

# Duck typing also enables polymorphism without inheritance
class Duck:
    def speak(self): print("Quack!")
make_speak(Duck()) # Works because Duck has a 'speak' method

# --- 5.4 Encapsulation ---
# Bundling data and methods. Using conventions for access control.
# Public: `attribute`
# Protected (convention): `_attribute`
# Private (name mangling): `__attribute` -> `_ClassName__attribute`
class BankAccount:
    def __init__(self, balance: float = 0.0):
        self._balance = balance # "Protected"
        self.__log = [] # "Private"
    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            self.__log_transaction(f"Deposit: {amount}")
    def get_balance(self) -> float: return self._balance # Controlled access
    def __log_transaction(self, msg): self.__log.append(msg) # Private method

acc = BankAccount(100)
acc.deposit(50)
print(f"Account balance: {acc.get_balance()}")
# print(acc.__log) # AttributeError
# print(acc._BankAccount__log) # Access via mangled name (discouraged)

# --- 5.5 Properties ---
# Methods that act like attributes (getters, setters, deleters)
class Temperature:
    def __init__(self, celsius: float): self.celsius = celsius # Calls setter
    @property # Getter
    def celsius(self) -> float: return self._celsius
    @celsius.setter # Setter
    def celsius(self, value: float):
        if value < -273.15: raise ValueError("Too cold!")
        self._celsius = value

temp = Temperature(25)
print(f"\nTemperature (property): {temp.celsius}°C")
temp.celsius = 30 # Calls setter
print(f"Updated temperature: {temp.celsius}°C")

# --- 5.6 Using typing.Self (Python 3.11+) ---
print("\nUsing typing.Self (Python 3.11+):")
class ConfigBuilder:
    def __init__(self):
        self._settings: dict[str, typing.Any] = {}

    def set_option(self, key: str, value: typing.Any) -> Self: # Returns instance of itself
        """Sets an option and returns the builder for chaining."""
        print(f" Setting {key} = {value}")
        self._settings[key] = value
        return self # Return self, annotated with Self

    def build(self) -> dict[str, typing.Any]:
        print(" Building configuration...")
        return self._settings.copy()

if PYTHON_VERSION >= (3, 11):
    builder = ConfigBuilder()
    config = (builder
              .set_option("host", "localhost") # Chaining works because set_option returns Self
              .set_option("port", 8080)
              .set_option("debug", True)
              .build()
             )
    print(f"Built config: {config}")
else:
    print(" (Skipping typing.Self demo, requires Python 3.11+)")
    # Without Self, you might annotate with the class name 'ConfigBuilder'
    # or use TypeVar('T', bound='ConfigBuilder') in older versions.

# ==============================================================================
# Section 6: Modules and Packages
# ==============================================================================

print("\n=== Section 6: Modules and Packages ===")

# Modules: .py files with Python code.
# Packages: Directories with modules and an __init__.py file.

# import math (already imported)
# import os as operating_system (already imported 'os')
# from random import choice, randint (already imported)

print(f"Pi: {math.pi:.4f}")
print(f"Random choice from [1,2,3]: {random.choice([1,2,3])}")
print(f"Current dir: {os.getcwd()}")

# The `if __name__ == "__main__":` block runs only when script is executed directly.
# See end of file.


# ==============================================================================
# Section 7: Error Handling (Exceptions)
# ==============================================================================

print("\n=== Section 7: Error Handling (Exceptions) ===")

# --- 7.1 Basic Try...Except...Else...Finally ---
print("\nBasic Try/Except:")
try:
    result = 10 / 0 # Raises ZeroDivisionError
except ZeroDivisionError:
    print(" Error: Cannot divide by zero!")
except TypeError as e:
    print(f" Error: Type mismatch - {e}")
except Exception as e: # Catch other exceptions
    print(f" An unexpected error: {e}")
else: # Runs if no exception occurred
    print(f" Division successful, result={result}")
finally: # Always runs
    print(" Finally block executed.")

# --- 7.2 Raising Exceptions ---
def check_positive(num):
    if num <= 0: raise ValueError("Number must be positive.")
    print(f" {num} is positive.")

try:
    check_positive(5)
    check_positive(-2)
except ValueError as e:
    print(f" Caught Error: {e}")

# --- 7.3 Custom Exceptions ---
class MyCustomError(Exception): pass
# try: raise MyCustomError("Something specific went wrong!")
# except MyCustomError as e: print(f" Caught Custom Error: {e}")

# --- 7.4 Exception Groups and except* (Python 3.11+) ---
print("\nException Groups and except* (Python 3.11+):")
if PYTHON_VERSION >= (3, 11):
    def func_a(): raise TypeError("Type issue in A")
    def func_b(): raise ValueError("Value issue in B")

    exceptions_to_raise = []
    try: func_a()
    except TypeError as e: exceptions_to_raise.append(e)
    try: func_b()
    except ValueError as e: exceptions_to_raise.append(e)

    if exceptions_to_raise:
        # Manually creating an ExceptionGroup for demonstration
        # Typically created automatically by constructs like asyncio.TaskGroup
        eg = ExceptionGroup("Multiple issues occurred", exceptions_to_raise)
        print(f"Created ExceptionGroup: {repr(eg)}")

        try:
            raise eg # Raise the group
        except* TypeError as e_type: # Handle only TypeErrors from the group
            print(f" Handled TypeError via except*: {e_type}")
        except* ValueError as e_val: # Handle only ValueErrors from the group
            print(f" Handled ValueError via except*: {e_val}")
        # The original ExceptionGroup (or a modified one containing unhandled
        # exceptions) would propagate if not all exceptions are handled.

    # Example integrated with asyncio.TaskGroup shown later in Section 10.2
else:
    print(" (Skipping Exception Groups / except* demo, requires Python 3.11+)")


# ==============================================================================
# Section 8: File I/O (Input/Output)
# ==============================================================================

print("\n=== Section 8: File I/O ===")

# --- 8.1 Reading and Writing Text Files ---
file_path = "temp_example_file.txt"
try:
    # Writing ('w' overwrites) using context manager (ensures file closure)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("First line.\n")
        f.write("Second line.\n")
    print(f" Wrote to '{file_path}'")

    # Reading ('r' is default mode)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f" Read content:\n---\n{content}---")

    # Appending ('a' adds to end)
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write("Third line (appended).\n")
    print(f" Appended to '{file_path}'")

    # Reading line by line
    print(" Reading lines:")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(f"  - {line.strip()}")

except IOError as e:
    print(f"File I/O Error: {e}")
finally:
    # Clean up the temporary file
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f" Cleaned up '{file_path}'")

# --- 8.2 Working with Binary Files ---
# Use 'rb' (read binary), 'wb' (write binary)
# try:
#     with open("temp_binary.bin", "wb") as f: f.write(b'\x01\x02\x03')
#     with open("temp_binary.bin", "rb") as f: data = f.read()
#     print(f"\nRead binary data: {data}")
#     os.remove("temp_binary.bin")
# except IOError as e: print(f"Binary File Error: {e}")

# --- 8.3 Parsing TOML Files (tomllib - Python 3.11+) ---
print("\nParsing TOML (tomllib - Python 3.11+):")
if PYTHON_VERSION >= (3, 11):
    toml_content = """
[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # First-class date type
"""
    try:
        # Parse TOML string using tomllib.loads
        parsed_data = tomllib.loads(toml_content)
        print("Successfully parsed TOML string:")
        print(f" Database server: {parsed_data['database']['server']}")
        print(f" Owner name: {parsed_data.get('owner', {}).get('name')}")
        print(f" Owner DoB type: {type(parsed_data['owner']['dob'])}") # Note: datetime object

        # To parse from a file, use tomllib.load(file_object) in binary read mode
        # with open("config.toml", "rb") as f:
        #     data = tomllib.load(f)

    except tomllib.TOMLDecodeError as e:
        print(f"Error parsing TOML: {e}")
    except KeyError as e:
        print(f"Error accessing key in parsed TOML: {e}")
else:
    print(" (Skipping tomllib demo, requires Python 3.11+)")


# ==============================================================================
# Section 9: Advanced Concepts
# ==============================================================================

print("\n=== Section 9: Advanced Concepts ===")

# --- 9.1 Decorators ---
# Function that modifies another function. Uses @ syntax.
def timer_decorator(func):
    @functools.wraps(func) # Preserves metadata (name, docstring)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f" {func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@timer_decorator
def slow_func(delay=0.1):
    """Simulates work."""
    time.sleep(delay)
    return "Done"

print("\nDecorator Example:")
print(f"Result: {slow_func(0.05)}")

# --- 9.2 Generators ---
# Create iterators lazily using 'yield'. Memory efficient.
def count_up_to(n):
    i = 0
    while i < n:
        yield i # Pauses and returns value
        i += 1

print("\nGenerator Example:")
counter_gen = count_up_to(3)
print(f" Generator object: {counter_gen}")
print(f" Values: {list(counter_gen)}") # Exhausts the generator

# Generator expression (uses parentheses)
squares_gen = (x*x for x in range(4))
print(f" Generator expression values: {list(squares_gen)}")

# --- 9.3 Context Managers (`with` statement) ---
# Ensure setup/teardown (e.g., file closing, lock release).
# Implement __enter__ and __exit__ or use @contextmanager.

@contextmanager
def managed_resource(name):
    print(f"\n Context Manager: Acquiring '{name}'")
    try:
        yield f"Data from {name}" # Value available via 'as'
    finally:
        print(f" Context Manager: Releasing '{name}'")

with managed_resource("MyRes") as data:
    print(f" Inside 'with': working with '{data}'")
# Resource is automatically released here

# --- 9.4 Interfaces / Abstract Base Classes (ABCs) ---
# Define expected structure/methods for subclasses.
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self) -> float: pass

class Square(Shape):
    def __init__(self, side: float): self.side = side
    def area(self) -> float: return self.side ** 2

# shape = Shape() # TypeError: Can't instantiate abstract class
sq = Square(5)
print(f"\nABC Example: Square area = {sq.area()}")
print(f" Is Square a Shape? {issubclass(Square, Shape)}")


# ==============================================================================
# Section 10: Concurrency (Threading and Asyncio)
# ==============================================================================

print("\n=== Section 10: Concurrency (Threading and Asyncio) ===")

# --- 10.1 Threading ---
# Uses OS threads. Good for I/O-bound tasks.
# CPython GIL limits true CPU-bound parallelism.

# --- Conceptual Note on No-GIL Builds (Python 3.13+ Experimental) ---
# Python 3.13 introduced an *optional* experimental build mode (`--disable-gil`)
# that removes the Global Interpreter Lock (GIL).
# Purpose: Allow true multi-threaded parallelism for CPU-bound tasks in CPython.
# Status: Experimental. May impact single-thread performance or C-extension compatibility.
# Usage: Requires building Python from source with the flag. Not the default.
# Significance: A major potential change for CPU-bound concurrent Python code.
print("\n(Conceptual Note: Python 3.13+ offers experimental No-GIL builds)")


def io_task(name: str, delay: float):
    print(f" Thread {name}: Start, wait {delay}s")
    time.sleep(delay)
    print(f" Thread {name}: Finish")

print("\nThreading Example:")
t1 = threading.Thread(target=io_task, args=("T1", 0.2))
t2 = threading.Thread(target=io_task, args=("T2", 0.1))
start_th = time.perf_counter()
t1.start()
t2.start()
t1.join() # Wait for t1
t2.join() # Wait for t2
end_th = time.perf_counter()
print(f"Threading took {end_th - start_th:.4f}s") # Should be ~0.2s


# --- 10.2 Asyncio ---
# Single thread, event loop, cooperative multitasking via async/await.
# Excellent for high-concurrent I/O. Not for CPU-bound tasks.

async def async_io_task(name: str, delay: float, should_fail: bool = False):
    print(f" Async {name}: Start, await {delay}s")
    await asyncio.sleep(delay) # Yields control
    if should_fail:
        print(f" Async {name}: Raising error!")
        raise ValueError(f"Error in task {name}")
    print(f" Async {name}: Finish")
    return f"Result from {name}"

async def main_async_taskgroup():
    print("\nAsyncio Example with TaskGroup (Python 3.11+):")
    start_async = time.perf_counter()
    results = {}
    try:
        # TaskGroup ensures all tasks are awaited, handles errors together
        async with asyncio.TaskGroup() as tg:
            print(" Creating tasks in TaskGroup...")
            task1 = tg.create_task(async_io_task("A1", 0.2))
            task2 = tg.create_task(async_io_task("A2", 0.1, should_fail=True)) # This one will fail
            task3 = tg.create_task(async_io_task("A3", 0.15))
            task4 = tg.create_task(async_io_task("A4", 0.05, should_fail=True)) # This one will fail too
            # Tasks run concurrently here
            print(" Tasks created, awaiting TaskGroup completion...")
        # Code here runs only if NO exceptions occurred in the TaskGroup
        # This block will likely be skipped in this example due to failures
        print(" TaskGroup finished successfully (all tasks completed without error).")
        # Access results if needed (results are on the task objects)
        # results['A1'] = task1.result()
        # results['A3'] = task3.result()

    except* ValueError as eg: # Use except* to handle ExceptionGroup errors (Python 3.11+)
        print(f"\n Caught ExceptionGroup with {len(eg.exceptions)} ValueError(s):")
        for i, exc in enumerate(eg.exceptions):
            print(f"  - Error {i+1}: {exc}")

        # Safely collect results from successful tasks
        for task, name in [(task1, 'A1'), (task3, 'A3')]:
            try:
                if task.done() and not task.cancelled():
                    try:
                        # If task.exception() returns None, the task completed successfully
                        if task.exception() is None:
                            results[name] = task.result()
                    except asyncio.CancelledError:
                        # Task was cancelled
                        pass
            except Exception as e:
                print(f"  Error checking task {name}: {type(e).__name__}: {e}")

    except* Exception as eg: # Catch any other potential errors in exception groups
        print(f"\n Caught ExceptionGroup with {len(eg.exceptions)} other exception(s):")
        for i, exc in enumerate(eg.exceptions):
            print(f"  - Error {i+1}: {type(exc).__name__}: {exc}")

    finally:
        end_async = time.perf_counter()
        print(f"\nAsyncio (TaskGroup) section took {end_async - start_async:.4f}s")
        print(f" Results obtained from successful tasks: {results}")


# Run the asyncio main function
if __name__ == "__main__": # Ensure this runs only when script is executed directly
    if PYTHON_VERSION >= (3, 11):
        try:
            print("\n--- Running Asyncio TaskGroup Demo ---")
            asyncio.run(main_async_taskgroup())
            print("--- Finished Asyncio TaskGroup Demo ---")
        except RuntimeError as e:
            print(f"\n Note: Could not run asyncio TaskGroup example (possibly due to nested event loops or environment): {e}")
        except Exception as e:
             print(f"\n Unexpected error running asyncio TaskGroup: {type(e).__name__}: {e}")
    else:
        print("\n (Skipping asyncio.TaskGroup demo, requires Python 3.11+)")


# ==============================================================================
# Section 11: Pydantic (Optional External Library)
# ==============================================================================

print("\n=== Section 11: Pydantic (Optional External Library) ===")

if PYDANTIC_INSTALLED:
    print("\nPydantic Example (requires 'pip install pydantic'):")
    try:
        # Define a data model using Pydantic BaseModel
        class Item(BaseModel):
            id: int
            name: str = Field(..., min_length=3) # Required, min length 3
            price: float | None = None # Optional float (uses | union)
            tags: list[str] = [] # List of strings, default empty

        # Valid data
        item_data_valid = {"id": 1, "name": "Gadget", "price": 99.90, "tags": ["tech", "new"]}
        item_valid = Item(**item_data_valid)
        print(" Valid Pydantic model created:")
        print(f"  {item_valid}")
        print(f"  JSON: {item_valid.model_dump_json(indent=2)}")

        # Invalid data
        item_data_invalid = {"id": "abc", "name": "X"} # id not int, name too short
        print("\n Attempting to parse invalid data:")
        try:
            Item(**item_data_invalid)
        except ValidationError as e:
            print(" Pydantic validation failed (expected):")
            # Detailed JSON representation of errors
            print(e.json(indent=2))

    except Exception as e:
         print(f"An error occurred during the Pydantic example: {type(e).__name__}: {e}")

else:
    print("\n (Pydantic library not installed. Skipping Pydantic examples.)")
    print(" (Install using: pip install pydantic)")


# --- Pydantic-AI (Conceptual Overview - Remains unchanged) ---
# Pydantic-AI bridges LLMs and structured data validation (Pydantic models).
# Key Purpose: Reliably extract structured data from unstructured text generated by LLMs.
# How it works: Define Pydantic model -> Prompt LLM -> Feed text & model to Pydantic-AI ->
#               Pydantic-AI uses LLM/parsing for extraction & validation -> Get validated Pydantic object.
# Use Cases: Info extraction (emails, docs), function calling from natural language, ensuring LLM output format.
# Note: Requires installing `pydantic-ai` and configuring an LLM client (e.g., OpenAI, Gemini) with API keys.
# See previous conceptual code snippet explanation if needed.
print("\nConceptual Pydantic-AI description remains relevant.")
print(" Using it requires 'pydantic-ai' install and LLM client setup.")


# ==============================================================================
# Section 12: Conclusion
# ==============================================================================

print("\n=== Section 12: Conclusion ===")
print("You have reached the end of this updated comprehensive Python learning script.")
print(f"Covered concepts include features up to ~Python {PYTHON_VERSION.major}.{PYTHON_VERSION.minor}.")
print("Key additions/enhancements demonstrated or discussed:")
print("- Control Flow: Structural Pattern Matching (match/case) (3.10+)")
print("- Error Handling: Exception Groups (except*) (3.11+)")
print("- Asyncio: TaskGroup for better task management (3.11+)")
print("- Type Hinting: | Union syntax (3.10+), typing.Self (3.11+), PEP 695 Generics (3.12+)")
print("- File I/O: Built-in TOML parsing (tomllib) (3.11+)")
print("- Strings: More flexible f-string expressions (3.12+)")
print("- Concurrency: Conceptual awareness of experimental No-GIL builds (3.13+)")
print("\nOriginal coverage included:")
print("- Basics, Data Structures, Functions, OOP, Modules, Files, Decorators, Generators, Context Managers, Threading, Pydantic concept.")
print("\nKeep practicing and exploring the vast Python ecosystem!")
print("Consider libraries like NumPy, Pandas, Flask, Django, Requests, Matplotlib, etc.")
print("Good luck on your Python journey!")


# ==============================================================================
# Main Execution Block
# ==============================================================================

if __name__ == "__main__":
    print("\n--- Script Execution Finished ---")
    # Any code here runs only when the script is executed directly,
    # not when imported as a module.
    # The asyncio demo needed to be here to run correctly using asyncio.run().

# End of script