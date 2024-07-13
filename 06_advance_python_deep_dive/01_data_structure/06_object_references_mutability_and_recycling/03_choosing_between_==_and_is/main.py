# Define the sentinel object
END_OF_DATA = object()
print(END_OF_DATA)  # Output: <object object at 0x7f8b1c7b3b20>
def traverse(node):
    if node is END_OF_DATA:
        return "End of Data"
    return "Processing Node"

# Example usage
node = END_OF_DATA
result = traverse(node)
print(result)  # Output: End of Data

node = "some other node"
result = traverse(node)
print(result)  # Output: Processing Node