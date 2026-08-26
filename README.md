# Object-Oriented Programming with Python

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Course-RME%202203%20%7C%202213-6f42c1)](#course-information)
[![Status](https://img.shields.io/badge/Status-Learning%20Journey-2ea44f)](#learning-journey)

A practical collection of my academic work and independent exercises in **Python object-oriented programming (OOP)**. This repository documents my progression from Python fundamentals to designing reusable classes and modelling real-world systems with core OOP principles.

## OOP skills demonstrated

| Concept | What I practised | Examples |
| --- | --- | --- |
| Classes and objects | Constructors, instance state, class and static methods | [`lab_01_oop_basics`](./lab_01_oop_basics), [`module_04_object_oriented_programming`](./ostad/module_04_object_oriented_programming) |
| Encapsulation | Private/protected attributes, properties, getters and setters | [`encapsulated_bank_account.py`](./final_oop_projects/encapsulated_bank_account.py), [`secure_bank_account_with_pin.py`](./final_oop_projects/secure_bank_account_with_pin.py) |
| Inheritance | Single, multiple, multilevel, hierarchical and hybrid inheritance | [`final_oop_projects`](./final_oop_projects), [`inheritance.py`](./ostad/module_04_object_oriented_programming/inheritance.py) |
| Polymorphism | Method overriding and common interfaces | [`polymorphism.py`](./ostad/module_04_object_oriented_programming/polymorphism.py), [`payment_processing_system.py`](./final_oop_projects/payment_processing_system.py) |
| Abstraction | Abstract base classes and implementation contracts | [`abstraction.py`](./final_oop_projects/abstraction.py), [`shape_area_calculator.py`](./final_oop_projects/shape_area_calculator.py) |
| Object relationships | Association, aggregation and composition | [`association_aggregation_composition.py`](./ostad/module_04_object_oriented_programming/association_aggregation_composition.py) |
| Applied modelling | Payroll, banking, university, vehicle and payment systems | [`final_oop_projects`](./final_oop_projects) |
| Problem solving | Searching, sorting, recursion, strings and exception handling | [`lab_02_python_fundamentals`](./lab_02_python_fundamentals), [`lab_03_algorithms/tasks`](./lab_03_algorithms/tasks) |

## Featured projects

These examples best represent the object-oriented ideas explored in the repository:

- **Employee payroll system** — models multiple employee types through inheritance and polymorphic pay calculation.
- **Payment processing system** — gives different payment methods a shared interface and specialized behaviour.
- **University employee management** — applies inheritance to a real-world organizational hierarchy.
- **Secure bank account** — demonstrates encapsulation, private state and PIN-based access control.
- **Shape area calculator** — uses abstraction and method overriding across shape types.
- **Vehicle hierarchy** — explores reusable parent behaviour and specialized child classes.

You can find all of them in [`final_oop_projects`](./final_oop_projects).

## Repository structure

```text
OOP_academic/
├── lab_01_oop_basics/                    # Classes, objects and methods
├── lab_02_python_fundamentals/           # Core Python problem solving
├── lab_03_algorithms/                    # Searching and sorting
├── lab_04_library_catalog_assessment/    # Library catalogue assessment
├── lab_05_collections/                   # Dictionaries, lists and sets
├── lab_06_string_processing/             # String exercises
├── lab_07_abstraction_submission/        # Abstract classes and methods
├── lab_08_inheritance_encapsulation_submission/
│                                           # Inheritance and secure state
├── final_oop_projects/                   # Applied OOP mini-projects
├── pynative_practice/                    # Python and OOP exercises
├── additional_practice/                  # Extra problem solving
└── ostad/                                # Structured learning modules
```

All active folders and scripts use descriptive `snake_case` names. ZIP archives are retained as snapshots of the original academic submissions and are named by their topic.

## Run the examples

This repository uses the Python standard library, so no package installation is required.

```bash
git clone <your-repository-url>
cd OOP_academic
python3 final_oop_projects/employee_payroll_system.py
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

Suggestions and constructive feedback are welcome. If you are exploring this repository, start with [`final_oop_projects`](./final_oop_projects) for the clearest overview of my OOP practice.
