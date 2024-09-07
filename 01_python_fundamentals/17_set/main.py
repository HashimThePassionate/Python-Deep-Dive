# Creating a set with curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}


# Creating a set from a list using the set() constructor
my_set = set([1, 2, 3, 3, 4, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}


# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()


# 🍎 Adding an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}


# 🧹 Clearing all elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()

# 📋 Making a shallow copy of the set
fruits = {"apple", "banana", "cherry"}
new_fruits = fruits.copy()
print(new_fruits)  # Output: {'apple', 'banana', 'cherry'}



# ➖ Difference between sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.difference(set2)
print(result)  # Output: {1, 2}




# 🔄 Updating set1 by removing common elements
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}



# 🚫 Discarding an element
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}
fruits.discard("pear")  # Does nothing since "pear" is not in the set



# ⛓️ Intersection of sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print(result)  # Output: {3, 4}


# 🔄 Updating set1 to its intersection with set2
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(set1)  # Output: {3, 4}


# ❌ Checking if sets are disjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True


# ✔️ Checking if set1 is a subset of set2
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: True



# ✔️ Checking if set1 is a superset of set2
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set1.issuperset(set2))  # Output: True



# 🔄 Popping an element from the set
fruits = {"apple", "banana", "cherry"}
item = fruits.pop()
print(item)  # Output: Random element (e.g., 'banana')
print(fruits)  # Output: Remaining set without


# 🗑️ Removing an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}
# fruits.remove("pear")  # Raises KeyError


# 🔄 Symmetric difference between sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 4, 5


# 🔄 Updating set1 to its symmetric difference with set2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}


# 🔗 Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}


# 🔄 Updating set1 with union of set2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}