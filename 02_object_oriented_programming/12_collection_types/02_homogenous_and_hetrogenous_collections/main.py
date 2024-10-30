from dataclasses import dataclass
from typing import List, Union

# Step 1: Define Data Classes
@dataclass
class Book:
    title: str
    author: str
    isbn: str

@dataclass
class Magazine:
    title: str
    issue_number: int
    publisher: str

@dataclass
class DVD:
    title: str
    director: str
    duration_minutes: int

# Step 2: Define Type Aliases
MediaItem = Union[Book, Magazine, DVD]

# Step 3: Create Homogeneous Collections
books: List[Book] = [
    Book(title="1984", author="George Orwell", isbn="1234567890"),
    Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="0987654321"),
]

magazines: List[Magazine] = [
    Magazine(title="National Geographic", issue_number=202, publisher="National Geographic Society"),
    Magazine(title="TIME", issue_number=105, publisher="Time USA, LLC"),
]

dvds: List[DVD] = [
    DVD(title="Inception", director="Christopher Nolan", duration_minutes=148),
    DVD(title="The Matrix", director="Lana Wachowski", duration_minutes=136),
]

# Step 4: Create a Heterogeneous Collection
library_inventory: List[MediaItem] = books + magazines + dvds

# Step 5: Function to Display Media Information
def display_media_info(media: MediaItem):
    if isinstance(media, Book):
        print(f"Book: {media.title} by {media.author}, ISBN: {media.isbn}")
    elif isinstance(media, Magazine):
        print(f"Magazine: {media.title}, Issue: {media.issue_number}, Publisher: {media.publisher}")
    elif isinstance(media, DVD):
        print(f"DVD: {media.title} directed by {media.director}, Duration: {media.duration_minutes} minutes")

# Step 6: Display Information for All Items in the Library
for item in library_inventory:
    display_media_info(item)
