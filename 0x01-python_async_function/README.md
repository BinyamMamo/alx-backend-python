# 0x01. Python - Async 📌

<p>
	<img src="https://miro.medium.com/v2/resize:fit:400/1*dZBikGD1DDmrqTbhI_qvUw.jpeg"
		width="40%"
	>
</p>

## Project Description ✨
This project focuses on exploring asynchronous programming in Python using the `async` and `await` syntax along with the `asyncio` module. It aims to provide a comprehensive understanding of executing asynchronous tasks, running concurrent coroutines, creating asyncio tasks, and utilizing the `random` module for asynchronous operations.

## 🔧 Requirements and Dependencies
- Python 3.7
- `pycodestyle` style checker (version 2.5.x)

##  📚 Tasks
### 📝 Task 0: The basics of async
**📃Task Requirements:**
- Implement an asynchronous coroutine `wait_random` that generates a random delay.
- The coroutine should take an integer argument `max_delay` with a default value of 10.
- Use the `random` module.

**📁 Files Used:** [0-basic_async_syntax.py](0-basic_async_syntax.py)

**🧾 Description:** `0-basic_async_syntax.py` contains the implementation of the `wait_random` coroutine, which generates a random delay between 0 and `max_delay`.

### 📝 Task 1: Let's execute multiple coroutines at the same time with async
**📃 Task Requirements:**
- Define an async function `wait_n` that spawns `wait_random` coroutine `n` times with a specified `max_delay`.
- Return a list of all delays in ascending order without using `sort()`.

**📂 Files Used:** [1-concurrent_coroutines.py](1-concurrent_coroutines.py)

**🧾 Description:** `1-concurrent_coroutines.py` implements the `wait_n` function to execute multiple coroutines concurrently and return their delays in ascending order.

### 📝 Task 2: Measure the runtime
**📃Task Requirements:** Create a function `measure_time` to measure the total execution time for `wait_n(n, max_delay)` and return the average execution time per coroutine.

**📁Files Used:** [2-measure_runtime.py](2-measure_runtime.py)

**🧾Description:**  `2-measure_runtime.py` contains the implementation of the `measure_time` function to calculate the average execution time per coroutine.

### 📝 Task 3: Tasks
**📃 Task Requirements:**
- Implement a function `task_wait_random` that returns an `asyncio.Task` object for the `wait_random` coroutine.

**📁 Files Used:** [3-tasks.py](3-tasks.py)

**🧾 Description:** `3-tasks.py` provides the implementation of the `task_wait_random` function to create asyncio tasks for the `wait_random` coroutine.

### 📝 Task 4: Tasks
**📃 Task Requirements:**
- Alter the code from Task 1 to create a new function `task_wait_n` that spawns `wait_random` coroutine using `asyncio.Task`.

**📁 Files Used:** [4-tasks.py](4-tasks.py)

**🧾 Description:** `4-tasks.py` contains the implementation of the `task_wait_n` function to execute multiple coroutines concurrently using asyncio tasks.

## 🪄 Conclusion
This project provided hands-on experience with asynchronous programming in Python, exploring the `async` and `await` syntax, and utilizing the `asyncio` module for concurrent execution. Through completing the tasks, I gained a deeper understanding of asynchronous programming concepts and how to effectively leverage them in Python development.

## 🧷 Contact
👤 **Binyam Mamo** <[Binyam Mamo](https://github.com/BinyamMamo)>
