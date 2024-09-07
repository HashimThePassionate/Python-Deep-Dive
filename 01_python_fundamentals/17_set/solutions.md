# 🚀 Solutions:

## 1. **Remove Duplicates**

```python
# 🌟 Remove Duplicates from a List Using a Set
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}
```

## 2. **Set Union**

```python
# 🔗 Union of Two Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

## 3. **Set Intersection**

```python
# ⛓️ Intersection of Two Sets
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date"}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {'banana', 'cherry'}
```

## 4. **Set Difference**

```python
# ➖ Difference Between Two Sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2, 3}
```

## 5. **Symmetric Difference**

```python
# 🔄 Symmetric Difference Between Two Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)  # Output: {1, 2, 5, 6}
```

## 6. **Check Subset**

```python
# ✅ Check If One Set is a Subset of Another
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print(is_subset)  # Output: True
```

## 7. **Set Membership**

```python
# 🔍 Check If an Element Exists in a Set
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)  # Output: True
print("orange" in fruits)  # Output: False
```

## 8. **Set Update**

```python
# 🔄 Adding Multiple Items to a Set Using update()
fruits = {"apple", "banana"}
fruits.update(["cherry", "date", "elderberry"])
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'date', 'elderberry'}
```

## 9. **Frozen Set**

```python
# 🧊 Create a Frozen Set and Attempt Modifications
frozen_fruits = frozenset(["apple", "banana", "cherry"])
print(frozen_fruits)  # Output: frozenset({'apple', 'banana', 'cherry'})

# Attempting to add or remove elements will raise an AttributeError
# frozen_fruits.add("date")  # Uncommenting this line will raise an AttributeError
```

## 10. **Remove Common Elements**

```python
# 🗑️ Remove All Elements from Set1 that are Present in Set2
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}
```
