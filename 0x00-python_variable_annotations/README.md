# 0x00. Python - Variable Annotations

## Overview
This project focuses on understanding and applying variable annotations in Python, leveraging Python's type hints to enhance code readability and maintainability. It covers concepts like type annotations for functions, variables, duck typing, and validation with mypy.

![py-strongly_dynamically_typed.png](py-strongly_dynamically_typed.png)

## Concepts
- Type annotations in Python 3
- Function signatures and variable types
- Duck typing
- Code validation using `mypy`

## Tasks

| Task No | Filename                | Description                                                     |
|-------------|-------------------------|-----------------------------------------------------------------|
| 0           | [0-add.py](0-add.py)     | Write a type-annotated function `add` that takes two floats and returns their sum as a float. |
| 1           | [1-concat.py](1-concat.py) | Write a type-annotated function `concat` that takes two strings and returns their concatenation. |
| 2           | [2-floor.py](2-floor.py) | Write a type-annotated function `floor` that takes a float and returns the floor as an integer. |
| 3           | [3-to_str.py](3-to_str.py) | Write a type-annotated function `to_str` that takes a float and returns its string representation. |
| 4           | [4-define_variables.py](4-define_variables.py) | Define and annotate variables with specified values. |
| 5           | [5-sum_list.py](5-sum_list.py) | Write a type-annotated function `sum_list` that takes a list of floats and returns their sum. |
| 6           | [6-sum_mixed_list.py](6-sum_mixed_list.py) | Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float. |
| 7           | [7-to_kv.py](7-to_kv.py) | Write a type-annotated function `to_kv` that takes a string and an int/float, returns a tuple with the string and square of the int/float. |
| 8           | [8-make_multiplier.py](8-make_multiplier.py) | Write a type-annotated function `make_multiplier` that takes a float and returns a function to multiply by that float. |
| 9           | [9-element_length.py](9-element_length.py) | Annotate a function that takes an iterable and returns a list of tuples containing each element and its length. |
| 10          | [100-safe_first_element.py](100-safe_first_element.py) | Augment a function with correct duck-typed annotations. |
| 11          | [101-safely_get_value.py](101-safely_get_value.py) | Add type annotations to a function for safely getting values from a dictionary. |
| 12          | [102-type_checking.py](102-type_checking.py) | Use `mypy` to validate type annotations in a function for zooming arrays. |

## Setup Environment
- Ensure Python 3.7 is installed on Ubuntu 18.04 LTS
- Run the following command to validate your code:
  ```bash
  mypy <filename.py>

