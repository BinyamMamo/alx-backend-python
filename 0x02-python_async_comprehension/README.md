# ✨ Python Async Comprehension Project

<img src="https://miro.medium.com/v2/resize:fit:1000/1*H79qyJfkGrq8eqjQ5LyJXw.jpeg" width="75%">

## ✍️ Project Description
This project focuses on implementing asynchronous generators and comprehensions in Python. It covers writing coroutines, using async comprehensions, and measuring the runtime of parallel asynchronous operations.

## 🔧 Requirements and Dependencies
- Python 3.7
- Libraries: asyncio, random

## 📚 Tasks
### Task 0: Async Generator
**📜 Task Requirements:** Write a coroutine called `async_generator` that yields 10 random numbers between 0 and 10 with a delay of 1 second between each yield.

**🗂️ Files:** [0-async_generator.py](0-async_generator.py)

**🗒️ Description:** This file contains a coroutine that asynchronously generates 10 random numbers with a delay of 1 second between each yield.

### Task 1: Async Comprehensions
**📜 Task Requirements:** Implement a coroutine named `async_comprehension` that collects 10 random numbers using async comprehension over `async_generator`.

**🗂️ Files:** [1-async_comprehension.py](1-async_comprehension.py)

**🗒️ Description:** This module defines a coroutine that utilizes async comprehension to collect 10 random numbers generated by the `async_generator` coroutine.

### Task 2: Run time for four parallel comprehensions
**📜 Task Requirements:** Create a coroutine named `measure_runtime` to measure the total runtime of executing `async_comprehension` four times in parallel using `asyncio.gather`.

**🗂️ Files:** [2-measure_runtime.py](2-measure_runtime.py)

**🗒️ Description:** This file contains a coroutine that measures the total runtime of executing `async_comprehension` four times in parallel using asyncio.gather.

## 🪄 Concluding paragraph
In this project, I learned about asynchronous generators, async comprehensions, and measuring runtime in parallel asynchronous operations in Python. It provided hands-on experience in leveraging asynchronous features for efficient concurrent programming.

## 🔗 Contact Information
[Binyam Mamo](https://github.com/BinyamMamo)
