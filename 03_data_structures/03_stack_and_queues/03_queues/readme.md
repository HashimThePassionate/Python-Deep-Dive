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

#  **Python List-Based Queues** 📋

## 🖼️ Figure 5.13: Enqueue Operation on the Queue

<div align="center">
  <img src="./images/03.jpg" alt="" width="500px"/>

*Figure 5.13: Example of an enqueue operation on the queue*

</div>

### Step-by-Step (Enqueue):

1. **Start with an empty queue (array of size 6):**

   * `head/front` and `tail/rear` both point to index 0.

2. **Enqueue 3:**

   * Place `3` at index 0.
   * Move `tail/rear` to index 1.

3. **Enqueue 11:**

   * Place `11` at index 1.
   * Move `tail/rear` to index 2.

4. **Enqueue 7:**

   * Place `7` at index 2.
   * Move `tail/rear` to index 3.

**The queue now contains:** `[3, 11, 7]` (with `head` at index 0 and `tail` at index 3).

## 🖼️ Figure 5.14: Dequeue Operation on the Queue

<div align="center">
  <img src="./images/04.jpg" alt="" width="500px"/>

  
*Figure 5.14: Example of a dequeue operation on a queue*

</div>

### Step-by-Step (Dequeue):

1. **Start with a filled queue:**
   `[3, 11, 7, 1, 4, 2]`

   * `head/front` at index 0, `tail/rear` at index 5.

2. **Dequeue 3:**

   * Remove `3` from the front.
   * Move `head/front` to index 1.

3. **Dequeue 11:**

   * Remove `11` from the new front.
   * Move `head/front` to index 2.

4. **Dequeue 7:**

   * Remove `7`.
   * Move `head/front` to index 3.

**The queue now contains:** `[1, 4, 2]`


## 🐍 ListQueue: A Python List-Based Queue Class

Let's see how we implement a simple queue using Python's built-in list:

```python
class ListQueue:
    def __init__(self):
        self.items = []
        self.front = self.rear = 0
        self.size = 3  # Maximum capacity of the queue
```

* **`items`**: Holds the queue data.
* **`front` and `rear`**: Track the head and tail.
* **`size`**: Maximum number of items.

## ➕ Enqueue Operation

The `enqueue` operation adds an item at the **end (rear)** of the queue.

```python
def enqueue(self, data):
    if self.size == self.rear:
        print("\nQueue is full")
    else:
        self.items.append(data)
        self.rear += 1
```

* **Check if queue is full.**
* **If not**, add new data at the rear and move the `rear` pointer ahead.

### Example Usage

```python
q = ListQueue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)     # Should show 'Queue is full'
print(q.items)
```

**Output:**

```
Queue is full
[20, 30, 40]
```

## ➖ Dequeue Operation

The `dequeue` operation removes and returns the item at the **front** of the queue.

```python
def dequeue(self):
    if self.front == self.rear:
        print("Queue is empty")
    else:
        data = self.items.pop(0)  # Remove from front
        self.rear -= 1
        return data
```

* **Check if queue is empty.**
* **If not**, remove the front item (`pop(0)`), move `rear` pointer backward, and return data.

### Example Usage

```python
data = q.dequeue()
print(data)
print(q.items)
```

**Output:**

```
20
[30, 40]
```

> The first element (20) is removed, showing the **FIFO** property.

## ⚠️ Limitation

* The **length of the queue is fixed** with this approach.
* Not suitable for all scenarios; for more flexibility, use linked list-based or dynamic structures.

---

