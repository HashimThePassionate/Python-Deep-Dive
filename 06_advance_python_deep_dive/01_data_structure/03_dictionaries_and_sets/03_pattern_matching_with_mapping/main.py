# Function to get creators from different types of records
def get_creators(record: dict) -> list:
    # Using structural pattern matching to handle different record types
    match record:
        # Case for books with API version 2 and a list of authors
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        # Case for books with API version 1 and a single author
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        # Case for books without the necessary API fields
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        # Case for movies with a director
        case {'type': 'movie', 'director': name}:
            return [name]
        # Default case for invalid records
        case _:
            raise ValueError(f'Invalid record: {record!r}')

# Creating a dictionary for a book with API version 1
b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
# Calling the get_creators function and printing the result
print(get_creators(b1))

from collections import OrderedDict
# Creating an OrderedDict for a book with API version 2
b2 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())
# Calling the get_creators function and printing the result
print(get_creators(b2))

# Calling the get_creators function with an invalid book record
print(get_creators({'type': 'book', 'pages': 770}))

# Creating a dictionary for an ice cream food item
food = dict(category='ice cream', flavor='vanilla', cost=199)
# Using structural pattern matching to handle the food dictionary
match food:
    # Case for ice cream category and capturing other details
    case {'category': 'ice cream', **details}:
        # Printing the captured details of the ice cream
        print(f'Ice cream details: {details}')
