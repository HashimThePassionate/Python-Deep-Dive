# Generators Functions

### Function Definitions

#### 1. `create_stream_from_collection(collection)`
This generator function takes a collection (like a list) and yields each element one by one.

```python
def create_stream_from_collection(collection):
    for item in collection:
        yield item
```

- **Input:** A collection (e.g., a list `[1, 2, 3, 4, 5]`).
- **Operation:** Iterates through the collection.
- **Output:** Yields each element of the collection.

#### 2. `create_stream_from_array(array)`
This generator function takes an array and yields each element one by one.

```python
def create_stream_from_array(array):
    for item in array:
        yield item
```

- **Input:** An array (e.g., `[1, 2, 3]`).
- **Operation:** Iterates through the array.
- **Output:** Yields each element of the array.

#### 3. `create_stream_from_objects(*objects)`
This generator function takes an arbitrary number of objects and yields each one.

```python
def create_stream_from_objects(*objects):
    for item in objects:
        yield item
```

- **Input:** Arbitrary number of objects (e.g., `1, 2, 3`).
- **Operation:** Iterates through the objects.
- **Output:** Yields each object.

#### 4. `generate_random_stream(limit)`
This generator function yields a specified number of random numbers.

```python
def generate_random_stream(limit):
    import random
    count = 0
    while count < limit:
        yield random.random()
        count += 1
```

- **Input:** A limit (e.g., `3`).
- **Operation:** Generates random numbers using `random.random()`.
- **Output:** Yields random numbers until the specified limit is reached.

#### 5. `generate_iterate_stream(start, step, limit)`
This generator function yields numbers starting from a given value, incremented by a specified step, up to a given limit.

```python
def generate_iterate_stream(start, step, limit):
    count = 0
    current = start
    while count < limit:
        yield current
        current += step
        count += 1
```

- **Input:** A starting value (`start`), an increment step (`step`), and a limit (`limit`).
- **Operation:** Generates numbers starting from `start`, incremented by `step`.
- **Output:** Yields numbers until the specified limit is reached.

### The `show` Function

The `show` function demonstrates the usage of the above generator functions, mimicking the behavior of the `CreatingStreamsDemo` class in Java.

```python
def show():
    # From a collection
    print("Stream from collection:")
    collection = [1, 2, 3, 4, 5]
    for n in create_stream_from_collection(collection):
        print(n)

    # From an array
    print("\nStream from array:")
    array = [1, 2, 3]
    for n in create_stream_from_array(array):
        print(n)

    # From an arbitrary number of objects
    print("\nStream from objects:")
    for n in create_stream_from_objects(1, 2, 3):
        print(n)

    # Generate from scratch (random numbers)
    print("\nStream from random numbers:")
    for n in generate_random_stream(3):
        print(n)

    # Generate from scratch (iterate)
    print("\nStream from iterated numbers:")
    for n in generate_iterate_stream(1, 1, 10):
        print(n)

if __name__ == "__main__":
    show()
```

### Breakdown of `show` Function:

1. **Stream from Collection:**
   - Creates a collection `[1, 2, 3, 4, 5]`.
   - Uses `create_stream_from_collection` to iterate and print each element.

2. **Stream from Array:**
   - Creates an array `[1, 2, 3]`.
   - Uses `create_stream_from_array` to iterate and print each element.

3. **Stream from Objects:**
   - Uses `create_stream_from_objects` with objects `1, 2, 3`.
   - Iterates and prints each object.

4. **Stream from Random Numbers:**
   - Uses `generate_random_stream(3)` to generate 3 random numbers.
   - Iterates and prints each random number.

5. **Stream from Iterated Numbers:**
   - Uses `generate_iterate_stream(1, 1, 10)` to generate numbers starting from 1, incremented by 1, up to 10 numbers.
   - Iterates and prints each number.

### Execution
The `if __name__ == "__main__":` block ensures that `show()` is called only when the script is executed directly, not when imported as a module.

This setup effectively mimics Java Streams using Python generators, showcasing how to process collections, arrays, arbitrary objects, and generate data on the fly in a lazy and efficient manner.