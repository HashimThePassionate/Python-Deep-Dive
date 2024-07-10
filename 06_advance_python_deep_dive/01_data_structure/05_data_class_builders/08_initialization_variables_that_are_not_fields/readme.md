# Initialization Variables That Are Not Fields

## Introduction
Sometimes, you may need to pass arguments to the `__init__` method that are not instance fields. These are called init-only variables. The `dataclasses` module provides the `InitVar` pseudotype for this purpose.

### Purpose of `InitVar`
- **Init-only Variables**: Arguments passed to `__init__` that are not stored as instance fields.
- **Special Handling**: These variables can be used for special initialization logic in the `__post_init__` method.

### Example
Consider a data class where a field is initialized from a database object, which must be passed to the constructor but should not be stored as an instance attribute.

### Code Example
Here’s an example illustrating the use of `InitVar`:

```python
from dataclasses import dataclass, InitVar

# Example database type
class DatabaseType:
    def lookup(self, key):
        # Simulate a database lookup
        return 42

@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

# Creating an instance of C
my_database = DatabaseType()
c = C(10, database=my_database)
print(c)
# Output: C(i=10, j=42)
```

### Explanation

#### Class Definition
- **Attributes**:
  - `i`: An integer attribute.
  - `j`: An integer attribute with a default value of `None`.
  - `database`: An `InitVar` attribute, meaning it is passed to `__init__` but not stored as an instance attribute.

#### `__post_init__` Method
- **Special Initialization**:
  - The `database` argument is used to initialize `j` if `j` is `None`.
  - `database.lookup('j')`: Simulates a lookup in the database to initialize `j` to `42`.

#### Creating an Instance
- **Usage**:
  - `my_database = DatabaseType()`: Create a database object.
  - `c = C(10, database=my_database)`: Pass the database object to the constructor.
  - `print(c)`: The instance `c` has `i` set to `10` and `j` initialized to `42` from the database.

### How `j` is Initialized to 42

1. **Class and Method Definitions**:
   - `DatabaseType`: A mock class representing a database. The `lookup` method simulates a database lookup and returns `42`.
   - `C`: A data class with attributes `i`, `j`, and `database`.

2. **Attributes in Class `C`**:
   - `i`: An integer attribute.
   - `j`: An integer attribute with a default value of `None`.
   - `database`: An `InitVar` attribute, meaning it is passed to `__init__` but not stored as an instance attribute.

3. **Instance Creation**:
   - `my_database = DatabaseType()`: Creates an instance of the `DatabaseType` class.
   - `c = C(10, database=my_database)`: Creates an instance of class `C`, passing `10` for `i` and `my_database` for `database`.

4. **Generated `__init__` Method**:
   ```python
   class C:
       def __init__(self, i: int, j: int = None, database: DatabaseType = None):
           self.i = i
           self.j = j
           self.__post_init__(database)
   ```

5. **`__post_init__` Method**:
   - `def __post_init__(self, database):`: This method is called after the `__init__` method.
   - `if self.j is None and database is not None:`: Checks if `j` is `None` and if `database` is not `None`.
   - `self.j = database.lookup('j')`: Calls the `lookup` method of the `database` object, passing `'j'` as the key. The `lookup` method returns `42`, so `self.j` is set to `42`.

### Detailed Process

1. **Initialization**:
   - The `__init__` method assigns `10` to `i` and `None` to `j`.
   - The `database` parameter is passed to `__post_init__`.

2. **Post-initialization**:
   - The `__post_init__` method checks if `j` is `None` and if `database` is provided.
   - Since both conditions are met (`j` is `None` and `database` is not `None`), `self.j` is set to the value returned by `database.lookup('j')`, which is `42`.

3. **Final Output**:
   - When `print(c)` is executed, it shows `C(i=10, j=42)`.

### How `__init__` is Generated
When you use the `@dataclass` decorator, it automatically generates the `__init__` method for the class. Here's how the `__init__` method would look like for the class `C`:

```python
class C:
    def __init__(self, i: int, j: int = None, database: DatabaseType = None):
        self.i = i
        self.j = j
        self.__post_init__(database)
```

### Detailed Explanation of Generated `__init__`
1. **Parameters**:
   - `i`: Required integer parameter.
   - `j`: Optional integer parameter, defaults to `None`.
   - `database`: Optional `InitVar` parameter, defaults to `None`.

2. **Instance Attribute Assignment**:
   - `self.i = i`: Assigns the value of `i` to the instance attribute `i`.
   - `self.j = j`: Assigns the value of `j` to the instance attribute `j`.

3. **Calling `__post_init__`**:
   - `self.__post_init__(database)`: Calls the `__post_init__` method, passing the `database` argument.

### Benefits
- **Flexibility**: Allows for complex initialization logic without storing unnecessary attributes.
- **Clean Code**: Keeps the class interface clean by not exposing implementation details as instance attributes.

### Note
- **Not Listed by `dataclasses.fields`**: The `InitVar` attribute will not be listed by the `dataclasses.fields` function.
- **Passed to `__post_init__`**: The `InitVar` argument will be passed to the `__post_init__` method, so you must include it in the method signature.

### Conclusion
Using `InitVar` in the `dataclasses` module allows you to handle complex initialization scenarios where certain arguments are needed for initialization but should not be stored as instance fields. This keeps your class definitions clean and focused on their primary responsibilities.
