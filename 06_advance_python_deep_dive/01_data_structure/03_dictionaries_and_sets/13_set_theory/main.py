l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
unique_items = set(l)
print(unique_items)  # Output: {'eggs', 'spam', 'bacon'}

# Convert back to list if needed
unique_list = list(unique_items)
print(unique_list)  # Output: ['eggs', 'spam', 'bacon']


ordered_unique = list(dict.fromkeys(l).keys())
print(ordered_unique)  # Output: ['spam', 'eggs', 'bacon']


# Attempting to create a set with another set as an element (this will fail)
# try:
#     s = {1, 2, {3, 4}}
# except TypeError as e:
#     print(e)  # Output: unhashable type: 'set'

# Using frozenset instead
s = {1, 2, frozenset({3, 4})}
print(s)  # Output: {1, 2, frozenset({3, 4})}

# Creating a frozenset
fs = frozenset([1, 2, 3])
print(fs)  # Output: frozenset({1, 2, 3})




# Defining the lists
haystack = [
    "alice@example.com", "bob@example.com", "carol@example.com",
    "dave@example.com", "eve@example.com", "bob@example.com",
    "alice@example.com", "frank@example.com", "grace@example.com"
]

needles = ["bob@example.com", "alice@example.com", "eve@example.com", "mallory@example.com"]

# Using set operations
haystack_set = set(haystack)
needles_set = set(needles)

# Count occurrences using set intersection
found = len(needles_set & haystack_set)
print(f"Number of needles found in haystack: {found}")

# Without using set operations (for comparison)
found = 0
for needle in needles:
    if needle in haystack_set:  # Checking in the set for efficiency
        found += 1

print(f"Number of needles found in haystack (without set operations): {found}")

# Using set intersection with conversion
found = len(set(needles) & set(haystack))
print(f"Number of needles found in haystack (with on-the-fly conversion): {found}")

# Using the .intersection method
found = len(set(needles).intersection(haystack))
print(f"Number of needles found in haystack (using .intersection method): {found}")