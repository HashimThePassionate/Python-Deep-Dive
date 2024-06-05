def create_stream_from_collection(collection):
    for item in collection:
        yield item

def create_stream_from_array(array):
    for item in array:
        yield item

def create_stream_from_objects(*objects):
    for item in objects:
        yield item

def generate_random_stream(limit):
    import random
    count = 0
    while count < limit:
        yield random.random()
        count += 1

def generate_iterate_stream(start, step, limit):
    count = 0
    current = start
    while count < limit:
        yield current
        current += step
        count += 1

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
