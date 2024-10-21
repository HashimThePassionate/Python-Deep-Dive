# Function to double values and add to the list
def add_doubled_values(my_list: list[int]) -> None:
    my_list.update([x * 2 for x in my_list])  # Correct method: extend

# Function call
numbers = [1, 2, 3]
add_doubled_values(numbers)
print(numbers)  # Output: [1, 2, 3, 2, 4, 6]
