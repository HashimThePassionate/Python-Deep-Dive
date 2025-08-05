#  **Queues Data Structure** 🚶‍♂️

## 📚 What is a Queue?

A **queue** is a data structure used to store data with special rules for how data is added and removed.
It is very similar to a real-life line (queue) at a shop or bus stop.


## 🖼️ Figure 5.11: Illustration of a Queue

<div align="center">
  <img src="./images/01.jpg" alt="" width="600px"/>

 *Figure 5.11: Illustration of a queue*
</div>


### Explanation:

* Each person stands in line and waits for their turn to be served.
* **Rear/End:** Where new people join the queue.
* **Front:** Where people are served and leave the queue.
* **FIFO (First In, First Out):**
  The first person to join the queue is the first to be served.

## 🔄 Queue Operations

A **queue** works on the **FIFO** principle:

* **First In, First Out:** The element added first will be removed first.

### Key Rules:

1. **Enqueue:** Add new element at the **rear (tail)**.
2. **Dequeue:** Remove element from the **front (head)**.
3. **Peek:** Only the front element can be read (peeked) at any time.

## 🏗️ Queue Implementation (Doubly Linked List)

## 🖼️ Figure 5.12: Queue Using a Linked List

<div align="center">
  <img src="./images/02.jpg" alt="" width="600px"/>

*Figure 5.12: Queue implementation using the stack data structure*

</div>


### Explanation:

* Each node has **data**, a **next** pointer, and a **previous** pointer.
* **Elements are added (enqueued)** at the **tail/rear end**.
* **Elements are removed (dequeued)** from the **head/front end**.
* Only one end is used for enqueue, and the other for dequeue.

> **Good Practice:**
>
> * Always **enqueue** at the **rear end**
> * Always **dequeue** from the **front end**

## 📝 Table: Queue Operations Example

| Queue Operation         | Size | Contents                  | Operation Results                                                          |
| ----------------------- | ---- | ------------------------- | -------------------------------------------------------------------------- |
| `queue()`               | 0    | `[]`                      | Queue object created, which is empty.                                      |
| `enqueue("Muhammad")`      | 1    | `['Muhammad']`               | One item, `Muhammad`, is added to the queue.                                  |
| `enqueue("Hashim")` | 2    | `['Muhammad', 'Hashim']` | One more item, `Hashim`, is added to the queue.                        |
| `size()`                | 2    | `['Muhammad', 'Hashim']` | Returns number of items in queue, which is 2 in this example.              |
| `dequeue()`             | 1    | `['Hashim']`          | The `Muhammad` item is dequeued and returned (added first, removed first).    |
| `dequeue()`             | 0    | `[]`                      | The `Hashim` item is dequeued and returned (added last, removed last). |

*Table 5.2: Illustration of different operations on an example queue*

## ⚙️ How Can Queues Be Implemented in Python?

* Using **Python’s built-in list**
* Using **stacks**
* Using **node-based linked lists**
* Using **Python’s built-in `queue.Queue`**
* Using **`deque` class** from the `collections` module

---

