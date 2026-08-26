# Python & Object-Oriented Programming Portfolio

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Focus-Object--Oriented%20Programming-6f42c1)](#technical-skills)
[![University](https://img.shields.io/badge/University%20of%20Dhaka-RME-2ea44f)](#academic-background)

## About this portfolio

I am **Shahnewaj Hridoy**, a Robotics and Mechatronics Engineering student at the University of Dhaka. This repository presents my practical experience with **Python, object-oriented design, algorithms, data structures, and problem solving**.

The work ranges from focused concept implementations to complete domain models for banking, payroll, payments, university employees, shapes, and vehicles. Together, these projects demonstrate how I translate real-world requirements into classes, relationships, reusable behaviour, and maintainable program structure.

> **Portfolio highlights:** 160+ Python files covering the four pillars of OOP, multiple inheritance models, object relationships, searching and sorting algorithms, file handling, exception handling, and applied system design.

## Featured projects

| Project | Engineering focus | OOP evidence |
| --- | --- | --- |
| [Payment Processing System](./final_oop_projects/payment_processing_system.py) | A shared checkout flow for card, PayPal, and cash payments | Polymorphism, inheritance, extensible interfaces |
| [Employee Payroll System](./final_oop_projects/employee_payroll_system.py) | Different compensation rules for hourly and salaried employees | Inheritance, method overriding, runtime polymorphism |
| [University Employee Management](./final_oop_projects/university_employee_management_system.py) | Salary calculation across managers, developers, and researchers | Hierarchical inheritance, specialization, reusable base state |
| [Shape Area Calculator](./final_oop_projects/shape_area_calculator.py) | A common contract for rectangle, circle, and triangle calculations | Abstract base classes, polymorphism, `__str__` |
| [Secure Bank Account](./final_oop_projects/secure_bank_account_with_pin.py) | Controlled access to private balance information | Encapsulation, name mangling, method-based access |
| [Vehicle Hierarchy](./final_oop_projects/vehicle_hierarchy.py) | Specialized car and motorcycle models | Inheritance, overriding, domain modelling |
| [Library Catalogue Assessment](./lab_04_library_catalog_assessment/python_test_1/library_catalog_submission.py) | Catalogue operations over structured book records | Decomposition, searching, sorting, data processing |

## Technical skills

| Area | Demonstrated capabilities | Evidence |
| --- | --- | --- |
| Python | Functions, collections, comprehensions, file I/O, exceptions, modules | [Python foundations](./pynative_practice/python_fundamentals), [functions and files](./ostad/module_03_functions_and_files) |
| Classes and objects | Constructors, instance state, class variables, instance/class/static methods | [OOP basics](./lab_01_oop_basics), [method examples](./ostad/module_04_object_oriented_programming) |
| Encapsulation | Private and protected attributes, properties, getters/setters, controlled access | [Encapsulation examples](./lab_08_inheritance_encapsulation_submission/encapsulation_examples) |
| Inheritance | Single, multiple, multilevel, hierarchical, and hybrid inheritance; `super()` | [Inheritance examples](./lab_08_inheritance_encapsulation_submission/inheritance_examples) |
| Polymorphism | Method overriding and common interfaces across different object types | [Payment system](./final_oop_projects/payment_processing_system.py), [shape system](./final_oop_projects/shape_area_calculator.py) |
| Abstraction | `ABC`, abstract methods, abstract properties, implementation contracts | [Abstraction lab](./lab_07_abstraction_submission), [vehicle abstraction](./final_oop_projects/abstraction.py) |
| Object relationships | Association, aggregation, and composition | [Relationship examples](./ostad/module_04_object_oriented_programming/association_aggregation_composition.py) |
| Algorithms | Binary search, merge sort, quick sort, recursion | [Algorithms lab](./lab_03_algorithms/tasks) |
| Problem solving | Numeric, string, collection, validation, and transformation problems | [Complete project index](./PROJECT_INDEX.md) |

## OOP concepts demonstrated

### Encapsulation

Bank-account implementations progress from public state to private balance storage, PIN verification, failed-attempt tracking, and account-blocking design. This shows both the reason for encapsulation and its practical implementation.

### Inheritance

Dedicated examples cover every major inheritance structure. Larger systems then apply inheritance to meaningful domains such as employees, products, vehicles, organisms, and university roles.

### Polymorphism

The payment and shape projects process different concrete objects through a common method. New payment methods or shapes can be introduced without rewriting the client loop.

### Abstraction

Abstract base classes define required behaviour for vehicles and shapes. Concrete subclasses are responsible for their own implementations while client code depends on a stable contract.

### Association, aggregation, and composition

The object-relationship examples model students with laptops, universities with departments, and cars with engines to distinguish weak and strong ownership.

## Project index

The [complete project index](./PROJECT_INDEX.md) groups the repository by technical area:

- Python fundamentals and numerical problems
- Strings and text processing
- Lists, sets, and dictionaries
- Functions, files, and exceptions
- Searching and sorting algorithms
- Classes and object fundamentals
- Core OOP principles
- Applied OOP systems

For course review material, see the [final OOP revision notes](./final_oop_projects/README.md).

## Repository structure

```text
OOP_academic/
├── final_oop_projects/                   # Portfolio-ready OOP systems
├── lab_01_oop_basics/                    # Classes, objects, and methods
├── lab_02_python_fundamentals/           # Core problem solving
├── lab_03_algorithms/                    # Searching and sorting
├── lab_04_library_catalog_assessment/    # Applied catalogue assessment
├── lab_05_collections/                   # Lists and dictionaries
├── lab_06_string_processing/             # Text processing and validation
├── lab_07_abstraction_submission/        # Abstract class implementations
├── lab_08_inheritance_encapsulation_submission/
│                                           # Advanced OOP exercises
├── pynative_practice/                    # Extended Python practice
├── ostad/                                # Structured Python/OOP modules
└── additional_practice/                  # Independent experiments
```

## Run a project

The examples use the Python standard library and require no third-party packages.

```bash
git clone https://github.com/hridoy264/OOP_academic.git
cd OOP_academic
python3 final_oop_projects/payment_processing_system.py
```

Most programs are self-contained and display results in the terminal. Some foundational exercises request user input.

## Academic background

- **Student:** Shahnewaj Hridoy
- **Degree:** B.Sc. in Robotics and Mechatronics Engineering
- **University:** University of Dhaka
- **Course:** Object-Oriented Programming
- **Course codes:** RME 2203 (Theory), RME 2213 (Lab)
- **Language:** Python
- **Instructor:** Dr. Md. Mehedi Hasan

## Development roadmap

- Add automated unit tests for the featured systems
- Refactor selected scripts into importable Python packages
- Add type hints, docstrings, and consistent validation
- Expand the portfolio with persistence and command-line interfaces

This repository preserves my progression from Python fundamentals to applied object-oriented modelling. It is both a record of academic work and evidence of my ability to design, implement, and reason about Python software.
