# 🌐 Coroutines in Python Asyncio 🚀

In this guide, we'll delve into the concept of **coroutines** in Python's `asyncio` library. We'll explore what coroutines are, how they work, and how they interact with the event loop. We'll also provide detailed explanations and code examples to solidify your understanding.


## 📖 Table of Contents

1. [What is a Coroutine? 🤔](#1-what-is-a-coroutine-)
2. [The `async def` Syntax ✍️](#2-the-async-def-syntax-)
3. [Coroutine Functions vs. Coroutine Objects 🔄](#3-coroutine-functions-vs-coroutine-objects-)
4. [Using `await` with Coroutines ⏳](#4-using-await-with-coroutines-)
5. [Understanding the Event Loop 🔁](#5-understanding-the-event-loop-)
6. [Cancellation of Coroutines ❌](#6-cancellation-of-coroutines-)
7. [Putting It All Together 🧩](#7-putting-it-all-together-)
8. [Conclusion 🎉](#8-conclusion-)


## 1. What is a Coroutine? 🤔

A **coroutine** is a specialized version of a Python generator function that can **pause** and **resume** its execution. Coroutines are the building blocks of asynchronous programming in Python and are used extensively in the `asyncio` library to manage asynchronous tasks.

**Key Characteristics:**

- **Cooperative Multitasking 🤝**: Coroutines allow multiple tasks to run seemingly in parallel by yielding control to each other at specific points.
- **Non-Preemptive 🚫⏰**: The coroutine decides when to yield control, unlike threads, which can be preempted by the operating system.
- **Used with `asyncio` 🛠️**: Coroutines are fundamental to writing asynchronous code with `asyncio`.


## 2. The `async def` Syntax ✍️

In Python 3.5 and later, the `async def` syntax was introduced to define coroutine functions natively.

**Example:**

```python
async def my_coroutine():
    return 42
```

**Explanation:**

- **`async def`**: Defines an asynchronous function (coroutine function).
- **`my_coroutine`**: The name of the coroutine function.
- **`return 42`**: Coroutines can return values like regular functions.


## 3. Coroutine Functions vs. Coroutine Objects 🔄

It's important to distinguish between **coroutine functions** and **coroutine objects**.

### Coroutine Functions 🏭

- Defined using `async def`.
- They are **not** coroutines themselves but functions that return coroutine objects when called.

**Example:**

```python
async def my_coroutine():
    pass

print(type(my_coroutine))  # Output: <class 'function'>
```

- `my_coroutine` is a coroutine function.

### Coroutine Objects 🎁

- Created when a coroutine function is called.
- Represent the **execution** of the coroutine function.
- Can be awaited or scheduled to run in an event loop.

**Example:**

```python
coro_obj = my_coroutine()
print(type(coro_obj))  # Output: <class 'coroutine'>
```

- `coro_obj` is a coroutine object.

**Key Point:**

- **Calling** a coroutine function returns a coroutine object but does not start its execution.


## 4. Using `await` with Coroutines ⏳

The `await` keyword is used to **suspend** the execution of a coroutine until the awaited coroutine or future is complete.

**Example:**

```python
async def compute():
    return 21 * 2

async def main():
    result = await compute()
    print(f"The answer is {result}")

# To run the coroutine, use an event loop
import asyncio
asyncio.run(main())
```

**Explanation:**

- **`compute` Coroutine Function**:
  - Returns a computed value.
- **`main` Coroutine Function**:
  - Awaits the completion of `compute`.
  - Prints the result.
- **`await compute()`**:
  - Suspends `main` until `compute` completes and returns a result.
- **`asyncio.run(main())`**:
  - Starts the event loop and runs the `main` coroutine.


## 5. Understanding the Event Loop 🔁

The **event loop** orchestrates the execution of coroutines and handles I/O events.

**Key Functions:**

- **`asyncio.get_event_loop()`**: Retrieves the current event loop.
- **`loop.run_until_complete(coro)`**: Runs the coroutine `coro` until it completes.

**Example:**

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Get the event loop
loop = asyncio.get_event_loop()

# Run the coroutine until it completes
loop.run_until_complete(say_hello())

# Close the loop
loop.close()
```

**Explanation:**

- **`say_hello` Coroutine Function**:
  - Prints "Hello".
  - Awaits `asyncio.sleep(1)` to pause for 1 second.
  - Prints "World".
- **Event Loop Management**:
  - **`loop.run_until_complete(say_hello())`**: Schedules `say_hello` to run and waits for it to finish.
  - **`loop.close()`**: Closes the event loop.

**Note:**

- In modern Python (3.7+), it's recommended to use `asyncio.run()` to handle the event loop automatically:

  ```python
  asyncio.run(say_hello())
  ```


## 6. Cancellation of Coroutines ❌

Coroutines can be cancelled, which raises an `asyncio.CancelledError` exception inside the coroutine.

### Cancelling a Coroutine

**Example:**

```python
import asyncio

async def long_running_task():
    try:
        while True:
            print("Task is running...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise

async def main():
    task = asyncio.create_task(long_running_task())

    # Let the task run for 3 seconds
    await asyncio.sleep(3)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Caught task cancellation")

asyncio.run(main())
```

**Explanation:**

- **`long_running_task` Coroutine Function**:
  - Enters an infinite loop, printing a message every second.
  - Awaits `asyncio.sleep(1)` to yield control.
  - Handles `asyncio.CancelledError` to perform cleanup if needed.
- **`main` Coroutine Function**:
  - Creates a task for `long_running_task` using `asyncio.create_task()`.
  - Allows the task to run for 3 seconds using `await asyncio.sleep(3)`.
  - Cancels the task using `task.cancel()`.
  - Awaits the task to handle the cancellation exception.
- **Output**:

  ```
  Task is running...
  Task is running...
  Task is running...
  Task was cancelled
  Caught task cancellation
  ```

**Key Points:**

- **Cancelling a Task**:
  - `task.cancel()` requests cancellation.
  - The coroutine receives a `CancelledError` exception.
- **Handling `CancelledError`**:
  - Allows the coroutine to perform any necessary cleanup.
  - Should re-raise the exception or return to terminate the coroutine.


## 7. Putting It All Together 🧩

Let's combine what we've learned to see how coroutines, `await`, and the event loop work together.

### Example: Fetching Data Asynchronously 🌐

Suppose we want to fetch data from two different sources asynchronously.

**Code:**

```python
import asyncio

async def fetch_data(source, delay):
    print(f"Fetching data from {source}")
    await asyncio.sleep(delay)  # Simulate I/O operation
    data = f"Data from {source}"
    print(f"Finished fetching from {source}")
    return data

async def main():
    # Schedule both fetch_data coroutines concurrently
    task1 = asyncio.create_task(fetch_data("Source 1", 2))
    task2 = asyncio.create_task(fetch_data("Source 2", 3))

    # Await both tasks to complete
    results = await asyncio.gather(task1, task2)

    print("Results:")
    for result in results:
        print(result)

asyncio.run(main())
```

**Explanation:**

- **`fetch_data` Coroutine Function**:
  - Simulates fetching data from a source with a given delay.
  - Uses `await asyncio.sleep(delay)` to mimic an I/O-bound operation.
  - Returns the fetched data.
- **`main` Coroutine Function**:
  - Creates two tasks for fetching data from different sources.
  - Uses `asyncio.create_task()` to schedule them concurrently.
  - Awaits both tasks using `asyncio.gather()`.
  - Prints the results.
- **Output**:

  ```
  Fetching data from Source 1
  Fetching data from Source 2
  Finished fetching from Source 1
  Finished fetching from Source 2
  Results:
  Data from Source 1
  Data from Source 2
  ```

**Key Points:**

- **Concurrency with Tasks**:
  - By creating tasks, we allow multiple coroutines to run concurrently.
- **`asyncio.gather()`**:
  - Awaits multiple awaitables (coroutines or futures) concurrently.
  - Returns a list of results.


## 8. Conclusion 🎉

Understanding coroutines is fundamental to writing asynchronous code in Python using `asyncio`. Here's a recap of the key concepts:

- **Coroutines** are defined using `async def` and are the core building blocks of asynchronous code.
- **Coroutine Functions vs. Coroutine Objects**: Calling a coroutine function returns a coroutine object but does not start its execution.
- **`await` Keyword**: Used to suspend a coroutine until the awaited coroutine or future completes.
- **Event Loop**: Manages the execution of coroutines and handles scheduling.
- **Tasks**: Wrap coroutines and allow them to be scheduled for concurrent execution.
- **Cancellation**: Coroutines can be cancelled and should handle `asyncio.CancelledError` if cleanup is necessary.
