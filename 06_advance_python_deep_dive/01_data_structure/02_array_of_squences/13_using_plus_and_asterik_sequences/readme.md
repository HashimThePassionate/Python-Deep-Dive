# Using + and * with Sequences

Python allows sequences to be combined and repeated using the `+` and `*` operators. These operations are intuitive for Python programmers and always result in the creation of a new sequence, leaving the original sequences unmodified.

## Concatenation with +

The `+` operator concatenates sequences of the same type to create a new sequence.

### Example
```python
l = [1, 2, 3]
l2 = [4, 5, 6]
result = l + l2
print(result)  # Output: [1, 2, 3, 4, 5, 6]
```

## Repetition with *

The `*` operator repeats a sequence a specified number of times to create a new sequence.

### Example
```python
l = [1, 2, 3]
repeated = l * 5
print(repeated)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

string_repeated = 5 * 'abcd'
print(string_repeated)  # Output: 'abcdabcdabcdabcdabcd'
```

## Important Notes

- Both `+` and `*` always create a new sequence object and do not modify the original operands.
- Be cautious when using `*` with sequences containing mutable items.

## Pitfall: Mutable Items in Sequences

Using the `*` operator with sequences containing mutable items can lead to unexpected results. For instance, initializing a list of lists with `my_list = [[]] * 3` creates a list with three references to the same inner list, which is usually not the desired outcome.

### Example
```python
my_list = [[]] * 3
print(my_list)  # Output: [[], [], []]

my_list[0].append(1)
print(my_list)  # Output: [[1], [1], [1]]
```

In this example, appending an element to one of the inner lists affects all the inner lists because they are all references to the same list.

## Summary

- Use `+` for concatenating sequences.
- Use `*` for repeating sequences.
- Be aware of the behavior when working with sequences containing mutable items to avoid unintended side effects.

The next section will cover the pitfalls of using `*` to initialize a list of lists.