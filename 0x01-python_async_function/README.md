# 0x01. Python - Async

## Overview
This project focuses on learning asynchronous programming in Python using `async` and `await` syntax. You will understand how to execute concurrent coroutines and manage asynchronous tasks. The project involves working with `asyncio` and Python's `random` module to achieve concurrency in a non-blocking manner.

![async_everywhere.png](async_everywhere.png)

## Concepts
- Async and await syntax in Python
- Executing asynchronous programs with `asyncio`
- Running concurrent coroutines
- Creating `asyncio` tasks
- Using the `random` module in async functions

## Tasks

| Task No. | Filename                       | Description                                                                 |
| -------- | ------------------------------ | --------------------------------------------------------------------------- |
| 0        | [0-basic_async_syntax.py](./0-basic_async_syntax.py) | Write an asynchronous coroutine `wait_random` that waits for a random delay between 0 and `max_delay` seconds and returns it. |
| 1        | [1-concurrent_coroutines.py](./1-concurrent_coroutines.py) | Write an async routine `wait_n` that runs `wait_random` n times concurrently and returns the delays in ascending order. |
| 2        | [2-measure_runtime.py](./2-measure_runtime.py) | Create a `measure_time` function to compute the average time taken to execute `wait_n`. |
| 3        | [3-tasks.py](./3-tasks.py) | Write a function `task_wait_random` that returns an `asyncio.Task` object for `wait_random`. |
| 4        | [4-tasks.py](./4-tasks.py) | Alter `wait_n` into `task_wait_n` by using `task_wait_random` to run the tasks concurrently. |

## Task Breakdown

### 0. The Basics of Async
**Filename:** [0-basic_async_syntax.py](./0-basic_async_syntax.py)  
**Description:**  
Create an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default value: 10) and waits for a random delay between 0 and `max_delay` (inclusive), then returns the delay.

### 1. Let's Execute Multiple Coroutines at the Same Time with async
**Filename:** [1-concurrent_coroutines.py](./1-concurrent_coroutines.py)  
**Description:**  
Write `wait_n`, which spawns `wait_random` n times and collects the delays into a list. Ensure that the delays are returned in ascending order, but without explicitly using sort functions.

### 2. Measure the Runtime
**Filename:** [2-measure_runtime.py](./2-measure_runtime.py)  
**Description:**  
Write a function `measure_time(n, max_delay)` that measures how long `wait_n(n, max_delay)` takes to complete, then returns the total time divided by n.

### 3. Tasks
**Filename:** [3-tasks.py](./3-tasks.py)  
**Description:**  
Write a function `task_wait_random(max_delay)` that returns an `asyncio.Task` object for `wait_random`.

### 4. Tasks (continued)
**Filename:** [4-tasks.py](./4-tasks.py)  
**Description:**  
Modify the `wait_n` function to `task_wait_n`, using `task_wait_random` to create tasks concurrently.

## Environment Setup
- Python 3.7 on Ubuntu 18.04 LTS
- Code should follow `pycodestyle` guidelines (version 2.5.x)
- Ensure all functions and coroutines are type-annotated
- All modules and functions should be documented

To run these scripts, you must have Python 3.7 installed and follow these steps:

```bash
chmod +x <filename>.py  # Make the script executable
./<filename>.py         # Run the script

