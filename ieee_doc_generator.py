def generate_ieee_documentation(classes, code_text):
    doc = """
# Software Design Document (IEEE Format)

## Abstract
This document presents the system design extracted from the provided Python source code, including class structure and relationships.

## Introduction
The following system is implemented in Python. The design is described using UML diagrams and follows IEEE documentation standards.

## System Architecture

"""
    for cls in classes:
        doc += f"### Class `{cls.name}`\n"
        if cls.parents:
            doc += f"- **Inherits from:** {', '.join(cls.parents)}\n"
        if cls.attributes:
            doc += f"- **Attributes:** {', '.join(cls.attributes)}\n"
        if cls.methods:
            doc += f"- **Methods:** {', '.join(cls.methods)}\n"
        doc += "\n"
    doc += """
## UML Class Diagram

- See the attached draw.io diagram XML for a visual representation.

## Source Code

```python
""" + code_text + """
