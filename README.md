# Python OOP Tutorial and Practice Platform

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Course-RME%202203%20%7C%202213-6f42c1)](#academic-context)
[![Learning](https://img.shields.io/badge/Mode-Tutorial%20%2B%20Practice-2ea44f)](#learning-path)

A step-by-step Python and object-oriented programming learning platform based on my academic labs, independent exercises, assessments, and final revision projects.

Use this repository to **learn a concept, study a small example, solve a related problem, and then compare your approach with an existing implementation**.

## Start here

| Your goal | Go to |
| --- | --- |
| Follow the course from beginner to advanced | [Learning path](#learning-path) |
| Find practice by problem type | [Complete practice catalogue](./PRACTICE_CATALOG.md) |
| Prepare for an OOP exam or viva | [Final revision guide](./final_oop_projects/README.md) |
| Review the strongest applied examples | [`final_oop_projects`](./final_oop_projects) |
| Practise Python fundamentals first | [`pynative_practice/python_fundamentals`](./pynative_practice/python_fundamentals) |

## How to use this platform

For each topic, use this four-step cycle:

1. **Learn** — read the short concept summary below.
2. **Predict** — inspect an example and predict its output before running it.
3. **Practise** — recreate the solution without looking at the original code.
4. **Improve** — add validation, type hints, tests, or a new subclass.

Run any self-contained example from the repository root:

```bash
python3 final_oop_projects/employee_payroll_system.py
```

Some fundamental exercises request terminal input. All examples use the Python standard library, so no package installation is required.

## OOP tutorial

### 1. Classes and objects

A **class** is a blueprint. An **object** is one instance created from that blueprint. The `__init__` method initializes object state, while `self` refers to the current object.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}"

student = Student("Hridoy")
print(student.introduce())
```

Study [`lab_01_oop_basics`](./lab_01_oop_basics), then practise with [`pynative_practice/oop_exercises`](./pynative_practice/oop_exercises).

### 2. Encapsulation

Encapsulation keeps state and the methods that control it together. Python commonly uses `_name` for protected-by-convention attributes and `__name` for name-mangled private attributes.

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

Compare the unsafe and protected versions in [`lab_08_inheritance_encapsulation_submission/encapsulation_examples`](./lab_08_inheritance_encapsulation_submission/encapsulation_examples).

### 3. Inheritance and `super()`

Inheritance lets a child class reuse and specialize a parent class. `super()` calls the parent implementation without hard-coding the parent class name.

```python
class Vehicle:
    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def start(self):
        return "Car started"
```

Review every inheritance form in [`lab_08_inheritance_encapsulation_submission/inheritance_examples`](./lab_08_inheritance_encapsulation_submission/inheritance_examples).

### 4. Polymorphism

Polymorphism lets different objects respond to the same method call in their own way. Code can work with a shared interface instead of checking every concrete type.

```python
for payment_method in payment_methods:
    payment_method.process_payment(100)
```

Study [`payment_processing_system.py`](./final_oop_projects/payment_processing_system.py) and [`shape_area_calculator.py`](./final_oop_projects/shape_area_calculator.py).

### 5. Abstraction

Abstraction defines what subclasses must do while hiding implementation details. Python provides `ABC` and `@abstractmethod` for explicit abstract contracts.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

Begin with [`lab_07_abstraction_submission`](./lab_07_abstraction_submission), then solve the shape problem in the final revision set.

### 6. Object relationships

- **Association:** two independent objects communicate.
- **Aggregation:** one object contains objects that can exist independently.
- **Composition:** one object owns another object's lifetime.

Study all three together in [`association_aggregation_composition.py`](./ostad/module_04_object_oriented_programming/association_aggregation_composition.py).

## Learning path

| Stage | Topics | Learn from | Practice outcome |
| --- | --- | --- | --- |
| 1. Python foundations | Variables, conditions, loops, strings, collections | [`ostad/modules_01_02_python_basics`](./ostad/modules_01_02_python_basics) | Write small input/output programs |
| 2. Problem solving | Numbers, strings, patterns, files | [`pynative_practice/python_fundamentals`](./pynative_practice/python_fundamentals) | Break problems into clear steps |
| 3. Functions and errors | Parameters, scope, lambda, files, exceptions | [`ostad/module_03_functions_and_files`](./ostad/module_03_functions_and_files) | Build reusable functions |
| 4. OOP foundations | Classes, objects, constructors, methods | [`lab_01_oop_basics`](./lab_01_oop_basics) | Model a simple real object |
| 5. Algorithms | Binary search, merge sort, quick sort | [`lab_03_algorithms`](./lab_03_algorithms) | Explain algorithm flow and complexity |
| 6. Core OOP | Encapsulation, inheritance, polymorphism | [`ostad/module_04_object_oriented_programming`](./ostad/module_04_object_oriented_programming) | Reuse and specialize behaviour |
| 7. Advanced OOP | Abstraction and object relationships | [`lab_07_abstraction_submission`](./lab_07_abstraction_submission) | Design around contracts |
| 8. Applied modelling | Banking, payroll, payments, shapes, vehicles | [`final_oop_projects`](./final_oop_projects) | Combine multiple OOP principles |

## Practice rules

- Create your solution in a separate scratch file before opening the provided answer.
- Test normal cases, boundary cases, and invalid input.
- Explain which OOP principle each class demonstrates.
- Refactor repeated logic into a parent class or helper method.
- Prefer behaviour methods over changing object attributes directly.
- Treat files marked **Draft** in the final revision guide as exercises to complete.

## Repository map

| Folder | Purpose |
| --- | --- |
| [`lab_01_oop_basics`](./lab_01_oop_basics) | Introductory classes, objects, `self`, and class methods |
| [`lab_02_python_fundamentals`](./lab_02_python_fundamentals) | Short numeric and string problems |
| [`lab_03_algorithms`](./lab_03_algorithms) | Searching, sorting, and an introductory class task |
| [`lab_04_library_catalog_assessment`](./lab_04_library_catalog_assessment) | Larger catalogue assessment |
| [`lab_05_collections`](./lab_05_collections) | Lists, dictionaries, filtering, and lookup problems |
| [`lab_06_string_processing`](./lab_06_string_processing) | Validation and text-processing exercises |
| [`lab_07_abstraction_submission`](./lab_07_abstraction_submission) | Abstract class examples |
| [`lab_08_inheritance_encapsulation_submission`](./lab_08_inheritance_encapsulation_submission) | Inheritance and secure account exercises |
| [`final_oop_projects`](./final_oop_projects) | Final revision and applied OOP problems |
| [`pynative_practice`](./pynative_practice) | Extended beginner and OOP practice |
| [`ostad`](./ostad) | Structured lesson examples |
| [`additional_practice`](./additional_practice) | Extra experiments and utility problems |

## Recommended challenges

After finishing the existing exercises:

1. Add input validation and custom exceptions to the bank account.
2. Convert `Employee.calculate_pay()` into an abstract method.
3. Add a new `MobileBankingPayment` class without changing checkout logic.
4. Add `Square` and `Trapezoid` to the shape calculator.
5. Write unit tests for deposits, withdrawals, overtime, and payment fees.
6. Refactor scripts so example code only runs inside `if __name__ == "__main__":`.

## Academic context

- **Degree:** B.Sc. in Robotics and Mechatronics Engineering, University of Dhaka
- **Level:** 2, Semester 2
- **Course:** Object-Oriented Programming
- **Course codes:** RME 2203 (Theory), RME 2213 (Lab)
- **Language:** Python
- **Instructor:** Dr. Md. Mehedi Hasan

This is a learning repository. Early examples intentionally show the development of my understanding, while later projects combine multiple OOP ideas into larger models.
