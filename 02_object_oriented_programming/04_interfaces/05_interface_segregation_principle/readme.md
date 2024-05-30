# What is Interface Segregation Principle?
The Interface Segregation Principle (ISP) states that clients should not be forced to depend on interfaces they do not use. In other words, interfaces should be fine-grained and specific to the requirements of the clients that use them, rather than being monolithic and covering all possible behaviors. By segregating interfaces, ISP aims to minimize the coupling between components, promote modularity, and prevent the bloat of unnecessary dependencies, ultimately leading to more maintainable and flexible software systems.

## Example  

Suppose we are designing an interface for different types of documents in a system. We might start with a generic `Document` interface that provides methods for manipulating documents:

```python
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def print_document(self):
        pass
```

However, not all types of documents support the same operations. For example, a simple text document may support opening, closing, and saving, but it may not support printing. On the other hand, a PDF document may support all operations.

Following the Interface Segregation Principle, we can break down the `Document` interface into smaller, more specific interfaces, each catering to a specific type of document:

```python
from abc import ABC, abstractmethod

class Openable(ABC):
    @abstractmethod
    def open(self):
        pass
    
class Closable(ABC):
    @abstractmethod
    def close(self):
        pass
    
class Savable(ABC):
    @abstractmethod
    def save(self):
        pass
    
class Printable(ABC):
    @abstractmethod
    def print_document(self):
        pass
```

Now, we can create concrete document classes that implement only the interfaces relevant to them:

```python
class TextDocument(Openable, Closable, Savable):
    def open(self):
        print("Text document opened")
    
    def close(self):
        print("Text document closed")
    
    def save(self):
        print("Text document saved")

class PDFDocument(Openable, Closable, Savable, Printable):
    def open(self):
        print("PDF document opened")
    
    def close(self):
        print("PDF document closed")
    
    def save(self):
        print("PDF document saved")
    
    def print_document(self):
        print("PDF document printed")
```

In this example:

- `TextDocument` implements `Openable`, `Closable`, and `Savable` interfaces, as it supports opening, closing, and saving operations.
- `PDFDocument` implements `Openable`, `Closable`, `Savable`, and `Printable` interfaces, as it supports all operations including printing.
