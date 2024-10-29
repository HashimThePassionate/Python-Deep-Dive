# 🏰 The Tower of Asyncio
In this guide, we'll explore the concept of the **"Tower of Asyncio,"** which is a hierarchical way to understand the various layers and components of the `asyncio` module in Python. This structure helps differentiate between features essential for end-user developers and those intended for framework designers. We'll delve into each tier in detail, providing comprehensive explanations to enhance your understanding.


## 📖 Table of Contents

1. [Introduction](#1-introduction-)
2. [The Hierarchy of Asyncio](#2-the-hierarchy-of-asyncio-)
   - [Tier 1: Coroutines and `await`](#tier-1-coroutines-and-await-)
   - [Tier 2: Event Loop](#tier-2-event-loop-)
   - [Tier 3: Futures](#tier-3-futures-)
   - [Tier 4: Tasks](#tier-4-tasks-)
   - [Tier 5: Executors and Subprocesses](#tier-5-executors-and-subprocesses-)
   - [Tier 6: Asyncio Utilities](#tier-6-asyncio-utilities-)
   - [Tier 7: Transports](#tier-7-transports-)
   - [Tier 8: Protocols](#tier-8-protocols-)
   - [Tier 9: Streams API](#tier-9-streams-api-)
3. [Focusing on Essential Tiers for End-User Developers](#3-focusing-on-essential-tiers-for-end-user-developers-)
4. [Conclusion](#4-conclusion-)
5. [Additional Resources](#5-additional-resources-)


## 1. Introduction 📚

The `asyncio` module in Python is a powerful tool for writing concurrent code using the async/await syntax. However, its documentation can be overwhelming due to the breadth of APIs it offers, often without clear guidance on which parts are most relevant to different types of users.

To simplify this, we can visualize `asyncio` as a hierarchical **tower**, where each level builds upon the previous one. This conceptual model helps both end-user developers and framework designers understand which components they need to focus on.


## 2. The Hierarchy of Asyncio 🏗️

Let's explore each tier of the **Tower of Asyncio** in detail:

### Tier 1: Coroutines and `await`

**Description**:

- **Coroutines** are the foundation of asynchronous programming in Python. They are special functions defined using the `async def` syntax.
- The `await` keyword is used within coroutines to pause execution until the awaited coroutine or asynchronous operation is complete.

**Key Concepts**:

- **Defining a Coroutine**:

  ```python
  async def my_coroutine():
      # Asynchronous code here
      pass
  ```

- **Using `await`**:

  ```python
  async def my_coroutine():
      result = await another_coroutine()
  ```

**Detailed Explanation**:

- **Coroutines** are similar to generators but are designed for asynchronous programming. When a coroutine is called, it returns a **coroutine object** but doesn't start execution immediately.
- **`await`** suspends the execution of the coroutine until the awaited object (another coroutine or an awaitable) is complete. This allows other coroutines to run in the meantime.

**Importance for Developers**:

- Understanding how to write coroutines and use `await` is **essential** for asynchronous programming.
- Some frameworks like **Curio** and **Trio** operate solely on native coroutines without relying on the `asyncio` module, highlighting the fundamental role of coroutines.


### Tier 2: Event Loop

**Description**:

- The **event loop** is the core component that manages and schedules the execution of coroutines.
- It handles the orchestration of asynchronous tasks, ensuring they run when ready and managing I/O events.

**Key Concepts**:

- **Obtaining the Event Loop**:

  ```python
  loop = asyncio.get_event_loop()
  ```

- **Running Coroutines**:

  ```python
  loop.run_until_complete(my_coroutine())
  ```

- **High-Level API**:

  ```python
  asyncio.run(my_coroutine())
  ```

**Detailed Explanation**:

- **Event Loop Mechanics**:

  - The event loop continuously checks for completed I/O operations and resumes the corresponding coroutines.
  - It runs in a single thread, leveraging cooperative multitasking, where coroutines yield control using `await`.

- **Separation of Specification and Implementation**:

  - **AbstractEventLoop**: Defines the event loop's interface.
  - **BaseEventLoop**: Provides a default implementation.
  - This separation allows for alternative implementations, such as **uvloop**, a high-performance event loop.

**Importance for Developers**:

- Understanding how to start, manage, and close the event loop is **crucial**.
- The event loop is what brings coroutines to life, making it necessary for any asynchronous application.


### Tier 3: Futures

**Description**:

- **Futures** represent a placeholder for a result that will be available in the future.
- In `asyncio`, a **Future** is an object that can be awaited and is used to bridge low-level callback-based code with coroutine-based code.

**Key Concepts**:

- **Creating a Future**:

  ```python
  future = asyncio.Future()
  ```

- **Setting a Result**:

  ```python
  future.set_result('result')
  ```

- **Awaiting a Future**:

  ```python
  result = await future
  ```

**Detailed Explanation**:

- **Loop-Aware**:

  - Futures are associated with the event loop and are aware of its state.
  - They provide a way to handle the result of asynchronous operations that are not coroutines.

- **Use Cases**:

  - Integrating with code that uses callbacks.
  - Representing one-time events that will happen in the future.

**Importance for Developers**:

- While not as commonly used directly by end-user developers, understanding futures is helpful for advanced asynchronous programming.
- Framework designers often use futures to build higher-level abstractions.


### Tier 4: Tasks

**Description**:

- **Tasks** are a subclass of **Future** that wrap coroutines and schedule their execution on the event loop.
- They represent the execution of a coroutine and allow you to track its progress.

**Key Concepts**:

- **Creating a Task**:

  ```python
  task = asyncio.create_task(my_coroutine())
  ```

- **Awaiting a Task**:

  ```python
  result = await task
  ```

**Detailed Explanation**:

- **Loop-Aware and Coroutine-Aware**:

  - Tasks are aware of both the event loop and the coroutine they are wrapping.
  - They manage the execution of the coroutine, including scheduling and result retrieval.

- **Task Methods**:

  - **`task.cancel()`**: Requests cancellation of the task.
  - **`task.done()`**: Checks if the task is completed.
  - **`task.result()`**: Retrieves the result when the task is done.

**Importance for Developers**:

- Tasks are essential for running coroutines concurrently.
- They allow you to schedule multiple coroutines and manage their execution.


### Tier 5: Executors and Subprocesses

**Description**:

- **Executors** allow you to run blocking code in separate threads or processes without blocking the event loop.
- **Subprocesses** enable running external processes asynchronously.

**Key Concepts**:

- **Running Blocking Code**:

  ```python
  loop.run_in_executor(None, blocking_function)
  ```

- **Using Executors**:

  - **ThreadPoolExecutor**: For I/O-bound blocking tasks.
  - **ProcessPoolExecutor**: For CPU-bound tasks to avoid the GIL.

- **Running Subprocesses**:

  ```python
  proc = await asyncio.create_subprocess_exec('cmd', 'arg')
  ```

**Detailed Explanation**:

- **Need for Executors**:

  - Since the event loop runs in a single thread, blocking operations can freeze the entire loop.
  - Executors offload these operations to separate threads or processes.

- **`run_in_executor()`**:

  - Schedules a function to run in an executor.
  - Returns a Future that can be awaited.

**Importance for Developers**:

- Handling blocking code is a common necessity.
- Executors allow you to integrate existing synchronous code into your asynchronous application.


### Tier 6: Asyncio Utilities

**Description**:

- This tier includes utilities and tools that are designed to work with coroutines.
- Examples include **`asyncio.Queue`**, synchronization primitives, and locks.

**Key Concepts**:

- **Asyncio Queue**:

  ```python
  queue = asyncio.Queue()
  await queue.put(item)
  item = await queue.get()
  ```

- **Synchronization Primitives**:

  - **Locks**: `asyncio.Lock()`
  - **Events**: `asyncio.Event()`
  - **Semaphores**: `asyncio.Semaphore()`

**Detailed Explanation**:

- **`asyncio.Queue`**:

  - Works similarly to `queue.Queue` but is designed for use with coroutines.
  - Methods like `put()` and `get()` are coroutines and need to be awaited.

- **Use Cases**:

  - Managing communication between coroutines.
  - Implementing producer-consumer patterns.

**Importance for Developers**:

- Essential for coordinating tasks and sharing data safely between coroutines.
- These utilities help manage complex asynchronous workflows.


### Tier 7: Transports

**Description**:

- **Transports** are low-level abstractions for data transmission.
- They handle the actual I/O operations, such as sending and receiving bytes.

**Key Concepts**:

- **BaseTransport**: The base class for all transports.
- **Types of Transports**:

  - **ReadTransport**
  - **WriteTransport**
  - **DatagramTransport**

**Detailed Explanation**:

- **Role of Transports**:

  - Decouple the protocol logic from the underlying I/O mechanism.
  - Allow for flexibility in how data is sent and received.

- **Working with Transports**:

  - Typically managed by the event loop and not used directly.
  - Paired with protocols to handle I/O events.

**Importance for Developers**:

- Mostly relevant for framework developers or when building custom networking components.
- End-user developers usually interact with higher-level APIs.


### Tier 8: Protocols

**Description**:

- **Protocols** define how to handle events like data received, connection made, or connection lost.
- They are classes that implement callback methods invoked by transports.

**Key Concepts**:

- **Creating a Protocol**:

  ```python
  class MyProtocol(asyncio.Protocol):
      def connection_made(self, transport):
          pass

      def data_received(self, data):
          pass

      def connection_lost(self, exc):
          pass
  ```

- **Registering a Protocol**:

  ```python
  loop.create_connection(MyProtocol, 'host', port)
  ```

**Detailed Explanation**:

- **Protocol Methods**:

  - **`connection_made()`**: Called when a connection is established.
  - **`data_received()`**: Called when data is received.
  - **`connection_lost()`**: Called when the connection is closed.

- **Interaction with Transports**:

  - Protocols receive a transport instance to send data.
  - They focus on the logic of handling events, while transports handle the I/O.

**Importance for Developers**:

- Useful when you need fine-grained control over network communication.
- More advanced and typically used in custom networking applications.


### Tier 9: Streams API

**Description**:

- The **Streams API** provides high-level, easy-to-use abstractions for network I/O.
- It simplifies handling TCP connections and data streams.

**Key Concepts**:

- **Opening a Connection**:

  ```python
  reader, writer = await asyncio.open_connection('host', port)
  ```

- **Starting a Server**:

  ```python
  server = await asyncio.start_server(client_handler, 'host', port)
  ```

- **StreamReader and StreamWriter**:

  - **`reader.read(n)`**: Reads up to `n` bytes.
  - **`writer.write(data)`**: Writes data to the stream.
  - **`await writer.drain()`**: Waits until it's appropriate to resume writing.

**Detailed Explanation**:

- **Simplified Networking**:

  - The Streams API abstracts away the details of protocols and transports.
  - Provides an interface similar to file I/O, making it more accessible.

- **Use Cases**:

  - Implementing clients and servers without dealing with low-level details.
  - Prototyping network applications quickly.

**Importance for Developers**:

- Highly relevant for end-user developers working on network applications.
- Offers a balance between simplicity and functionality.


## 3. Focusing on Essential Tiers for End-User Developers 🎯

As an end-user developer, you can focus on the following tiers:

- **Tier 1: Coroutines and `await`**

  - Fundamental for writing any asynchronous code.

- **Tier 2: Event Loop**

  - Necessary for running and managing your coroutines.

- **Tier 4: Tasks**

  - Important for scheduling and managing concurrent execution of coroutines.

- **Tier 5: Executors and Subprocesses**

  - Allows integration of blocking code and external processes.

- **Tier 6: Asyncio Utilities**

  - Useful for coordinating coroutines and managing shared resources.

- **Tier 9: Streams API**

  - Essential for network communication in a straightforward manner.


## 4. Conclusion 🎉

The **Tower of Asyncio** provides a structured way to understand the `asyncio` module's components, helping you identify which parts are most relevant to your work. By focusing on the essential tiers, you can effectively leverage `asyncio` to write efficient, asynchronous applications without getting overwhelmed by the complexities intended for framework developers.

Understanding the lower tiers (1-2) is critical, as they form the foundation of asynchronous programming. As you move up the tower, you can incorporate additional features like tasks, utilities, and high-level APIs to enhance your applications.


## 5. Additional Resources 📚

- **Official Asyncio Documentation**: [Asyncio — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- **Python Asyncio Tutorial**: [Real Python - Async IO in Python](https://realpython.com/async-io-python/)
- **Understanding the Event Loop**: [Python Docs - Event Loop](https://docs.python.org/3/library/asyncio-eventloop.html)
- **Curio Framework**: [Curio GitHub Repository](https://github.com/dabeaz/curio)
- **Trio Framework**: [Trio Official Website](https://trio.readthedocs.io/en/stable/)
- **Uvloop**: [Uvloop GitHub Repository](https://github.com/MagicStack/uvloop)
- **Asyncio Cheat Sheet**: [Pysheeet - Asyncio](https://www.pythonsheets.com/notes/python-asyncio.html)
- **Dave Beazley's Talk**: [Python Concurrency from the Ground Up: LIVE!](https://www.youtube.com/watch?v=MCs5OvhV9S4)


