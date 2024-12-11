# 🔄 **The Factory Design Pattern** 🔄

Welcome to the **Factory Design Pattern** guide! 🚀 This document provides an in-depth exploration of the Factory Design Pattern, covering its purpose, importance, various forms (Factory Method and Abstract Factory), and detailed, line-by-line explanations of implementation examples. 💡 All code examples utilize **static typing** to ensure clarity and reliability. 🛠️✨ 

---

## 📖 Table of Contents 📖

- [🔄 **The Factory Design Pattern** 🔄](#-the-factory-design-pattern-)
  - [📖 Table of Contents 📖](#-table-of-contents-)
  - [🔍 Introduction](#-introduction)
    - [📌 Why Use the Factory Pattern?](#-why-use-the-factory-pattern)
  - [💡 What is the Factory Design Pattern?](#-what-is-the-factory-design-pattern)
    - [🎯 Core Idea](#-core-idea)
  - [🏆 Benefits of the Factory Pattern](#-benefits-of-the-factory-pattern)
  - [🛠️ Forms of the Factory Pattern](#️-forms-of-the-factory-pattern)
    - [1. Factory Method](#1-factory-method)
    - [2. Abstract Factory](#2-abstract-factory)
  - [📂 Example: Factory Method Pattern](#-example-factory-method-pattern)
    - [1. Creating Data Extractor Classes](#1-creating-data-extractor-classes)
      - [📝 Explanation:](#-explanation)
    - [2. Implementing the Factory Function](#2-implementing-the-factory-function)
      - [📝 Explanation:](#-explanation-1)
    - [3. Defining the Extraction Logic](#3-defining-the-extraction-logic)
      - [📝 Explanation:](#-explanation-2)
    - [4. Testing the Factory Method Implementation](#4-testing-the-factory-method-implementation)
      - [📝 Explanation:](#-explanation-3)
  - [🧪 Testing the Factory Method Implementation](#-testing-the-factory-method-implementation)
    - [1. Prepare the Data Files](#1-prepare-the-data-files)
    - [2. Save the Implementation Code](#2-save-the-implementation-code)
    - [3. Running the Test](#3-running-the-test)
    - [4. Expected Output](#4-expected-output)
  - [📂 Example: Abstract Factory Pattern](#-example-abstract-factory-pattern)
    - [Scenario: Game Environment with Different Worlds](#scenario-game-environment-with-different-worlds)
    - [1. Defining Game Components](#1-defining-game-components)
      - [FrogWorld Components](#frogworld-components)
      - [WizardWorld Components](#wizardworld-components)
      - [Obstacle Base Class (Optional for Type Hinting)](#obstacle-base-class-optional-for-type-hinting)
    - [📝 Explanation:](#-explanation-4)
    - [2. Creating the Factory Classes](#2-creating-the-factory-classes)
      - [📝 Explanation:](#-explanation-5)
    - [3. Implementing the Game Environment](#3-implementing-the-game-environment)
      - [📝 Explanation:](#-explanation-6)
    - [4. Testing the Abstract Factory Implementation](#4-testing-the-abstract-factory-implementation)
      - [📝 Explanation:](#-explanation-7)
  - [🧪 Testing the Factory Method Implementation](#-testing-the-factory-method-implementation-1)
    - [1. Execute the Script](#1-execute-the-script)
    - [2. Sample Output](#2-sample-output)
    - [3. Verification](#3-verification)
  - [📂 Example: Abstract Factory Pattern](#-example-abstract-factory-pattern-1)
    - [1. Defining Game Components](#1-defining-game-components-1)
      - [FrogWorld Components](#frogworld-components-1)
      - [WizardWorld Components](#wizardworld-components-1)
    - [📝 Explanation:](#-explanation-8)
    - [2. Creating the Factory Classes](#2-creating-the-factory-classes-1)
      - [📝 Explanation:](#-explanation-9)
    - [3. Implementing the Game Environment](#3-implementing-the-game-environment-1)
      - [📝 Explanation:](#-explanation-10)
    - [4. Testing the Abstract Factory Implementation](#4-testing-the-abstract-factory-implementation-1)
      - [📝 Explanation:](#-explanation-11)
  - [🧪 Testing the Abstract Factory Implementation](#-testing-the-abstract-factory-implementation)
    - [1. Execute the Script](#1-execute-the-script-1)
    - [2. Sample Output](#2-sample-output-1)
    - [3. Verification](#3-verification-1)

---

## 🔍 Introduction

The **Factory Design Pattern** is one of the fundamental creational design patterns described by the Gang of Four (GoF) in their seminal book on design patterns. 🛡️ It provides a way to encapsulate object creation logic, allowing clients to create objects without specifying the exact class of the object that will be created. This promotes loose coupling and enhances the flexibility and maintainability of your codebase. 📈

### 📌 Why Use the Factory Pattern?

- **Encapsulation of Object Creation**: Centralizes object creation, making it easier to manage and modify.
- **Loose Coupling**: Reduces dependencies between client code and concrete classes.
- **Enhanced Flexibility**: Facilitates the introduction of new types without altering existing client code.
- **Simplified Object Management**: Makes tracking and managing object creation more straightforward.

---

## 💡 What is the Factory Design Pattern?

The **Factory Design Pattern** is a creational pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. Essentially, it delegates the responsibility of object instantiation to factory classes or methods, enabling more controlled and flexible object creation.

### 🎯 Core Idea

- **Client Code Requests Objects Without Knowing Their Concrete Classes**: Clients interact with interfaces or abstract classes, relying on factories to provide the necessary implementations.
- **Factories Handle the Instantiation Logic**: Encapsulate the decision-making process about which concrete class to instantiate based on input parameters or configuration.

---

## 🏆 Benefits of the Factory Pattern

Implementing the Factory Pattern offers several significant advantages:

- **🔧 Maintainability**: Centralizing object creation logic makes it easier to update and maintain.
- **🛠️ Extensibility**: Adding new object types requires minimal changes to existing code, often limited to the factory.
- **🧪 Testability**: Facilitates testing by allowing the injection of mock objects through the factory.
- **📚 Readability**: Improves code readability by abstracting the instantiation process.
- **🚫 Reduced Coupling**: Decouples client code from concrete classes, promoting a more modular architecture.

---

## 🛠️ Forms of the Factory Pattern

The Factory Pattern comes in two primary forms:

1. **Factory Method**: Uses a single method or function to create objects, often based on input parameters.
2. **Abstract Factory**: Provides a family of related factory methods, allowing the creation of related or dependent objects without specifying their concrete classes.

---

### 1. Factory Method

The **Factory Method** is based on a single function or method responsible for creating objects. Clients call this method, passing parameters that guide the creation process, and receive the desired object without knowing its concrete class.

**Key Characteristics**:

- **Single Responsibility**: The factory method handles object creation, separating it from business logic.
- **Parameter-Based Instantiation**: Decisions about which object to create are based on input parameters.
- **Simplifies Object Creation**: Clients do not need to know the instantiation details of the objects they use.

---

### 2. Abstract Factory

The **Abstract Factory** pattern extends the Factory Method by grouping multiple factory methods into a single class or interface. It is used to create families of related or dependent objects without specifying their concrete classes.

**Key Characteristics**:

- **Multiple Factory Methods**: Provides several methods for creating different types of related objects.
- **Families of Products**: Ensures that related objects are used together, maintaining consistency.
- **Enhanced Flexibility**: Allows for the creation of complex object structures with interdependent components.

---

## 📂 Example: Factory Method Pattern

Let's dive into a practical implementation of the Factory Method pattern using Python. We'll create a scenario where we need to extract data from different file formats (JSON and XML) using separate extractor classes, and centralize the object creation process through a factory function.

### 1. Creating Data Extractor Classes

We'll start by defining two data extractor classes: `JSONDataExtractor` and `XMLDataExtractor`. Each class is responsible for loading and parsing data from its respective file format.

```python
# ch03/factory/factory_method.py

from typing import Protocol
from pathlib import Path
import json
import xml.etree.ElementTree as ET

class DataExtractor(Protocol):
    @property
    def parsed_data(self):
        ...

class JSONDataExtractor:
    def __init__(self, filepath: Path):
        self.data = {}
        with open(filepath) as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLDataExtractor:
    def __init__(self, filepath: Path):
        self.tree = ET.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
```

#### 📝 Explanation:

1. **Imports**:
    - `Protocol` from `typing`: Allows us to define interfaces.
    - `Path` from `pathlib`: Facilitates file path manipulations.
    - `json`: For handling JSON data.
    - `xml.etree.ElementTree` as `ET`: For handling XML data.

2. **DataExtractor Protocol**:
    - Defines a protocol (interface) with a single property `parsed_data`.
    - Any class adhering to this protocol must implement the `parsed_data` property.

3. **JSONDataExtractor Class**:
    - **`__init__` Method**:
        - Accepts a `filepath` of type `Path`.
        - Initializes an empty dictionary `self.data`.
        - Opens and reads the JSON file, loading its content into `self.data`.
    - **`parsed_data` Property**:
        - Returns the loaded JSON data.

4. **XMLDataExtractor Class**:
    - **`__init__` Method**:
        - Accepts a `filepath` of type `Path`.
        - Parses the XML file using `ElementTree` and stores the tree in `self.tree`.
    - **`parsed_data` Property**:
        - Returns the parsed XML tree.

**Key Takeaways**:

- Both extractor classes implement the `parsed_data` property, adhering to the `DataExtractor` protocol.
- Object creation logic is encapsulated within each extractor class.

---

### 2. Implementing the Factory Function

Next, we'll implement the factory function `extract_factory` that decides which extractor class to instantiate based on the file extension.

```python
def extract_factory(filepath: Path) -> DataExtractor:
    ext = filepath.suffix.lower()
    if ext == ".json":
        return JSONDataExtractor(filepath)
    elif ext == ".xml":
        return XMLDataExtractor(filepath)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
```

#### 📝 Explanation:

1. **Function Definition**:
    - `extract_factory` accepts a `filepath` of type `Path` and returns an instance adhering to the `DataExtractor` protocol.

2. **Determining File Extension**:
    - `ext = filepath.suffix.lower()`: Extracts the file extension (e.g., `.json`, `.xml`) and converts it to lowercase for consistency.

3. **Conditional Instantiation**:
    - **If the extension is `.json`**:
        - Instantiates and returns a `JSONDataExtractor` with the provided `filepath`.
    - **Elif the extension is `.xml`**:
        - Instantiates and returns an `XMLDataExtractor` with the provided `filepath`.
    - **Else**:
        - Raises a `ValueError` indicating an unsupported file extension.

**Key Takeaways**:

- The factory function abstracts away the instantiation details, allowing clients to request data extractors without knowing the underlying classes.
- It centralizes object creation, making it easier to manage and extend in the future.

---

### 3. Defining the Extraction Logic

We'll define the `extract` function that uses the factory to obtain the appropriate extractor and processes the data accordingly.

```python
def extract(case: str) -> None:
    dir_path = Path(__file__).parent
    if case == "json":
        path = dir_path / "movies.json"
        factory = extract_factory(path)
        data = factory.parsed_data
        for movie in data:
            print(f"- {movie['title']}")
            director = movie.get("director")
            if director:
                print(f"  Director: {director}")
            genre = movie.get("genre")
            if genre:
                print(f"  Genre: {genre}")
    elif case == "xml":
        path = dir_path / "person.xml"
        factory = extract_factory(path)
        data = factory.parsed_data
        search_xpath = ".//person[lastName='Liar']"
        items = data.findall(search_xpath)
        for item in items:
            first = item.find("firstName").text
            last = item.find("lastName").text
            print(f"- {first} {last}")
            for pn in item.find("phoneNumbers"):
                pn_type = pn.attrib.get("type", "unknown")
                pn_val = pn.text
                phone = f"  {pn_type}: {pn_val}"
                print(phone)
    else:
        print(f"Unknown case: {case}")
```

#### 📝 Explanation:

1. **Function Definition**:
    - `extract` accepts a `case` string (`"json"` or `"xml"`) and returns nothing (`None`).

2. **Determining Directory Path**:
    - `dir_path = Path(__file__).parent`: Gets the directory where the current script resides, ensuring relative file paths are correctly resolved.

3. **Handling JSON Case**:
    - **Condition**: `if case == "json":`
    - **Path Definition**: `path = dir_path / "movies.json"`
        - Constructs the path to the `movies.json` file within the same directory.
    - **Factory Usage**: `factory = extract_factory(path)`
        - Uses the factory to obtain a `JSONDataExtractor` instance.
    - **Data Extraction**: `data = factory.parsed_data`
        - Retrieves the parsed JSON data.
    - **Processing Data**:
        - Iterates over each `movie` in `data`.
        - **Printing Title**: `print(f"- {movie['title']}")`
        - **Optional Director and Genre**:
            - Uses `get` to safely access `director` and `genre` fields.
            - If present, prints them with indentation for readability.

4. **Handling XML Case**:
    - **Condition**: `elif case == "xml":`
    - **Path Definition**: `path = dir_path / "person.xml"`
        - Constructs the path to the `person.xml` file within the same directory.
    - **Factory Usage**: `factory = extract_factory(path)`
        - Uses the factory to obtain an `XMLDataExtractor` instance.
    - **Data Extraction**: `data = factory.parsed_data`
        - Retrieves the parsed XML tree.
    - **Defining Search Criteria**:
        - `search_xpath = ".//person[lastName='Liar']"`
            - XPath expression to find all `<person>` elements with `<lastName>` equal to `'Liar'`.
    - **Finding Elements**: `items = data.findall(search_xpath)`
        - Finds all matching `<person>` elements.
    - **Processing Data**:
        - Iterates over each `item` in `items`.
        - **Extracting Names**:
            - Retrieves `firstName` and `lastName` texts.
            - Prints them in a formatted string.
        - **Extracting Phone Numbers**:
            - Iterates over each `<number>` element within `<phoneNumbers>`.
            - Retrieves `type` attribute and text content.
            - Prints them with indentation.

5. **Handling Unknown Cases**:
    - **Condition**: `else:`
    - **Action**: Prints an error message indicating an unknown case.

**Key Takeaways**:

- The `extract` function demonstrates how client code interacts with the factory to obtain the necessary extractor.
- It processes different data formats uniformly by relying on the `DataExtractor` interface.
- Centralizing the extraction logic enhances maintainability and extensibility.

---

### 4. Testing the Factory Method Implementation

We'll add a test script to verify that our Factory Method pattern works as expected. This script will call the `extract` function for both JSON and XML cases.

```python
if __name__ == "__main__":
    print("* JSON case *")
    extract(case="json")
    print("* XML case *")
    extract(case="xml")
```

#### 📝 Explanation:

1. **Entry Point Check**:
    - `if __name__ == "__main__":`
        - Ensures that the following code runs only when the script is executed directly, not when imported as a module.

2. **Testing JSON Case**:
    - `print("* JSON case *")`: Prints a header indicating the JSON test case.
    - `extract(case="json")`: Calls the `extract` function with `"json"` to process the `movies.json` file.

3. **Testing XML Case**:
    - `print("* XML case *")`: Prints a header indicating the XML test case.
    - `extract(case="xml")`: Calls the `extract` function with `"xml"` to process the `person.xml` file.

**Key Takeaways**:

- The test script demonstrates the usage of the Factory Method pattern by processing different data formats through the same interface.
- It validates that the factory correctly instantiates the appropriate extractor based on the file extension.

---

## 🧪 Testing the Factory Method Implementation

To ensure that our Factory Method pattern implementation works correctly, follow these steps:

### 1. Prepare the Data Files

Ensure that you have the following data files in the same directory as your `factory_method.py` script:

- **movies.json**: A JSON file containing a list of movie entries.
- **person.xml**: An XML file containing information about individuals.

**Example Content**:

**movies.json**:
```json
[
    {
        "title": "After Dark in Central Park",
        "year": 1900,
        "director": null,
        "cast": null,
        "genre": null
    },
    {
        "title": "Boarding School Girls' Pajama Parade",
        "year": 1900,
        "director": null,
        "cast": null,
        "genre": null
    },
    {
        "title": "Buffalo Bill's Wild West Parad",
        "year": 1900,
        "director": null,
        "cast": null,
        "genre": null
    },
    {
        "title": "Caught",
        "year": 1900,
        "director": null,
        "cast": null,
        "genre": null
    },
    {
        "title": "Clowns Spinning Hats",
        "year": 1900,
        "director": null,
        "cast": null,
        "genre": null
    },
    {
        "title": "Capture of Boer Battery by British",
        "year": 1900,
        "director": "James H. White",
        "cast": null,
        "genre": "Short documentary"
    },
    {
        "title": "The Enchanted Drawing",
        "year": 1900,
        "director": "J. Stuart Blackton",
        "cast": null,
        "genre": null
    },
    {
        "title": "Family Troubles",
        "year": 1900,
        "director": null,
        "cast": null,
        "genre": null
    },
    {
        "title": "Feeding Sea Lions",
        "year": 1900,
        "director": null,
        "cast": "Paul Boyton",
        "genre": null
    }
]
```

**person.xml**:
```xml
<persons>
    <person>
        <firstName>John</firstName>
        <lastName>Smith</lastName>
        <age>25</age>
        <address>
            <streetAddress>21 2nd Street</streetAddress>
            <city>New York</city>
            <state>NY</state>
            <postalCode>10021</postalCode>
        </address>
        <phoneNumbers>
            <number type="home">212 555-1234</number>
            <number type="fax">646 555-4567</number>
        </phoneNumbers>
        <gender>
            <type>male</type>
        </gender>
    </person>
    <person>
        <firstName>Jimy</firstName>
        <lastName>Liar</lastName>
        <age>19</age>
        <address>
            <streetAddress>18 2nd Street</streetAddress>
            <city>New York</city>
            <state>NY</state>
            <postalCode>10021</postalCode>
        </address>
        <phoneNumbers>
            <number type="home">212 555-1234</number>
        </phoneNumbers>
        <gender>
            <type>male</type>
        </gender>
    </person>
    <person>
        <firstName>Patty</firstName>
        <lastName>Liar</lastName>
        <age>20</age>
        <address>
            <streetAddress>18 2nd Street</streetAddress>
            <city>New York</city>
            <state>NY</state>
            <postalCode>10021</postalCode>
        </address>
        <phoneNumbers>
            <number type="home">212 555-1234</number>
            <number type="mobile">001 452-8819</number>
        </phoneNumbers>
        <gender>
            <type>female</type>
        </gender>
    </person>
</persons>
```

### 2. Save the Implementation Code

Save the following implementation code in a file named `factory_method.py` within the `ch03/factory/` directory.

```python
# ch03/factory/factory_method.py

from typing import Protocol
from pathlib import Path
import json
import xml.etree.ElementTree as ET

class DataExtractor(Protocol):
    @property
    def parsed_data(self):
        ...

class JSONDataExtractor:
    def __init__(self, filepath: Path):
        self.data = {}
        with open(filepath) as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLDataExtractor:
    def __init__(self, filepath: Path):
        self.tree = ET.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

def extract_factory(filepath: Path) -> DataExtractor:
    ext = filepath.suffix.lower()
    if ext == ".json":
        return JSONDataExtractor(filepath)
    elif ext == ".xml":
        return XMLDataExtractor(filepath)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def extract(case: str) -> None:
    dir_path = Path(__file__).parent
    if case == "json":
        path = dir_path / "movies.json"
        factory = extract_factory(path)
        data = factory.parsed_data
        for movie in data:
            print(f"- {movie['title']}")
            director = movie.get("director")
            if director:
                print(f"  Director: {director}")
            genre = movie.get("genre")
            if genre:
                print(f"  Genre: {genre}")
    elif case == "xml":
        path = dir_path / "person.xml"
        factory = extract_factory(path)
        data = factory.parsed_data
        search_xpath = ".//person[lastName='Liar']"
        items = data.findall(search_xpath)
        for item in items:
            first = item.find("firstName").text
            last = item.find("lastName").text
            print(f"- {first} {last}")
            for pn in item.find("phoneNumbers"):
                pn_type = pn.attrib.get("type", "unknown")
                pn_val = pn.text
                phone = f"  {pn_type}: {pn_val}"
                print(phone)
    else:
        print(f"Unknown case: {case}")

if __name__ == "__main__":
    print("* JSON case *")
    extract(case="json")
    print("* XML case *")
    extract(case="xml")
```

### 3. Running the Test

Open your terminal, navigate to the directory containing `factory_method.py`, and execute the following command:

```bash
python3.12 ch03/factory/factory_method.py
```

### 4. Expected Output

You should see output similar to the following:

```
* JSON case *
- After Dark in Central Park
- Boarding School Girls' Pajama Parade
- Buffalo Bill's Wild West Parad
- Caught
- Clowns Spinning Hats
- Capture of Boer Battery by British
  Director: James H. White
  Genre: Short documentary
- The Enchanted Drawing
  Director: J. Stuart Blackton
- Family Troubles
- Feeding Sea Lions
* XML case *
- Jimy Liar
  home: 212 555-1234
- Patty Liar
  home: 212 555-1234
  mobile: 001 452-8819
```

**Note**: The actual output may vary based on the contents of your `movies.json` and `person.xml` files.

**Key Observations**:

- **JSON Case**:
    - Lists movie titles, directors (if available), and genres (if available).
- **XML Case**:
    - Lists individuals with the last name "Liar" and their phone numbers.

**Conclusion**:

This demonstrates that the Factory Method pattern successfully abstracts the creation of different data extractors (`JSONDataExtractor` and `XMLDataExtractor`). Clients can request data extraction without knowing the underlying implementation details, promoting a clean and maintainable codebase.

---

## 📂 Example: Abstract Factory Pattern

The **Abstract Factory** pattern is a generalization of the Factory Method pattern. It provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is particularly useful when a system needs to work with multiple families of related objects, and the exact types may vary.

### Scenario: Game Environment with Different Worlds

We'll create a simple game environment where players can enter different worlds (e.g., FrogWorld for children and WizardWorld for adults). Each world has its own set of characters and obstacles. The Abstract Factory will manage the creation of these components, allowing the game to switch between different worlds seamlessly.

### 1. Defining Game Components

We'll start by defining the core components of our game: characters and obstacles.

#### FrogWorld Components

```python
class Frog:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: "Obstacle") -> None:
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)

class Bug:
    def __str__(self) -> str:
        return "a bug"

    def action(self) -> str:
        return "eats it"
```

#### WizardWorld Components

```python
class Wizard:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: "Obstacle") -> None:
        act = obstacle.action()
        msg = f"{self} the Wizard battles against {obstacle} and {act}!"
        print(msg)

class Ork:
    def __str__(self) -> str:
        return "an evil ork"

    def action(self) -> str:
        return "kills it"
```

#### Obstacle Base Class (Optional for Type Hinting)

```python
from abc import ABC, abstractmethod

class Obstacle(ABC):
    @abstractmethod
    def action(self) -> str:
        pass
```

### 📝 Explanation:

1. **Frog Class**:
    - **`__init__` Method**:
        - Initializes the frog's `name`.
    - **`__str__` Method**:
        - Returns the frog's name for readable string representation.
    - **`interact_with` Method**:
        - Takes an `Obstacle` instance.
        - Calls the obstacle's `action` method.
        - Prints a message describing the interaction.

2. **Bug Class**:
    - **`__str__` Method**:
        - Returns a string representation of the bug.
    - **`action` Method**:
        - Returns the action "eats it".

3. **Wizard Class**:
    - Similar structure to the `Frog` class but tailored for a wizard.
    - **`interact_with` Method**:
        - Describes a battle against an obstacle.

4. **Ork Class**:
    - Represents an enemy in the wizard world.
    - **`action` Method**:
        - Returns the action "kills it".

5. **Obstacle Abstract Base Class (Optional)**:
    - Defines an abstract `action` method to enforce a contract for all obstacles.
    - Useful for type hinting and ensuring consistency across obstacle implementations.

---

### 2. Creating the Factory Classes

We'll create two factory classes: `FrogWorld` and `WizardWorld`. Each factory is responsible for creating its respective characters and obstacles.

```python
class FrogWorld:
    def __init__(self, name: str):
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return "\n\n\t------ Frog World -------"

    def make_character(self) -> Frog:
        return Frog(self.player_name)

    def make_obstacle(self) -> Bug:
        return Bug()

class WizardWorld:
    def __init__(self, name: str):
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return "\n\n\t------ Wizard World -------"

    def make_character(self) -> Wizard:
        return Wizard(self.player_name)

    def make_obstacle(self) -> Ork:
        return Ork()
```

#### 📝 Explanation:

1. **FrogWorld Class**:
    - **`__init__` Method**:
        - Accepts the player's `name`.
        - Prints the world name using the `__str__` method.
    - **`__str__` Method**:
        - Returns a string representing the Frog World.
    - **`make_character` Method**:
        - Creates and returns a `Frog` instance with the player's name.
    - **`make_obstacle` Method**:
        - Creates and returns a `Bug` instance.

2. **WizardWorld Class**:
    - **`__init__` Method**:
        - Similar to `FrogWorld`, initializes with the player's `name` and prints the world name.
    - **`__str__` Method**:
        - Returns a string representing the Wizard World.
    - **`make_character` Method**:
        - Creates and returns a `Wizard` instance with the player's name.
    - **`make_obstacle` Method**:
        - Creates and returns an `Ork` instance.

**Key Takeaways**:

- Each factory class encapsulates the creation logic for its specific world.
- Clients interact with the factories to obtain characters and obstacles without knowing the concrete classes involved.

---

### 3. Implementing the Game Environment

We'll define the `GameEnvironment` class, which serves as the main entry point for the game. It utilizes the factory to create game components and initiates interactions between characters and obstacles.

```python
class GameEnvironment:
    def __init__(self, factory: object):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self) -> None:
        self.hero.interact_with(self.obstacle)
```

#### 📝 Explanation:

1. **`GameEnvironment` Class**:
    - **`__init__` Method**:
        - Accepts a `factory` object (either `FrogWorld` or `WizardWorld`).
        - Uses the factory to create a `hero` by calling `make_character()`.
        - Uses the factory to create an `obstacle` by calling `make_obstacle()`.
    - **`play` Method**:
        - Initiates the interaction between the `hero` and the `obstacle` by calling `hero.interact_with(obstacle)`.

**Key Takeaways**:

- `GameEnvironment` depends on the abstract interface provided by the factory, not on concrete classes.
- It orchestrates the game flow by utilizing the components created by the factory.

---

### 4. Testing the Abstract Factory Implementation

We'll implement the main function that sets up the game environment based on user input (player's name and age) and decides which factory to use (FrogWorld or WizardWorld).

```python
def validate_age(name: str) -> tuple[bool, int]:
    age = None
    try:
        age_input = input(f"Welcome {name}. How old are you? ")
        age = int(age_input)
    except ValueError:
        print(f"Age {age_input} is invalid, please try again...")
        return False, age
    return True, age

def main() -> None:
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(factory=game(name))
    environment.play()

if __name__ == "__main__":
    main()
```

#### 📝 Explanation:

1. **`validate_age` Function**:
    - **Parameters**: `name` (str) - the player's name.
    - **Returns**: A tuple containing a boolean indicating validity and the age (int).
    - **Functionality**:
        - Prompts the user to input their age.
        - Attempts to convert the input to an integer.
        - If successful, returns `(True, age)`.
        - If a `ValueError` occurs (invalid input), prints an error message and returns `(False, age)`.

2. **`main` Function**:
    - **Functionality**:
        - Prompts the user for their name.
        - Initializes `valid_input` as `False`.
        - Enters a loop that continues until a valid age is provided.
        - Calls `validate_age(name)` to get the validity and age.
        - **Determining the Game**:
            - If `age < 18`, selects `FrogWorld` for children.
            - Else, selects `WizardWorld` for adults.
        - **Creating the Game Environment**:
            - Instantiates the selected factory with the player's name.
            - Passes the factory to `GameEnvironment`.
        - **Starting the Game**:
            - Calls `environment.play()` to initiate the interaction between the hero and the obstacle.

3. **Entry Point Check**:
    - `if __name__ == "__main__": main()`
        - Ensures that the `main` function runs only when the script is executed directly.

**Key Takeaways**:

- User input determines which factory is used, showcasing the Factory Pattern's flexibility.
- The game environment remains decoupled from the specific factories, relying only on the abstract interfaces they provide.

---

## 🧪 Testing the Factory Method Implementation

Let's run the `factory_method.py` script to observe how the Factory Method pattern works in practice.

### 1. Execute the Script

Run the following command in your terminal:

```bash
python3.12 ch03/factory/factory_method.py
```

### 2. Sample Output

**JSON Case**:
```
* JSON case *
- After Dark in Central Park
- Boarding School Girls' Pajama Parade
- Buffalo Bill's Wild West Parad
- Caught
- Clowns Spinning Hats
- Capture of Boer Battery by British
  Director: James H. White
  Genre: Short documentary
- The Enchanted Drawing
  Director: J. Stuart Blackton
- Family Troubles
- Feeding Sea Lions
```

**XML Case**:
```
* XML case *
- Jimy Liar
  home: 212 555-1234
- Patty Liar
  home: 212 555-1234
  mobile: 001 452-8819
```

### 3. Verification

- **JSON Output**:
    - Lists movie titles.
    - Displays director and genre information where available.
- **XML Output**:
    - Lists individuals with the last name "Liar".
    - Shows their phone numbers categorized by type.

**Conclusion**:

The output confirms that the Factory Method pattern effectively abstracts the creation of different data extractors. The client code (`extract` function) interacts with the factory to obtain the appropriate extractor based on the file extension, without needing to know the underlying implementation details.

---

## 📂 Example: Abstract Factory Pattern

Now, let's explore the **Abstract Factory** pattern through a more complex example involving game environments. This pattern allows the creation of related objects without specifying their concrete classes, making it ideal for scenarios where a system needs to handle multiple families of related objects.

### 1. Defining Game Components

We'll define two separate worlds: `FrogWorld` for children and `WizardWorld` for adults. Each world has its own set of characters and obstacles.

#### FrogWorld Components

```python
class Frog:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: "Obstacle") -> None:
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)

class Bug:
    def __str__(self) -> str:
        return "a bug"

    def action(self) -> str:
        return "eats it"
```

#### WizardWorld Components

```python
class Wizard:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle: "Obstacle") -> None:
        act = obstacle.action()
        msg = f"{self} the Wizard battles against {obstacle} and {act}!"
        print(msg)

class Ork:
    def __str__(self) -> str:
        return "an evil ork"

    def action(self) -> str:
        return "kills it"
```

### 📝 Explanation:

These classes define the characters (`Frog` and `Wizard`) and their respective obstacles (`Bug` and `Ork`). Each character has an `interact_with` method that defines how they interact with obstacles.

---

### 2. Creating the Factory Classes

We'll create two factory classes: `FrogWorld` and `WizardWorld`. Each factory will be responsible for creating its respective character and obstacle.

```python
class FrogWorld:
    def __init__(self, name: str):
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return "\n\n\t------ Frog World -------"

    def make_character(self) -> Frog:
        return Frog(self.player_name)

    def make_obstacle(self) -> Bug:
        return Bug()

class WizardWorld:
    def __init__(self, name: str):
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return "\n\n\t------ Wizard World -------"

    def make_character(self) -> Wizard:
        return Wizard(self.player_name)

    def make_obstacle(self) -> Ork:
        return Ork()
```

#### 📝 Explanation:

1. **FrogWorld Class**:
    - **`__init__` Method**:
        - Accepts the player's `name`.
        - Prints the world name using the `__str__` method.
    - **`__str__` Method**:
        - Returns a string indicating the Frog World.
    - **`make_character` Method**:
        - Creates and returns a `Frog` instance with the player's name.
    - **`make_obstacle` Method**:
        - Creates and returns a `Bug` instance.

2. **WizardWorld Class**:
    - **`__init__` Method**:
        - Similar to `FrogWorld`, initializes with the player's `name` and prints the world name.
    - **`__str__` Method**:
        - Returns a string indicating the Wizard World.
    - **`make_character` Method**:
        - Creates and returns a `Wizard` instance with the player's name.
    - **`make_obstacle` Method**:
        - Creates and returns an `Ork` instance.

**Key Takeaways**:

- Each factory class encapsulates the creation logic for its specific world.
- This setup allows for easy addition of new worlds by creating new factory classes without modifying existing ones.

---

### 3. Implementing the Game Environment

We'll define the `GameEnvironment` class, which serves as the main entry point for the game. It utilizes the abstract factory to create game components and initiates interactions between characters and obstacles.

```python
class GameEnvironment:
    def __init__(self, factory: object):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self) -> None:
        self.hero.interact_with(self.obstacle)
```

#### 📝 Explanation:

1. **`GameEnvironment` Class**:
    - **`__init__` Method**:
        - Accepts a `factory` object (either `FrogWorld` or `WizardWorld`).
        - Uses the factory to create a `hero` by calling `make_character()`.
        - Uses the factory to create an `obstacle` by calling `make_obstacle()`.
    - **`play` Method**:
        - Initiates the interaction between the `hero` and the `obstacle` by calling `hero.interact_with(obstacle)`.

**Key Takeaways**:

- `GameEnvironment` relies on the abstract factory to obtain the necessary game components.
- It remains agnostic of the concrete classes, promoting flexibility and extensibility.

---

### 4. Testing the Abstract Factory Implementation

We'll implement the main function that sets up the game environment based on user input (player's name and age) and decides which factory to use (FrogWorld or WizardWorld).

```python
def validate_age(name: str) -> tuple[bool, int]:
    age = None
    try:
        age_input = input(f"Welcome {name}. How old are you? ")
        age = int(age_input)
    except ValueError:
        print(f"Age {age_input} is invalid, please try again...")
        return False, age
    return True, age

def main() -> None:
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(factory=game(name))
    environment.play()

if __name__ == "__main__":
    main()
```

#### 📝 Explanation:

1. **`validate_age` Function**:
    - **Parameters**: `name` (str) - the player's name.
    - **Returns**: A tuple containing a boolean indicating validity and the age (int).
    - **Functionality**:
        - Prompts the user to input their age.
        - Attempts to convert the input to an integer.
        - If successful, returns `(True, age)`.
        - If a `ValueError` occurs (invalid input), prints an error message and returns `(False, age)`.

2. **`main` Function**:
    - **Functionality**:
        - Prompts the user for their name.
        - Initializes `valid_input` as `False`.
        - Enters a loop that continues until a valid age is provided.
        - Calls `validate_age(name)` to get the validity and age.
        - **Determining the Game**:
            - If `age < 18`, selects `FrogWorld` for children.
            - Else, selects `WizardWorld` for adults.
        - **Creating the Game Environment**:
            - Instantiates the selected factory with the player's name.
            - Passes the factory to `GameEnvironment`.
        - **Starting the Game**:
            - Calls `environment.play()` to initiate the interaction between the hero and the obstacle.

3. **Entry Point Check**:
    - `if __name__ == "__main__": main()`
        - Ensures that the `main` function runs only when the script is executed directly.

**Key Takeaways**:

- User input determines which factory is used, showcasing the Abstract Factory Pattern's flexibility.
- The game environment remains decoupled from the specific factories, relying only on the abstract interfaces they provide.

---

## 🧪 Testing the Abstract Factory Implementation

Let's run the `abstract_factory.py` script to observe how the Abstract Factory pattern works in practice.

### 1. Execute the Script

Run the following command in your terminal:

```bash
python3.12 ch03/factory/abstract_factory.py
```

### 2. Sample Output

**Teenager (FrogWorld)**:
```
Hello. What's your name? Arthur
Welcome Arthur. How old are you? 13

	------ Frog World -------
Arthur the Frog encounters a bug and eats it!
```

**Adult (WizardWorld)**:
```
Hello. What's your name? Tom
Welcome Tom. How old are you? 34

	------ Wizard World -------
Tom the Wizard battles against an evil ork and kills it!
```

### 3. Verification

- **Teenager Scenario**:
    - User inputs name "Arthur" and age "13".
    - The game selects `FrogWorld`.
    - Outputs interaction between Arthur the Frog and a bug.

- **Adult Scenario**:
    - User inputs name "Tom" and age "34".
    - The game selects `WizardWorld`.
    - Outputs interaction between Tom the Wizard and an ork.

**Conclusion**:

The output confirms that the Abstract Factory pattern effectively manages the creation of related objects (`Frog` and `Bug` for `FrogWorld`, `Wizard` and `Ork` for `WizardWorld`). The `GameEnvironment` seamlessly interacts with different factories, ensuring that the appropriate components are created and used without modifying the high-level game logic.
