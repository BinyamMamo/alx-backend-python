# Python Decorators – ALX Backend Project

This directory contains a series of tasks focused on mastering **Python decorators** in the context of database operations using SQLite3. The decorators cover common patterns such as logging, connection handling, transaction management, retries, and caching.

---

## 📁 Directory: `python-decorators-0x01`

### ✔️ Requirements

- Python 3.8+
- SQLite3
- A `users.db` database file with a `users` table.
- GitHub repo: `alx-backend-python`

---

## 🧠 Learning Objectives

- Deepen knowledge of Python decorators.
- Enhance database operations with reusable, clean, and efficient code.
- Learn to manage connections, transactions, retries, and caching using decorators.

---

## 🗂 Tasks

### `0-log_queries.py`
- **Goal:** Log SQL queries before executing them.
- **Decorator:** `log_queries`

---

### `1-with_db_connection.py`
- **Goal:** Automatically open and close database connections.
- **Decorator:** `with_db_connection`

---

### `2-transactional.py`
- **Goal:** Wrap DB ops in transactions (commit/rollback).
- **Decorators:** `with_db_connection`, `transactional`

---

### `3-retry_on_failure.py`
- **Goal:** Retry failed DB queries.
- **Decorators:** `with_db_connection`, `retry_on_failure(retries, delay)`

---

### `4-cache_query.py`
- **Goal:** Cache query results based on SQL string.
- **Decorators:** `with_db_connection`, `cache_query`

---

## 🛠 Usage

Ensure `users.db` exists and contains a `users` table. Then run any of the Python scripts:

```bash
python3 0-log_queries.py
```

Each script demonstrates the use of one or more decorators on realistic database tasks.

