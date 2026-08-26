# Final OOP Revision Guide

Use this folder for final exam, lab test, and viva revision. The problems are separated by type so you can revise one OOP concept at a time.

## Quick revision order

1. Classes, objects, constructors, and `self`
2. Single inheritance and `super()`
3. Multiple, multilevel, hierarchical, and hybrid inheritance
4. Encapsulation and private attributes
5. Method overriding and polymorphism
6. Abstract base classes and abstract methods
7. Applied systems combining several principles

## Problems by type

### Inheritance

| Problem | Main idea | Level | Revision task |
| --- | --- | --- | --- |
| [`single_inheritance.py`](./single_inheritance.py) | Parent `Animal`, child `Dog`, method overriding | Beginner | Add `Cat` with its own sound |
| [`using_super.py`](./using_super.py) | Initialize parent state with `super()` | Beginner | Add another electronic product attribute |
| [`multilevel_inheritance.py`](./multilevel_inheritance.py) | `Organism → Plant → FloweringPlant` | Beginner | Add one more inheritance level |
| [`multiple_inheritance.py`](./multiple_inheritance.py) | Combine `Artist` and `Engineer` behaviour | Intermediate | Explain the method resolution order |
| [`hierarchical_inheritance.py`](./hierarchical_inheritance.py) | Several child classes share one parent | Intermediate | Add a child with specialized state |
| [`hybrid_inheritance.py`](./hybrid_inheritance.py) | Multiple inheritance forms in one hierarchy | Intermediate | Refactor constructors to use `super()` |
| [`vehicle_hierarchy.py`](./vehicle_hierarchy.py) | Applied vehicle specialization | Intermediate | Return and display fuel efficiency |

### Encapsulation and access control

| Problem | Main idea | Level | Revision task |
| --- | --- | --- | --- |
| [`bank_account_without_access_control.py`](./bank_account_without_access_control.py) | Why public balance is unsafe | Beginner | Demonstrate unwanted direct modification |
| [`encapsulated_bank_account.py`](./encapsulated_bank_account.py) | Private balance and controlled methods | Beginner | Reject zero and negative amounts |
| [`secure_bank_account_with_pin.py`](./secure_bank_account_with_pin.py) | Private balance with PIN verification | Intermediate | Require the PIN for withdrawals |
| [`secure_account_attempt_tracking.py`](./secure_account_attempt_tracking.py) | Count failed authentication attempts | Intermediate | Reset attempts after a correct PIN |
| [`blocked_secure_account_draft.py`](./blocked_secure_account_draft.py) | Account blocking design | Draft challenge | Complete blocking after three failures |

### Abstraction and polymorphism

| Problem | Main idea | Level | Revision task |
| --- | --- | --- | --- |
| [`abstraction.py`](./abstraction.py) | Abstract methods and abstract properties | Intermediate | Add a `Truck` implementation |
| [`shape_area_calculator.py`](./shape_area_calculator.py) | Common abstract interface for shapes | Intermediate | Use `math.pi` and add `Square` |
| [`payment_processing_system.py`](./payment_processing_system.py) | Polymorphic payment processing | Intermediate | Add mobile banking without changing the loop |
| [`payment_processing_notes.py`](./payment_processing_notes.py) | Saved checkout call notes | Reference | Use the calls to test every payment type |

### Applied OOP systems

| Problem | Main idea | Level | Revision task |
| --- | --- | --- | --- |
| [`employee_payroll_system.py`](./employee_payroll_system.py) | Employee subclasses calculate pay differently | Advanced | Make the base class abstract |
| [`university_employee_management_system.py`](./university_employee_management_system.py) | Role-based salaries through inheritance | Advanced | Validate salary inputs and add a lecturer |
| [`vehicle_hierarchy.py`](./vehicle_hierarchy.py) | Inheritance, overriding, and domain modelling | Advanced | Add polymorphic fuel calculations |
| [`payment_processing_system.py`](./payment_processing_system.py) | Shared interface across payment strategies | Advanced | Return transaction details instead of printing |

### Python problem solving and exceptions

| Problem | Main idea | Level | Revision task |
| --- | --- | --- | --- |
| [`extra_character_finder.py`](./extra_character_finder.py) | Nested-loop string comparison | Beginner | Solve again using character counts |
| [`exception_practice.py`](./exception_practice.py) | Exception handling | Draft challenge | Add examples for `ValueError` and division by zero |

## Concept checklist

Before the exam, make sure you can answer these without looking at the code:

- What is the difference between a class and an object?
- What does `self` represent?
- Why is `__init__` used?
- What is the difference between instance, class, and static methods?
- What is name mangling, and what does `__balance` become internally?
- When should `super()` be used?
- What is method overriding?
- How does polymorphism reduce `if`/`elif` type checking?
- Why can an abstract class not be instantiated?
- What is the difference between inheritance, association, aggregation, and composition?
- What is Python's method resolution order in multiple inheritance?

## Viva-ready definitions

| Term | Short definition |
| --- | --- |
| Class | A blueprint that defines data and behaviour |
| Object | A runtime instance of a class |
| Encapsulation | Bundling state with controlled behaviour |
| Inheritance | Creating a class from an existing class |
| Polymorphism | Different objects responding to the same interface |
| Abstraction | Exposing essential operations while hiding implementation details |
| Method overriding | Replacing inherited behaviour in a child class |
| Composition | Strong ownership where one object creates or controls another |

## Final practice routine

For each problem:

1. Draw the class hierarchy.
2. Identify parent classes, child classes, attributes, and methods.
3. Write the solution from memory.
4. Run at least three normal tests and two edge cases.
5. Explain the OOP principle aloud as if answering a viva question.
6. Compare your version with the repository solution and refactor it.

## Mock final challenges

### Challenge 1: Library system

Create `LibraryItem`, `Book`, and `Magazine`. Make borrowing behaviour polymorphic, keep availability private, and raise an exception when an unavailable item is borrowed.

### Challenge 2: Robotics team payroll

Create an abstract `TeamMember` with `calculate_payment()`. Implement `Researcher`, `Engineer`, and `Intern`, each with different payment rules.

### Challenge 3: Payment checkout

Create an abstract payment interface and implement card, cash, and mobile banking. The checkout function must work with every method without checking its concrete class.

When these three challenges can be completed without copying, the core course outcomes have been revised.
