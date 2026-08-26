# Object-Oriented Programming with Python

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Course-RME%202203%20%7C%202213-6f42c1)](#course-information)
[![Status](https://img.shields.io/badge/Status-Learning%20Journey-2ea44f)](#learning-journey)

A practical collection of my academic work and independent exercises in **Python object-oriented programming (OOP)**. This repository documents my progression from Python fundamentals to designing reusable classes and modelling real-world systems with core OOP principles.

## OOP skills demonstrated

| Concept | What I practised | Examples |
| --- | --- | --- |
| Classes and objects | Constructors, instance state, class and static methods | [`Lab_1`](./Lab_1), [`ostad/module 4`](./ostad/module%204) |
| Encapsulation | Private/protected attributes, properties, getters and setters | [`goodBankAccount.py`](./Lab_final_practice/goodBankAccount.py), [`secureAccountWithPin.py`](./Lab_final_practice/secureAccountWithPin.py) |
| Inheritance | Single, multiple, multilevel, hierarchical and hybrid inheritance | [`Lab_final_practice`](./Lab_final_practice), [`inheritance.py`](./ostad/module%204/inheritance.py) |
| Polymorphism | Method overriding and common interfaces | [`polymorphism.py`](./ostad/module%204/polymorphism.py), [`paymentProcessingForDifferentPaymentMethod.py`](./Lab_final_practice/paymentProcessingForDifferentPaymentMethod.py) |
| Abstraction | Abstract base classes and implementation contracts | [`abstraction.py`](./Lab_final_practice/abstraction.py), [`shapeAreaCalculator.py`](./Lab_final_practice/shapeAreaCalculator.py) |
| Object relationships | Association, aggregation and composition | [`association_aggregation_composition.py`](./ostad/module%204/association_aggregation_composition.py) |
| Applied modelling | Payroll, banking, university, vehicle and payment systems | [`Lab_final_practice`](./Lab_final_practice) |
| Problem solving | Searching, sorting, recursion, strings and exception handling | [`Lab_2`](./Lab_2), [`Lab_3/Tasks`](./Lab_3/Tasks) |

## Featured projects

These examples best represent the object-oriented ideas explored in the repository:

- **Employee payroll system** — models multiple employee types through inheritance and polymorphic pay calculation.
- **Payment processing system** — gives different payment methods a shared interface and specialized behaviour.
- **University employee management** — applies inheritance to a real-world organizational hierarchy.
- **Secure bank account** — demonstrates encapsulation, private state and PIN-based access control.
- **Shape area calculator** — uses abstraction and method overriding across shape types.
- **Vehicle hierarchy** — explores reusable parent behaviour and specialized child classes.

You can find all of them in [`Lab_final_practice`](./Lab_final_practice).

## Repository structure

```text
OOP_academic/
├── Lab_1/                  # Classes, objects, self and class methods
├── Lab_2/                  # Python fundamentals and problem solving
├── Lab_3/Tasks/            # Searching, sorting and introductory OOP tasks
├── Lab_4/ ... Lab_6/       # Course lab exercises
├── 18_Lab7/ and 18_Lab8/  # Later lab submissions and encapsulation exercises
├── Lab_final_practice/     # Applied OOP mini-projects and exam preparation
├── Pynative_practices/     # Basic Python and focused OOP exercises
├── Random_practices/       # Additional problem-solving experiments
└── ostad/                  # Structured Python and OOP learning modules
```

Some folders and filenames follow the original course submission format so the academic history remains intact.

## Run the examples

This repository uses the Python standard library, so no package installation is required.

```bash
git clone <your-repository-url>
cd OOP_academic
python3 Lab_final_practice/employeePayrollSystem.py
```

Replace the final path with any example you want to explore. Most files are self-contained scripts and print their results to the terminal; a few exercises request console input.

## Learning journey

This is a learning repository rather than a single production application. Early files capture my first experiments, while later exercises show increasingly structured modelling with inheritance, abstraction, encapsulation and object relationships. Keeping that progression visible is intentional: it demonstrates both the concepts I have learned and how my Python design skills have developed over time.

## Course information

- **Degree:** B.Sc. in Robotics and Mechatronics Engineering, University of Dhaka
- **Level:** 2, Semester 2
- **Course:** Object-Oriented Programming
- **Course codes:** RME 2203 (Theory), RME 2213 (Lab)
- **Language:** Python
- **Instructor:** Dr. Md. Mehedi Hasan

## Future improvements

- Refactor selected exercises into importable packages
- Add automated tests for the featured mini-projects
- Apply consistent naming and Python style conventions
- Expand examples with type hints and documentation

## Feedback

Suggestions and constructive feedback are welcome. If you are exploring this repository, start with [`Lab_final_practice`](./Lab_final_practice) for the clearest overview of my OOP practice.
