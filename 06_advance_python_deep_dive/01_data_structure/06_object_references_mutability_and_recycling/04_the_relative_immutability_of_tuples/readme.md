# The Relative Immutability of Tuples

## Overview
Tuples, like most Python collections (lists, dicts, sets, etc.), are containers that hold references to objects. If the referenced items are mutable, they may change even if the tuple itself does not. The immutability of tuples refers to the physical contents of the tuple data structure (i.e., the references it holds) and does not extend to the referenced objects.

## Key Points
- Tuples hold references to objects.
- The immutability of a tuple means that the references (or identities) of the items it contains cannot change.
- If a tuple contains a mutable object, the mutable object can change, affecting the overall value of the tuple.

## Example

### Scenario
Let's illustrate the situation where the value of a tuple changes due to changes in a mutable object it references.

#### Example Code:
```python
# Define two tuples containing a mutable object (a list)
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

# t1 and t2 initially compare equal
print(t1 == t2)  # Output: True

# Inspect the identity of the list at t1[-1]
print(id(t1[-1]))  # Example output: 4302515784

# Modify the list in place
t1[-1].append(99)

# Check the value of t1
print(t1)  # Output: (1, 2, [30, 40, 99])

# Inspect the identity of the list at t1[-1] again
print(id(t1[-1]))  # Example output: 4302515784 (same as before)

# t1 and t2 are now different
print(t1 == t2)  # Output: False
```

### Explanation:
1. **Define Tuples**: `t1` and `t2` are defined with identical items, including a mutable list `[30, 40]`.
2. **Initial Comparison**: `t1` and `t2` are compared and found to be equal because their contents are the same.
3. **Inspect Identity**: The identity (memory address) of the list at `t1[-1]` is checked.
4. **Modify List**: The list within `t1` is modified by appending `99` to it.
5. **Check Tuple Value**: After modification, `t1` shows the updated list `[30, 40, 99]`.
6. **Inspect Identity Again**: The identity of the list at `t1[-1]` remains the same, showing that the list itself hasn't changed, only its contents.
7. **Final Comparison**: `t1` and `t2` are compared again and found to be different because the list inside `t1` has changed.

## Important Notes
- **Immutability**: The tuple `t1` itself is immutable; its structure and the references it holds do not change. However, the mutable list inside `t1` can change.
- **Identity vs. Equality**: `t1` and `t2` initially compare equal because their contents are the same. After modifying the list inside `t1`, they compare unequal because their contents differ.

## Implications
- **Hashability**: The relative immutability of tuples affects their hashability. Tuples containing mutable objects are not hashable and cannot be used as dictionary keys.
- **Copying Objects**: When copying an object containing other objects, you need to decide whether to duplicate the inner objects or share them. This depends on whether you need a shallow copy or a deep copy.

### Additional Note
The distinction between equality and identity has further implications when you need to copy an object. A copy is an equal object with a different ID. If an object contains other objects, consider whether to duplicate the inner objects or share them.
