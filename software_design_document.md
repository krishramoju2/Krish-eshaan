# Software Design Document (IEEE Format)

## Abstract
This document presents the system design extracted from the provided Python source code, including class structure and relationships.

## Introduction
The following system is implemented in Python. The design is described using UML diagrams and follows IEEE documentation standards.

## System Architecture

### Class `Animal`
- **Attributes:** species
- **Methods:** __init__, speak

### Class `Dog`
- **Inherits from:** Animal
- **Attributes:** name
- **Methods:** __init__, speak

### Class `Cat`
- **Inherits from:** Animal
- **Attributes:** name
- **Methods:** __init__, speak

## UML Class Diagram

- See the attached draw.io diagram XML for a visual representation.

## Source Code

```python
class Animal:
    def __init__(self, species):
        self.species = species
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")
        self.name = name
    def speak(self):
        print("Meow!")
```

## References

- IEEE Standard for Information Technology—Software Life Cycle Processes—Software Design (IEEE 1016-2009)
