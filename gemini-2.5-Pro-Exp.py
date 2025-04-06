# -*- coding: utf-8 -*-
"""
Comprehensive Python Learning Script

This script covers Python basics, intermediate concepts, and advanced features.
It's designed as a single-file learning resource with extensive comments.

Run this file using: python comprehensive_python_script.py
"""

# ==============================================================================
# Section 1: Python Basics
# ==============================================================================

print("=== Section 1: Python Basics ===")

# --- 1.1 Comments ---
# This is a single-line comment. Comments start with '#' and are ignored by the interpreter.
# They are used to explain the code.

"""
This is a multi-line comment (or docstring).
It's often used at the beginning of files, functions, or classes
to provide a detailed description.
"""

# --- 1.2 Variables and Data Types ---
# Variables are used to store data. Python is dynamically typed,
# meaning you don't need to declare the type of a variable explicitly.

# Integer (whole number)
age = 30
print(f"Variable 'age': {age} (type: {type(age)})")

# Float (number with a decimal point)
price = 19.99
print(f"Variable 'price': {price} (type: {type(price)})")

# String (sequence of characters)
name = "Alice"
greeting = 'Hello, World!' # Single or double quotes work
multiline_string = """This is a
string that spans
multiple lines."""
print(f"Variable 'name': {name} (type: {type(name)})")
print(f"Variable 'greeting': {greeting}")
print(f"Variable 'multiline_string':\n{multiline_string}")

# Boolean (True or False) - Note the capitalization
is_active = True
has_permission = False
print(f"Variable 'is_active': {is_active} (type: {type(is_active)})")

# NoneType (represents the absence of a value)
result = None
print(f"Variable 'result': {result} (type: {type(result)})")

# --- 1.3 Basic Operators ---

# Arithmetic Operators
a = 10
b = 3
print(f"\nArithmetic Operators (a={a}, b={b}):")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")             # Float division
print(f"Floor Division (a // b): {a // b}")       # Integer division (discards remainder)
print(f"Modulus (a % b): {a % b}")               # Remainder of division
print(f"Exponentiation (a ** b): {a ** b}")       # a to the power of b

# Comparison Operators (return Boolean values)
x = 5
y = 10
print(f"\nComparison Operators (x={x}, y={y}):")
print(f"Equal (x == y): {x == y}")
print(f"Not Equal (x != y): {x != y}")
print(f"Greater Than (x > y): {x > y}")
print(f"Less Than (x < y): {x < y}")
print(f"Greater or Equal (x >= y): {x >= y}")
print(f"Less or Equal (x <= y): {x <= y}")

# Logical Operators
p = True
q = False
print(f"\nLogical Operators (p={p}, q={q}):")
print(f"AND (p and q): {p and q}") # True if both are True
print(f"OR (p or q): {p or q}")   # True if at least one is True
print(f"NOT (not p): {not p}")     # Inverts the boolean value

# Assignment Operators
count = 0
count += 1  # Equivalent to count = count + 1
print(f"\nAssignment Operator Example (count): {count}")
# Other examples: -=, *=, /=, //=, %=, **=

# --- 1.4 Input and Output ---
# print() is used for output (we've been using it!)
# input() is used to get input from the user (returns a string)
# user_name = input("Enter your name: ") # Uncomment to run
# print(f"Hello, {user_name}!")         # Uncomment to run

# You often need to convert input type
# user_age_str = input("Enter your age: ") # Uncomment to run
# try:                                      # Uncomment to run
#     user_age_int = int(user_age_str)      # Convert string to integer
#     print(f"Next year, you will be {user_age_int + 1}.")
# except ValueError:
#     print("Invalid age entered. Please enter a number.")

# --- 1.5 String Formatting ---
# Different ways to format strings:

# f-strings (Formatted String Literals) - Recommended (Python 3.6+)
item = "Laptop"
cost = 1200.50
print(f"\nString Formatting (f-string): The {item} costs ${cost:.2f}.") # .2f formats float to 2 decimal places

# .format() method
print("String Formatting (.format()): The {} costs ${:.2f}.".format(item, cost))
print("String Formatting (.format() with indices): The {0} costs ${1:.2f}. Item: {0}".format(item, cost))
print("String Formatting (.format() with keywords): The {i} costs ${c:.2f}.".format(i=item, c=cost))

# % operator (Older style, less common now)
print("String Formatting (%% operator): The %s costs $%.2f." % (item, cost))

# ==============================================================================
# Section 2: Control Flow
# ==============================================================================

print("\n=== Section 2: Control Flow ===")

# --- 2.1 Conditional Statements (if, elif, else) ---
# Execute code based on conditions.

score = 75
print(f"\nConditional Statements (score={score}):")
if score >= 90:
    print("Grade: A")
elif score >= 80: # 'elif' is short for 'else if'
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")

# Conditions can be complex
temperature = 25
is_raining = False

if temperature > 20 and not is_raining:
    print("It's a pleasant day!")
elif is_raining:
    print("Bring an umbrella.")
else:
    print("It might be cold.")

# --- 2.2 Loops ---

# For Loops: Iterate over a sequence (like lists, tuples, strings, ranges)

# Iterating over a range
print("\nFor Loop (range):")
for i in range(5): # range(5) generates numbers 0, 1, 2, 3, 4
    print(f"Iteration {i}")

# Iterating over a list
print("\nFor Loop (list):")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Iterating over a string
print("\nFor Loop (string):")
for char in "Python":
    print(f"Character: {char}")

# Iterating with index using enumerate
print("\nFor Loop (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# While Loops: Execute code as long as a condition is True

print("\nWhile Loop:")
attempts = 3
while attempts > 0:
    print(f"Attempts remaining: {attempts}")
    attempts -= 1 # Decrement attempts
    # Simulating an action that might succeed
    # if some_condition:
    #     break # Exit the loop early
else:
    # The 'else' block executes if the loop completes WITHOUT hitting 'break'
    print("While loop finished normally (no 'break').")


# Loop Control Statements: break and continue
print("\nLoop Control (break and continue):")
for num in range(10):
    if num == 3:
        print("Skipping 3 (continue)")
        continue # Skip the rest of this iteration and go to the next
    if num == 7:
        print("Stopping at 7 (break)")
        break    # Exit the loop entirely
    print(f"Processing number {num}")

# ==============================================================================
# Section 3: Data Structures
# ==============================================================================

print("\n=== Section 3: Data Structures ===")

# Python's built-in data structures are very powerful.

# --- 3.1 Lists ---
# Ordered, mutable (changeable), allow duplicate elements. Defined with [].
my_list = [1, "hello", 3.14, True, 1]
print(f"\nList: {my_list}")

# Accessing elements (zero-indexed)
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")

# Slicing [start:stop:step] (stop index is exclusive)
print(f"Slice [1:3]: {my_list[1:3]}") # Elements at index 1 and 2
print(f"Slice [:3]: {my_list[:3]}")   # From start up to index 3
print(f"Slice [2:]: {my_list[2:]}")   # From index 2 to the end
print(f"Slice [::2]: {my_list[::2]}") # Every second element

# Modifying lists
my_list[1] = "world" # Change element at index 1
my_list.append("new") # Add element to the end
my_list.insert(2, False) # Insert element at a specific index
print(f"Modified list: {my_list}")

# Removing elements
removed_item = my_list.pop() # Remove and return the last item
print(f"List after pop(): {my_list}, Removed: {removed_item}")
my_list.pop(2) # Remove item at index 2
print(f"List after pop(2): {my_list}")
my_list.remove(1) # Remove the *first* occurrence of the value 1
print(f"List after remove(1): {my_list}")

# Other useful methods: sort(), reverse(), count(), index(), len()
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort() # Sorts in-place
print(f"Sorted numbers: {numbers}")
print(f"Length of list: {len(numbers)}")
print(f"Count of '1': {numbers.count(1)}")

# List Comprehensions: Concise way to create lists
squares = [x**2 for x in range(10)] # [0, 1, 4, ..., 81]
print(f"List Comprehension (squares): {squares}")
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"List Comprehension (even squares): {even_squares}")

# --- 3.2 Tuples ---
# Ordered, immutable (unchangeable), allow duplicate elements. Defined with ().
my_tuple = (1, "hello", 3.14, True, 1)
print(f"\nTuple: {my_tuple}")

# Accessing and slicing works like lists
print(f"First element: {my_tuple[0]}")
print(f"Slice [1:3]: {my_tuple[1:3]}")

# Tuples are immutable - these lines would cause errors:
# my_tuple[0] = 5 # TypeError: 'tuple' object does not support item assignment
# my_tuple.append("world") # AttributeError: 'tuple' object has no attribute 'append'

# Use cases: When you need a constant sequence, dictionary keys (must be immutable).
# Can be created without parentheses (tuple packing)
point = 3, 4 # Creates a tuple (3, 4)
print(f"Packed tuple 'point': {point}")
# Tuple unpacking
x_coord, y_coord = point
print(f"Unpacked coordinates: x={x_coord}, y={y_coord}")

# --- 3.3 Dictionaries ---
# Unordered (Python < 3.7) / Ordered (Python >= 3.7), mutable, store key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, tuples). Defined with {}.
student = {
    "name": "Bob",
    "age": 25,
    "courses": ["Math", "Physics"],
    "is_graduated": False
}
print(f"\nDictionary: {student}")

# Accessing values using keys
print(f"Student name: {student['name']}")
# print(f"Student grade: {student['grade']}") # KeyError if key doesn't exist

# Safer access using .get() (returns None or a default value if key not found)
print(f"Student age: {student.get('age')}")
print(f"Student grade (using get): {student.get('grade')}") # Output: None
print(f"Student grade (using get with default): {student.get('grade', 'N/A')}") # Output: N/A

# Modifying dictionaries
student['age'] = 26 # Update existing value
student['city'] = "New York" # Add new key-value pair
print(f"Modified dictionary: {student}")

# Removing items
removed_value = student.pop('is_graduated') # Remove key and return its value
print(f"Dict after pop('is_graduated'): {student}, Removed: {removed_value}")
# del student['city'] # Another way to remove by key
# print(f"Dict after del 'city': {student}")

# Getting keys, values, and items (key-value pairs)
print(f"Keys: {student.keys()}")       # Returns a view object
print(f"Values: {student.values()}")   # Returns a view object
print(f"Items: {student.items()}")     # Returns a view object of (key, value) tuples

# Iterating over dictionaries
print("Iterating over keys:")
for key in student: # Default iteration is over keys
    print(f"  Key: {key}, Value: {student[key]}")

print("Iterating over items:")
for key, value in student.items():
    print(f"  Key: {key}, Value: {value}")

# Dictionary Comprehensions
squared_dict = {x: x**2 for x in range(6)} # {0: 0, 1: 1, 2: 4, ..., 5: 25}
print(f"Dictionary Comprehension: {squared_dict}")

# --- 3.4 Sets ---
# Unordered, mutable, do NOT allow duplicate elements. Defined with {} or set().
# Note: {} creates an empty dictionary, use set() for an empty set.
my_set = {1, 2, 3, "hello", 3, 2} # Duplicates are automatically removed
print(f"\nSet: {my_set}")
empty_set = set()
print(f"Empty set: {empty_set}")

# Adding and removing elements
my_set.add(4)
my_set.add("world")
print(f"Set after adding: {my_set}")
my_set.remove(2) # Raises KeyError if element not found
print(f"Set after remove(2): {my_set}")
my_set.discard("nonexistent") # Removes element if present, no error if not
print(f"Set after discard('nonexistent'): {my_set}")
popped_element = my_set.pop() # Removes and returns an *arbitrary* element
print(f"Set after pop(): {my_set}, Popped: {popped_element}")

# Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

print(f"Union (A | B): {set_a | set_b}")           # Elements in either set
print(f"Intersection (A & B): {set_a & set_b}")     # Elements in both sets
print(f"Difference (A - B): {set_a - set_b}")       # Elements in A but not in B
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}") # Elements in either A or B, but not both

# Use cases: Membership testing (very fast), removing duplicates from a list.
list_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
unique_elements = list(set(list_with_duplicates))
print(f"List with duplicates: {list_with_duplicates}")
print(f"Unique elements (from set): {unique_elements}")
print(f"Is 3 in set_a? {3 in set_a}") # Fast membership check

# ==============================================================================
# Section 4: Functions
# ==============================================================================

print("\n=== Section 4: Functions ===")

# Functions are blocks of reusable code. They help organize code and make it modular.

# --- 4.1 Defining and Calling Functions ---
# Use the 'def' keyword.

def greet():
    """This is a docstring. It explains what the function does."""
    print("Hello from the greet function!")

greet() # Call the function

# Functions with parameters (inputs)
def greet_person(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")

greet_person("Charlie") # 'Charlie' is the argument passed to the 'name' parameter

# Functions with return values (outputs)
def add_numbers(x, y):
    """Adds two numbers and returns the result."""
    return x + y

sum_result = add_numbers(5, 7)
print(f"Result of add_numbers(5, 7): {sum_result}")

# --- 4.2 Function Arguments ---

# Positional arguments: Order matters
print(f"add_numbers(10, 2): {add_numbers(10, 2)}")

# Keyword arguments: Order doesn't matter if names are specified
print(f"add_numbers(y=2, x=10): {add_numbers(y=2, x=10)}")

# Default parameter values
def power(base, exponent=2): # exponent defaults to 2 if not provided
    """Calculates base to the power of exponent."""
    return base ** exponent

print(f"power(3): {power(3)}")       # Uses default exponent 2 -> 9
print(f"power(3, 3): {power(3, 3)}") # Overrides default -> 27

# Variable number of positional arguments (*args)
# Collects extra positional arguments into a tuple
def sum_all(*numbers):
    """Sums all numbers passed as arguments."""
    print(f"Arguments received in *numbers: {numbers}")
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40, 50): {sum_all(10, 20, 30, 40, 50)}")

# Variable number of keyword arguments (**kwargs)
# Collects extra keyword arguments into a dictionary
def print_info(**info):
    """Prints key-value information."""
    print(f"Arguments received in **info: {info}")
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\nprint_info(name='David', age=40, city='London'):")
print_info(name="David", age=40, city="London")


# Combining argument types (order matters in definition: standard, *args, **kwargs)
def combined_args(required_arg, default_arg="default", *args, **kwargs):
    print(f"\nCombined Arguments Example:")
    print(f"  Required: {required_arg}")
    print(f"  Default: {default_arg}")
    print(f"  *args: {args}")
    print(f"  **kwargs: {kwargs}")

combined_args(100)
combined_args(100, "custom_default", 200, 300, key1="value1", key2="value2")
combined_args(required_arg=50, extra_key="extra_val", another_arg=99) # 'another_arg' goes into *args if no default provided


# --- 4.3 Scope ---
# Where variables are accessible.

global_var = "I am global"

def scope_test():
    local_var = "I am local"
    print(f"Inside function: {local_var}")
    print(f"Inside function accessing global: {global_var}")
    # Modifying global variable (need 'global' keyword)
    # global global_var
    # global_var = "Modified global"

scope_test()
print(f"Outside function: {global_var}")
# print(f"Outside function accessing local: {local_var}") # NameError: local_var is not defined outside

# --- 4.4 Lambda Functions (Anonymous Functions) ---
# Small, inline functions defined with 'lambda'. Syntax: lambda arguments: expression

# Equivalent to: def multiply(x, y): return x * y
multiply = lambda x, y: x * y
print(f"\nLambda function multiply(5, 4): {multiply(5, 4)}")

# Often used with functions like map(), filter(), sorted()
numbers = [1, 2, 3, 4, 5, 6]
# map applies a function to all items in an input list
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Map with lambda (squared): {squared_numbers}")

# filter creates a list of elements for which a function returns true
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter with lambda (evens): {even_numbers}")

# sorted can use a lambda for the key
points = [(1, 5), (3, 2), (2, 8)]
points_sorted_by_y = sorted(points, key=lambda p: p[1])
print(f"Sorted with lambda key (by y-coord): {points_sorted_by_y}")


# --- 4.5 Type Hinting (PEP 484) ---
# Allows specifying expected types for variables, function args, and return values.
# Does NOT enforce types at runtime (Python remains dynamically typed),
# but helps with code readability and static analysis tools (like MyPy).

import typing # Import common types

def calculate_area(length: float, width: float) -> float:
    """Calculates area with type hints."""
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numeric")
    return length * width

area: float = calculate_area(10.5, 5.2)
print(f"\nType Hinting Example: Area = {area}")

# Example with more complex types
def process_names(names: typing.List[str]) -> typing.Optional[str]:
    """Processes a list of names, returns the longest or None if empty."""
    if not names:
        return None
    return max(names, key=len)

name_list: typing.List[str] = ["Alice", "Bob", "Charlie"]
longest_name: typing.Optional[str] = process_names(name_list)
print(f"Longest name: {longest_name}")


# ==============================================================================
# Section 5: Object-Oriented Programming (OOP)
# ==============================================================================

print("\n=== Section 5: Object-Oriented Programming (OOP) ===")

# OOP allows modeling real-world things as objects. Objects have attributes (data)
# and methods (functions). Classes are blueprints for creating objects.

# --- 5.1 Classes and Objects ---

class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Initializer / Constructor method (called when an object is created)
    # 'self' refers to the instance of the class being created/operated on
    def __init__(self, name: str, breed: str, age: int):
        # Instance attributes (specific to each object)
        self.name = name
        self.breed = breed
        self.age = age
        self._is_hungry = True # Convention: Single underscore suggests "internal use"

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

    # Another instance method
    def describe(self) -> str:
        return f"{self.name} is a {self.age}-year-old {self.breed}."

    # Method modifying instance state
    def feed(self):
        if self._is_hungry:
            print(f"Feeding {self.name}...")
            self._is_hungry = False
        else:
            print(f"{self.name} is not hungry right now.")

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Lucy", "Poodle", 5)

# Accessing attributes and calling methods
print(f"\n{dog1.describe()}")
dog1.bark()
print(f"Species of dog1: {dog1.species}") # Accessing class attribute
print(f"Species of dog2: {dog2.species}")
# Can also access via class: Dog.species

dog1.feed()
dog1.feed() # Try feeding again

# --- 5.2 Inheritance ---
# Allows creating a new class (child/subclass) that inherits attributes and methods
# from an existing class (parent/superclass). Promotes code reuse.

# Parent class
class Animal:
    def __init__(self, name: str):
        self.name = name
        print(f"Animal '{self.name}' created.")

    def speak(self):
        # Abstract concept - specific animals make different sounds
        raise NotImplementedError("Subclass must implement this method")

    def eat(self):
        print(f"{self.name} is eating.")

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name: str, color: str):
        # Call the parent class's __init__ method
        super().__init__(name) # Recommended way
        # Animal.__init__(self, name) # Older way, works but super() is preferred
        self.color = color
        print(f"Cat '{self.name}' (color: {self.color}) created.")

    # Override the speak method from the parent
    def speak(self):
        print(f"{self.name} says Meow!")

    # Add a new method specific to Cat
    def purr(self):
        print(f"{self.name} starts purring...")

# Create instances
generic_animal = Animal("Creature") # Raises NotImplementedError if speak() is called
# generic_animal.speak() # Uncommenting this line will raise the error

cat1 = Cat("Whiskers", "Gray")
cat1.eat()    # Method inherited from Animal
cat1.speak()  # Method overridden in Cat
cat1.purr()   # Method specific to Cat

# --- 5.3 Polymorphism ---
# The ability of different objects to respond to the same method call in different ways.
# Often achieved through inheritance (method overriding) or "duck typing".

# Duck Typing: "If it walks like a duck and quacks like a duck, then it must be a duck."
# Python doesn't strictly require inheritance for polymorphism if objects have methods
# with the same name.

class Duck:
    def speak(self):
        print("Quack!")
    def swim(self):
        print("Duck swimming")

class Person:
    def speak(self):
        print("Hello!")
    def walk(self):
        print("Person walking")

def make_it_speak(entity):
    # This function works as long as the 'entity' object has a 'speak' method
    entity.speak()

print("\nPolymorphism (Duck Typing):")
duck = Duck()
person = Person()
cat = Cat("Fluffy", "White") # Our Cat class also has speak()

make_it_speak(duck)   # Calls Duck.speak()
make_it_speak(person) # Calls Person.speak()
make_it_speak(cat)    # Calls Cat.speak()


# --- 5.4 Encapsulation ---
# Bundling data (attributes) and methods that operate on the data within a single unit (class).
# Often involves controlling access to internal state (data hiding).
# Python uses conventions rather than strict enforcement like private/public keywords.

# - Public: Accessible from anywhere (e.g., `dog1.name`)
# - Protected (Convention): Prefix with single underscore (`_`). Signals "internal use",
#   but still accessible. (e.g., `dog1._is_hungry`)
# - Private (Name Mangling): Prefix with double underscore (`__`). Python internally
#   renames it to `_ClassName__attributeName` to avoid accidental overriding in subclasses.
#   Still accessible if you know the mangled name, but strongly discouraged.

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner # Public
        self._balance = initial_balance # Protected convention
        self.__transaction_log = [] # "Private" via name mangling

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            self.__log_transaction(f"Deposit: +{amount}")
            print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            self.__log_transaction(f"Withdrawal: -{amount}")
            print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")

    # Method intended for internal use (convention)
    def _check_balance(self):
        return self._balance

    # "Private" method (name mangled)
    def __log_transaction(self, message: str):
        # In a real app, add timestamp, etc.
        self.__transaction_log.append(message)
        # print(f"Logging: {message}") # For demonstration

    def get_balance(self) -> float:
        # Provide controlled access to the balance
        return self._balance

    def get_transaction_history(self) -> list:
        # Provide controlled access to the log
        return self.__transaction_log[:] # Return a copy

    # Special Methods (Dunder methods like __init__, __str__, __repr__)
    def __str__(self) -> str:
        # User-friendly string representation
        return f"BankAccount(Owner: {self.owner}, Balance: ${self._balance:.2f})"

    def __repr__(self) -> str:
        # Developer-friendly, unambiguous string representation
        return f"BankAccount(owner='{self.owner}', initial_balance={self._balance})"

print("\nEncapsulation Example:")
account = BankAccount("Eve", 1000.0)
print(account) # Calls __str__

account.deposit(500.50)
account.withdraw(200)
account.withdraw(2000) # Insufficient funds
account.deposit(-50)   # Invalid amount

# Accessing attributes
print(f"Account Owner: {account.owner}")
# Accessing protected attribute (possible, but violates convention)
# print(f"Protected Balance (direct access): {account._balance}")
print(f"Balance via method: {account.get_balance()}")

# Accessing "private" attribute using mangled name (discouraged)
# print(f"Private Log (mangled): {account._BankAccount__transaction_log}")
print(f"Transaction History via method: {account.get_transaction_history()}")

print(f"Developer representation: {repr(account)}") # Calls __repr__


# --- 5.5 Properties ---
# Provide controlled access to attributes, making methods look like attributes.
# Useful for validation or computed properties.

class Temperature:
    def __init__(self, celsius: float):
        # Use the setter method during initialization to apply validation
        self.celsius = celsius # This calls the @celsius.setter method

    @property # Getter method
    def celsius(self) -> float:
        print("Getting Celsius value...")
        return self._celsius # Note the use of a "private" attribute

    @celsius.setter # Setter method
    def celsius(self, value: float):
        print(f"Setting Celsius value to {value}...")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value # Store the actual value

    @property # Another property (read-only, computed)
    def fahrenheit(self) -> float:
        print("Calculating Fahrenheit...")
        return (self._celsius * 9/5) + 32

    # We could add a fahrenheit setter if needed, to allow setting via Fahrenheit
    # @fahrenheit.setter
    # def fahrenheit(self, value: float):
    #     print(f"Setting temperature via Fahrenheit ({value} F)...")
    #     self.celsius = (value - 32) * 5/9 # Convert and use Celsius setter for validation

print("\nProperties Example:")
temp = Temperature(25) # Calls setter
print(f"Temperature in Celsius: {temp.celsius}") # Calls getter
print(f"Temperature in Fahrenheit: {temp.fahrenheit}") # Calls fahrenheit getter

temp.celsius = 30 # Calls setter
print(f"New Celsius: {temp.celsius}")
print(f"New Fahrenheit: {temp.fahrenheit}")

# temp.celsius = -300 # Uncommenting this will raise ValueError due to setter validation


# ==============================================================================
# Section 6: Modules and Packages
# ==============================================================================

print("\n=== Section 6: Modules and Packages ===")

# Modules: Individual Python files (.py) containing code (functions, classes, variables).
# Packages: Collections of modules organized in directories. Must contain an `__init__.py` file
# (can be empty) to be recognized as a package.

# --- 6.1 Importing Modules ---
import math # Import the entire 'math' module
import os as operating_system # Import 'os' and rename it using 'as'
from random import choice, randint # Import specific functions from 'random'
# from collections import * # Import everything (generally discouraged due to namespace pollution)

print(f"Value of Pi from math module: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

print(f"Current working directory (using alias): {operating_system.getcwd()}")

print(f"Random integer between 1 and 10: {randint(1, 10)}")
my_options = ["A", "B", "C", "D"]
print(f"Random choice from {my_options}: {choice(my_options)}")

# --- 6.2 Creating Your Own Modules ---
# If you save the following code as `my_module.py` in the same directory:
# ```python
# # my_module.py
# print("my_module is being imported!")
# MY_CONSTANT = 42
# def my_function(x):
#     return x * 2
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"Hello from MyClass, {self.name}!")
# ```
# You could then import and use it in this script like this (if my_module.py exists):
# try:
#     import my_module
#     print(f"Constant from my_module: {my_module.MY_CONSTANT}")
#     print(f"Result of my_module.my_function(5): {my_module.my_function(5)}")
#     my_obj = my_module.MyClass("Test")
#     my_obj.greet()
# except ImportError:
#     print("\nNote: 'my_module.py' not found. Skipping custom module demonstration.")

# The `if __name__ == "__main__":` block
# Code inside this block only runs when the script is executed directly,
# not when it's imported as a module into another script.
# This is useful for testing or running code specific to the script itself.

def main_function():
    print("This function is part of the main script.")

if __name__ == "__main__":
    print("\nThis script is being run directly.")
    main_function()
    # Often, the main execution logic of a script goes here.
else:
    # This would execute if this script were imported by another module
    print(f"\nThis script ('{__name__}') is being imported.")


# ==============================================================================
# Section 7: Error Handling (Exceptions)
# ==============================================================================

print("\n=== Section 7: Error Handling (Exceptions) ===")

# Errors detected during execution are called exceptions.
# Use try...except blocks to handle potential errors gracefully.

# --- 7.1 Basic Try...Except ---
try:
    # Code that might raise an error
    numerator = 10
    denominator = 0
    result = numerator / denominator # Raises ZeroDivisionError
    print(f"Result: {result}") # This line won't execute if error occurs
except ZeroDivisionError:
    # Code to run if a ZeroDivisionError occurs
    print("Error: Cannot divide by zero!")
except TypeError as e:
    # Handle a different specific error (e.g., '10' / 'a')
    print(f"Error: Type mismatch - {e}")
except Exception as e:
    # Catch any other exception (use sparingly, better to catch specific errors)
    # 'e' holds the exception object
    print(f"An unexpected error occurred: {e} (Type: {type(e).__name__})")
else:
    # Code to run if NO exception occurred in the 'try' block
    print("Division successful (this runs only if no error).")
finally:
    # Code that ALWAYS runs, whether an exception occurred or not
    # Useful for cleanup actions (e.g., closing files)
    print("This 'finally' block always executes.")

print("Program continues after handling the error.")

# --- 7.2 Raising Exceptions ---
# You can trigger exceptions intentionally using the 'raise' keyword.

def check_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise PermissionError("User must be 18 or older.")
    else:
        print("Age is valid.")

try:
    check_age(25)
    check_age(15) # Raises PermissionError
    # check_age(-5) # Would raise ValueError
except ValueError as ve:
    print(f"Caught ValueError: {ve}")
except PermissionError as pe:
    print(f"Caught PermissionError: {pe}")

# --- 7.3 Custom Exceptions ---
# You can define your own exception classes by inheriting from Exception.

class MyCustomError(Exception):
    """A custom exception for specific application errors."""
    def __init__(self, message="A custom error occurred", error_code=None):
        super().__init__(message)
        self.error_code = error_code

# try:
#     # Simulate a condition where your custom error should be raised
#     config_status = "invalid"
#     if config_status == "invalid":
#         raise MyCustomError("Configuration is invalid.", error_code=101)
# except MyCustomError as mce:
#     print(f"Caught MyCustomError: {mce} (Code: {mce.error_code})")


# ==============================================================================
# Section 8: File I/O (Input/Output)
# ==============================================================================

print("\n=== Section 8: File I/O ===")

# Interacting with files on the filesystem.

# --- 8.1 Reading Files ---
# Use the `with open(...)` context manager - ensures the file is automatically closed.

file_path = "example.txt" # Assumes this file is in the same directory

# First, let's write something to the file to make sure it exists
try:
    with open(file_path, 'w') as f: # 'w' mode for writing (overwrites if exists)
        f.write("Hello, Python Files!\n")
        f.write("This is the second line.\n")
        f.write("And a third line for reading.\n")
    print(f"Successfully wrote to '{file_path}'")
except IOError as e:
    print(f"Error writing to file '{file_path}': {e}")

# Now, read the file
try:
    # 'r' mode for reading (default)
    with open(file_path, 'r') as f:
        # Read the entire file content into a string
        content = f.read()
        print(f"\nReading entire file ('{file_path}'):\n--- START ---\n{content}--- END ---")

    # Read file line by line
    print(f"\nReading file line by line ('{file_path}'):")
    with open(file_path, 'r') as f:
        for line in f: # Iterating over the file object reads lines
            print(f"  Line: {line.strip()}") # .strip() removes leading/trailing whitespace (like \n)

    # Read all lines into a list
    with open(file_path, 'r') as f:
        lines = f.readlines()
        print(f"\nReading all lines into a list: {lines}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except IOError as e:
    print(f"Error reading file '{file_path}': {e}")

# --- 8.2 Writing and Appending to Files ---

# 'w' mode: Write (overwrites existing file or creates new)
try:
    with open("output_write.txt", 'w') as f:
        f.write("This will overwrite the file.\n")
        f.writelines(["Line 2 added with writelines.\n", "Line 3.\n"])
    print("Successfully wrote to 'output_write.txt'")
except IOError as e:
    print(f"Error writing to file: {e}")

# 'a' mode: Append (adds to the end of the file or creates new)
try:
    with open("output_append.txt", 'a') as f:
        f.write("Appending this line.\n")
    print("Successfully appended to 'output_append.txt'")
except IOError as e:
    print(f"Error appending to file: {e}")


# --- 8.3 Working with Binary Files ---
# Use 'rb' (read binary) or 'wb' (write binary) modes.

# Example: Writing bytes
try:
    with open("binary_data.bin", "wb") as f:
        byte_data = b'\x48\x65\x6C\x6C\x6F' # Represents "Hello" in ASCII bytes
        f.write(byte_data)
    print("Successfully wrote binary data.")

    # Reading bytes
    with open("binary_data.bin", "rb") as f:
        read_bytes = f.read()
        print(f"Read binary data: {read_bytes}")
        print(f"Decoded binary data: {read_bytes.decode('utf-8')}") # Decode assuming UTF-8/ASCII
except IOError as e:
    print(f"Error with binary file: {e}")

# Clean up the created files (optional)
import os
try:
    os.remove(file_path)
    os.remove("output_write.txt")
    os.remove("output_append.txt")
    os.remove("binary_data.bin")
    print("\nCleaned up example files.")
except OSError as e:
    print(f"Error cleaning up files: {e}")


# ==============================================================================
# Section 9: Advanced Concepts
# ==============================================================================

print("\n=== Section 9: Advanced Concepts ===")

# --- 9.1 Decorators ---
# A decorator is a function that takes another function as input, adds some
# functionality to it (without modifying the original function's code),
# and returns the modified function. Uses '@' syntax sugar.

import time
import functools # For functools.wraps

def timer_decorator(func):
    """Decorator that prints the execution time of a function."""
    @functools.wraps(func) # Preserves original function's metadata (name, docstring)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs) # Call the original function
        end_time = time.perf_counter()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds.")
        return result
    return wrapper

@timer_decorator # Apply the decorator to this function
def slow_function(delay: float):
    """A function that simulates work by sleeping."""
    print(f"Running slow_function with delay {delay}...")
    time.sleep(delay)
    print("slow_function finished.")
    return "Done"

print("\nDecorator Example:")
result = slow_function(0.5) # This will now print execution time
print(f"Result of slow_function: {result}")
print(f"Original function name: {slow_function.__name__}") # Preserved by @wraps
print(f"Original docstring: {slow_function.__doc__}")   # Preserved by @wraps

# Decorators can also take arguments
def repeat(num_times):
    """Decorator factory: Creates a decorator that runs a function multiple times."""
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            # Could return last value, or a list of values, etc.
            return value # Return last value for simplicity
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=3)
def say_hello(name):
    print(f"Hello, {name}!")

print("\nDecorator with Arguments Example:")
say_hello("World")


# --- 9.2 Generators ---
# Generators are a simple way to create iterators. They use the 'yield' keyword
# to produce a sequence of values lazily (one at a time), which is memory-efficient
# for large sequences.

def count_up_to(n):
    """Generator function that yields numbers from 0 up to n-1."""
    i = 0
    while i < n:
        print(f"Generator yielding {i}")
        yield i # Pauses execution here, returns value, resumes on next call
        i += 1
    print("Generator finished.")

print("\nGenerator Function Example:")
counter_gen = count_up_to(5) # Creates a generator object, code doesn't run yet
print(f"Generator object: {counter_gen}")

# Iterate through the generator
print(f"First value: {next(counter_gen)}") # Runs until first yield
print(f"Second value: {next(counter_gen)}") # Resumes and runs until next yield

# Can also use in a for loop
print("Using generator in a for loop:")
for number in counter_gen: # Continues from where it left off
    print(f"  For loop got: {number}")

# Trying to get next value after exhaustion raises StopIteration
# try:
#     next(counter_gen)
# except StopIteration:
#     print("Generator is exhausted (StopIteration).")

# Generator Expressions: Similar syntax to list comprehensions, but create generators.
squares_gen = (x*x for x in range(5)) # Use () instead of []
print(f"\nGenerator Expression object: {squares_gen}")
print("Iterating over generator expression:")
for sq in squares_gen:
    print(f"  Square: {sq}")


# --- 9.3 Context Managers (`with` statement) ---
# Used for managing resources (like files, network connections, locks) by ensuring
# that setup and teardown actions are performed correctly, even if errors occur.
# The `with` statement uses objects that implement the context management protocol
# (`__enter__` and `__exit__` methods).

# Example: Creating a custom context manager class
class ManagedResource:
    def __init__(self, name):
        self.name = name
        print(f"Initializing resource '{self.name}'...")

    def __enter__(self):
        # Setup action: Called when entering the 'with' block
        print(f"Entering context for '{self.name}': Acquiring resource...")
        # You might return the resource itself or another related object
        return self # Often return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Teardown action: Called when exiting the 'with' block
        # exc_type, exc_val, exc_tb contain exception info if one occurred, otherwise None
        print(f"Exiting context for '{self.name}': Releasing resource...")
        if exc_type:
            print(f"  An exception occurred: {exc_type.__name__}: {exc_val}")
            # Return True to suppress the exception, False (or None) to propagate it
            return False # Propagate the exception by default
        print("  Exited cleanly.")
        return True # Suppress exception if desired (rarely needed unless handled)

print("\nContext Manager (Class) Example:")
with ManagedResource("MyResource") as resource:
    print(f"Inside 'with' block, working with {resource.name}...")
    # Simulate work
    # if True: raise ValueError("Something went wrong inside 'with'") # Test error handling

print("Outside 'with' block.")

# Example: Using contextlib.contextmanager decorator (simpler way)
from contextlib import contextmanager

@contextmanager
def managed_resource_func(name):
    print(f"\nInitializing resource '{name}' (using @contextmanager)...")
    # Code before yield is the __enter__ part
    resource_value = f"Resource Data for {name}"
    try:
        yield resource_value # The value yielded is available in the 'as' part
        # Code after yield (in normal flow) runs after the 'with' block body
        print(f"Exiting context for '{name}' cleanly (using @contextmanager)...")
    except Exception as e:
        # Exception handling within the generator acts like __exit__
        print(f"Exiting context for '{name}' after exception: {e} (using @contextmanager)...")
        # Re-raise the exception if you don't want to suppress it
        raise # Re-raises the caught exception
    finally:
        # Code in finally block always runs (like __exit__)
        print(f"Releasing resource '{name}' (using @contextmanager)...")

print("\nContext Manager (Decorator) Example:")
try:
    with managed_resource_func("AnotherResource") as data:
        print(f"Inside 'with' block, working with data: '{data}'")
        # if True: raise TypeError("Another error inside decorator 'with'") # Test error handling
except Exception as e:
    print(f"Caught exception outside the decorator 'with': {type(e).__name__}: {e}")

print("Outside decorator 'with' block.")

# --- 9.4 Interfaces / Abstract Base Classes (ABCs) ---
# Python doesn't have explicit 'interface' keyword like Java/C#.
# It often relies on "duck typing".
# However, for defining formal interfaces or ensuring subclasses implement
# specific methods, Abstract Base Classes (ABCs) from the 'abc' module are used.

import abc

# Define an Abstract Base Class
class Shape(abc.ABC): # Inherit from abc.ABC
    @abc.abstractmethod # Decorator marking 'area' as abstract
    def area(self) -> float:
        """Return the area of the shape."""
        pass # Abstract methods typically have no implementation

    @abc.abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass

    # Can also have concrete methods in an ABC
    def describe(self):
        print(f"This is a shape with area {self.area()} and perimeter {self.perimeter()}")

# Concrete subclass implementing the abstract methods
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

# Trying to instantiate the ABC directly will fail
# shape = Shape() # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

# Trying to instantiate a subclass that *doesn't* implement all abstract methods also fails
# class IncompleteSquare(Shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side * self.side
# # incomplete = IncompleteSquare(5) # TypeError: Can't instantiate abstract class... missing perimeter

print("\nAbstract Base Class (ABC) Example:")
rect = Rectangle(10, 5)
circ = Circle(7)

print(f"Rectangle area: {rect.area()}, perimeter: {rect.perimeter()}")
rect.describe() # Uses concrete method from ABC + implemented methods

print(f"Circle area: {circ.area():.2f}, perimeter: {circ.perimeter():.2f}")
circ.describe()

# Checking inheritance and instance types
print(f"Is Rectangle a subclass of Shape? {issubclass(Rectangle, Shape)}")
print(f"Is rect an instance of Shape? {isinstance(rect, Shape)}")


# ==============================================================================
# Section 10: Concurrency (Threading and Asyncio)
# ==============================================================================

print("\n=== Section 10: Concurrency (Threading and Asyncio) ===")

# Concurrency allows multiple tasks to make progress seemingly simultaneously.
# Python offers two main models: Threading and Asyncio.

# --- 10.1 Threading ---
# Uses OS-level threads. Good for I/O-bound tasks (waiting for network, disk).
# Subject to the Global Interpreter Lock (GIL) in CPython, which means only one
# thread can execute Python bytecode at a time per process. This limits true
# parallelism for CPU-bound tasks in CPython.

import threading
import time

def io_bound_task(name: str, duration: float):
    """Simulates a task that waits for I/O."""
    print(f"Thread '{name}': Starting task (will wait for {duration}s)...")
    time.sleep(duration) # Simulate waiting (e.g., network request)
    print(f"Thread '{name}': Finished task.")
    return f"{name} result"

print("\nThreading Example (I/O-bound):")
start_time_thread = time.time()

# Create thread objects
thread1 = threading.Thread(target=io_bound_task, args=("T1", 1.5), name="T1")
thread2 = threading.Thread(target=io_bound_task, args=("T2", 1.0), name="T2")

# Start the threads (they run concurrently)
thread1.start()
thread2.start()

# Wait for both threads to complete before continuing
print("Main thread: Waiting for T1 and T2 to finish...")
thread1.join() # Blocks until thread1 finishes
thread2.join() # Blocks until thread2 finishes

end_time_thread = time.time()
print(f"Threading finished in {end_time_thread - start_time_thread:.2f} seconds.")
# Note: Total time is ~max(1.5, 1.0), not 1.5 + 1.0, showing concurrency.

# Thread Synchronization (Example using Lock)
# Needed when multiple threads access shared resources to prevent race conditions.
shared_counter = 0
counter_lock = threading.Lock()

def increment_counter(name):
    global shared_counter
    print(f"Thread {name}: trying to acquire lock...")
    with counter_lock: # Acquire lock (blocks if already held)
        print(f"Thread {name}: acquired lock.")
        current_value = shared_counter
        # Simulate some processing time while holding the lock
        time.sleep(0.01)
        shared_counter = current_value + 1
        print(f"Thread {name}: incremented counter to {shared_counter}.")
    # Lock is automatically released when exiting 'with' block
    print(f"Thread {name}: released lock.")

print("\nThreading Synchronization (Lock) Example:")
threads = []
for i in range(5):
    t = threading.Thread(target=increment_counter, args=(f"Locker-{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final shared counter value: {shared_counter}") # Should be 5


# --- 10.2 Asyncio ---
# Uses a single thread and an event loop for cooperative multitasking.
# Relies on `async` and `await` keywords. Excellent for high-level structured
# network code and I/O-bound tasks without thread overhead. Tasks explicitly
# yield control using `await`. Not suitable for CPU-bound tasks as they block
# the single thread/event loop.

import asyncio

async def async_io_bound_task(name: str, duration: float):
    """Simulates an async task that waits for I/O."""
    print(f"Async Task '{name}': Starting (will await for {duration}s)...")
    await asyncio.sleep(duration) # Non-blocking sleep; yields control to event loop
    print(f"Async Task '{name}': Finished.")
    return f"{name} result"

async def main_async():
    """Main coroutine to run async tasks concurrently."""
    print("\nAsyncio Example (I/O-bound):")
    start_time_async = time.time()

    # Schedule tasks to run concurrently using asyncio.gather
    # gather waits for all provided awaitables (coroutines/futures) to complete
    task1 = asyncio.create_task(async_io_bound_task("A1", 1.5))
    task2 = asyncio.create_task(async_io_bound_task("A2", 1.0))
    task3 = asyncio.create_task(async_io_bound_task("A3", 0.5))

    print("Main coroutine: Awaiting gather...")
    # asyncio.gather collects results in order
    results = await asyncio.gather(task1, task2, task3)
    # Alternatively, just await them individually if order matters less for execution
    # await task1
    # await task2

    end_time_async = time.time()
    print(f"Asyncio tasks finished in {end_time_async - start_time_async:.2f} seconds.")
    # Again, time is ~max(1.5, 1.0, 0.5), showing concurrency.
    print(f"Asyncio results: {results}")

# To run the top-level async function:
if __name__ == "__main__": # Ensure this runs only when script is executed directly
    # In Python 3.7+ asyncio.run() is the preferred way to run the main async function
    try:
        asyncio.run(main_async())
    except RuntimeError as e:
        print(f"\nNote: Could not run asyncio example (possibly due to nested event loops): {e}")
        print("Asyncio examples often need to be run in a clean environment.")
    # Older way (pre 3.7):
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main_async())
    # loop.close()


# ==============================================================================
# Section 11: Pydantic and Pydantic-AI
# ==============================================================================

print("\n=== Section 11: Pydantic and Pydantic-AI ===")

# --- 11.1 Pydantic ---
# Data validation and settings management library using Python type hints.
# Enforces type hints at runtime, provides user-friendly errors, and allows
# defining complex data schemas easily. Widely used in API frameworks like FastAPI.

# You need to install pydantic first: pip install pydantic
try:
    from pydantic import BaseModel, Field, ValidationError, EmailStr, HttpUrl
    from typing import List, Optional
    from datetime import datetime

    print("\nPydantic Example:")

    # Define a data model using Pydantic BaseModel
    class User(BaseModel):
        id: int
        name: str = Field(..., min_length=2) # ... means required, adds validation
        signup_ts: Optional[datetime] = None # Optional field, defaults to None
        email: EmailStr # Built-in type for email validation
        website: Optional[HttpUrl] = None # Optional URL validation
        friends: List[int] = Field(default_factory=list) # Default to empty list

    # Example data (can be a dictionary)
    user_data_valid = {
        "id": 123,
        "name": "Alice",
        "signup_ts": "2023-01-15T10:30:00", # Pydantic automatically parses common formats
        "email": "alice@example.com",
        "website": "https://example.com",
        "friends": [1, 2, "3"] # Pydantic attempts type coercion (str '3' to int 3)
    }

    user_data_invalid = {
        "id": "not-an-int", # Invalid type
        "name": "A",        # Too short
        "email": "not-an-email", # Invalid format
        # signup_ts is optional, friends default, website optional
    }

    # --- Validation ---
    print("\nValidating data:")
    try:
        user_valid = User(**user_data_valid) # Unpack dict into model fields
        print("Valid data parsed successfully:")
        print(user_valid.model_dump_json(indent=2)) # Output as JSON string
        print(f"User ID: {user_valid.id}")
        print(f"Signup Timestamp (as datetime obj): {user_valid.signup_ts}")
        print(f"Friends list (coerced): {user_valid.friends}") # Note '3' became 3
    except ValidationError as e:
        print(f"Validation failed for valid data (unexpected): {e}")

    print("\nValidating invalid data:")
    try:
        user_invalid = User(**user_data_invalid)
        print("Invalid data parsed successfully (unexpected).")
        print(user_invalid.model_dump_json(indent=2))
    except ValidationError as e:
        print("Validation failed for invalid data (expected):")
        # Pydantic provides detailed error messages
        print(e.json(indent=2))

except ImportError:
    print("\nPydantic is not installed. Skipping Pydantic example.")
    print("Install using: pip install pydantic")
except Exception as e:
    print(f"\nAn error occurred during the Pydantic example: {e}")


# --- 11.2 Pydantic-AI (Conceptual Overview) ---
# Pydantic-AI is a library built on top of Pydantic that aims to bridge the gap
# between Large Language Models (LLMs) and structured data validation.
#
# Key Purpose: To reliably extract structured data (fitting a Pydantic model)
# from unstructured or semi-structured text generated by LLMs.
#
# How it typically works (conceptual):
# 1. Define a Pydantic Model: You define the structure of the data you want to extract.
# 2. Use an LLM: You prompt an LLM (like GPT, Claude, Gemini, etc.) to generate text
#    containing the desired information, perhaps asking it to format its response
#    in a specific way (though Pydantic-AI aims to handle less strict formats too).
# 3. Pydantic-AI Parsing: You feed the LLM's output text and your Pydantic model
#    to Pydantic-AI.
# 4. Validation & Extraction: Pydantic-AI uses the LLM itself (or sophisticated parsing)
#    to interpret the text and populate an instance of your Pydantic model. It leverages
#    Pydantic's validation rules during this process. It might even perform "correction loops"
#    where it asks the LLM to fix the output if it doesn't initially match the schema.
# 5. Structured Output: If successful, you get a validated Pydantic object containing
#    the extracted data.
#
# Use Cases:
# - Extracting structured information from emails, documents, chat logs.
# - Creating structured representations of function calls or API requests from natural language.
# - Ensuring LLM outputs adhere to a required format for downstream processing.
#
# Note: Using Pydantic-AI involves setting up an LLM client (like OpenAI's client)
# and potentially managing API keys. Its implementation details are more involved
# than basic Pydantic and depend heavily on the chosen LLM provider.
#
# Example (Conceptual - Requires `pydantic-ai` and an LLM client like `openai`):
# ```python
# # --- Conceptual Pydantic-AI Snippet (DO NOT RUN directly without setup) ---
# try:
#     from pydantic_ai import PydanticAI
#     from pydantic import BaseModel, Field
#     # Assuming you have an LLM client configured (e.g., from openai)
#     # from openai import OpenAI
#     # llm_client = OpenAI(api_key="YOUR_API_KEY") # Replace with actual setup
#
#     # 1. Define the Pydantic model for the desired structure
#     class PersonInfo(BaseModel):
#         name: str = Field(..., description="The full name of the person")
#         age: int = Field(..., description="The age of the person")
#         city: str = Field(..., description="The city where the person lives")
#
#     # 2. Sample unstructured text (e.g., from an LLM response)
#     unstructured_text = "John Doe is 35 years old and resides in New York City."
#
#     # 3. Use PydanticAI to parse the text into the model
#     # This requires a configured LLM client (like OpenAI, Anthropic, Gemini etc.)
#     # Replace `llm_client` with your actual configured LLM instance
#     # pydantic_ai_parser = PydanticAI(llm=llm_client)
#
#     print("\nConceptual Pydantic-AI Example (requires setup & API key):")
#     print(f"Input Text: {unstructured_text}")
#
#     # 4. Perform extraction (This step makes LLM calls)
#     # try:
#     #     extracted_info: PersonInfo = pydantic_ai_parser(
#     #         output_model=PersonInfo,
#     #         text=unstructured_text
#     #     )
#     #     # 5. Use the structured output
#     #     print("Extracted Information (Pydantic Model):")
#     #     print(extracted_info.model_dump_json(indent=2))
#     #     print(f"Name: {extracted_info.name}, Age: {extracted_info.age}, City: {extracted_info.city}")
#     # except Exception as ai_error:
#     #     print(f"Pydantic-AI extraction failed: {ai_error}")
#     #     print("Ensure LLM client is configured correctly and API key is valid.")
#
# except ImportError:
#    print("\nPydantic-AI or its dependencies (like an LLM client) are not installed.")
#    print("Install using: pip install pydantic-ai openai # Or other LLM provider")
# except Exception as e:
#    print(f"\nAn error occurred setting up the Pydantic-AI conceptual example: {e}")
# # --- End Conceptual Snippet ---
# ```
print("\nConceptual Pydantic-AI description provided above.")
print("Running the Pydantic-AI example requires installing 'pydantic-ai'")
print("and configuring an LLM client (e.g., OpenAI, Anthropic, Gemini) with API keys.")

# ==============================================================================
# Section 12: Conclusion
# ==============================================================================

print("\n=== Section 12: Conclusion ===")
print("You have reached the end of this comprehensive Python learning script.")
print("It covered:")
print("- Basics: Variables, types, operators, control flow, I/O.")
print("- Data Structures: Lists, tuples, dictionaries, sets.")
print("- Functions: Definition, arguments, scope, lambdas, type hinting.")
print("- OOP: Classes, objects, inheritance, polymorphism, encapsulation, properties.")
print("- Modules & Packages: Importing and structure.")
print("- Error Handling: try/except/finally, raising exceptions.")
print("- File I/O: Reading, writing, appending files.")
print("- Advanced Topics: Decorators, generators, context managers, ABCs.")
print("- Concurrency: Threading and Asyncio fundamentals.")
print("- Pydantic: Data validation and modeling.")
print("- Pydantic-AI: Concept of LLM output structuring.")
print("\nKeep practicing and exploring the vast Python ecosystem!")
print("Consider exploring libraries like NumPy, Pandas (data science), Flask, Django (web dev),")
print("Requests (HTTP), Matplotlib/Seaborn (plotting), etc.")
print("Good luck on your Python journey!")

# End of script