from collections import deque

class CollectionDemo:
    @staticmethod
    def show():
        # Using a deque as an example of a collection
        collection = deque()

        # Adding elements
        collection.append("a")
        collection.append("b")
        collection.append("c")

        # Add multiple items in one go
        collection.extend(["a", "b", "c"])

        # Getting the size of the collection
        size = len(collection)
        print(f"Size: {size}")

        # Removing an element
        collection.remove("a")
        contains_a = "a" in collection
        print(f"Contains 'a' after removal: {contains_a}")

        # Clearing the collection
        collection.clear()
        is_empty = len(collection) == 0
        print(f"Is collection empty: {is_empty}")

        # Converting to an array (list in Python)
        object_array = list(collection)
        string_array = list(collection)  # Since all elements are strings, this is the same as above

        # Another collection for comparison
        other = deque(["a", "b", "c"])

        # Comparing collections
        print(collection == other)  # This will print False since collection is empty
        print(list(collection) == list(other))  # This will print False

        # Adding elements back for a fair comparison
        collection.extend(["a", "b", "c"])
        print(list(collection) == list(other))  # This will print True

# Running the show method
CollectionDemo.show()
