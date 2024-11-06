# 🧑‍💻 **Runtime Validation with Pydantic** ✨

If you're looking to learn data validation in Python, especially if you're a beginner, **Pydantic** is an excellent tool that can assist you. This guide will walk you through step-by-step on how to use Pydantic to apply runtime validation in your Python classes. We'll create a simple **User Profile** class and implement Pydantic validations within it.


## 📚 **Table of Contents**

1. [🌟 What is Pydantic?](#-what-is-pydantic)
2. [🔧 Installing Pydantic](#-installing-pydantic)
3. [👨‍💼 Creating a Simple User Profile Class](#-creating-a-simple-user-profile-class)
4. [✅ Adding Validations with Pydantic](#-adding-validations-with-pydantic)
5. [🔄 Viewing Runtime Validation](#-viewing-runtime-validation)
6. [❌ Handling Validation Errors](#-handling-validation-errors)
7. [📝 Complete Code Example](#-complete-code-example)
8. [📌 Summary](#-summary)


## 🌟 What is Pydantic?

**Pydantic** is a Python library that simplifies data validation and settings management. It uses Python's type annotations to create data models and automatically validates data when you instantiate the model. This means that if there's an error in your data, Pydantic will notify you immediately.

### 🌟 **Key Features:**

- **Type Validation:** Checks data against specified types.
- **Data Parsing:** Parses data from different sources (like JSON, YAML, etc.).
- **Error Reporting:** Provides detailed error messages when validation fails.
- **Ease of Use:** Comes with simple syntax and powerful features.


## 🔧 Installing Pydantic

First, you'll need to install Pydantic. This is quite straightforward if you're using Python and `pip`.

### **Installation Steps:**

1. **Create a Virtual Environment (Recommended):**

   Virtual environments keep your project's dependencies isolated, preventing conflicts between different projects.

   ```bash
   python3 -m venv venv
   ```

   **Explanation:**
   - The command `python3 -m venv venv` creates a virtual environment named `venv`. This isolates your project's dependencies from other projects.

2. **Activate the Virtual Environment:**

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   **Explanation:**
   - Running `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows) activates the virtual environment. This ensures that any packages you install using `pip` are confined to this environment.

3. **Install Pydantic:**

   ```bash
   pip install pydantic
   ```

   **Explanation:**
   - The command `pip install pydantic` installs the Pydantic library, which is essential for data validation in your project.

   > **Note:** If you also want to use type checking (`mypy`), you can run:
   
   ```bash
   pip install pydantic[mypy]
   ```


## 👨‍💼 Creating a Simple User Profile Class

Let's create a simple **User Profile** class that will store a user's name, email, age, and phone number.

### **Step 1: Create a Python File**

First, create a Python file, for example, `user.py`.

```bash
touch user.py
```

### **Step 2: Define the User Class Without Pydantic**

Initially, let's create a simple Python class without any validation.

```python
# user.py

class User:
    def __init__(self, name: str, email: str, age: int, phone: str):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone

# Example Usage
user = User(name="Ali Ahmed", email="ali@example.com", age=30, phone="1234567890")
print(user.name)
```

**Explanation:**

- **Class Definition:**
  - `class User:` defines a new class named `User`.
  
- **Constructor (`__init__` Method):**
  - `def __init__(self, name: str, email: str, age: int, phone: str):` is the constructor method that's called when creating a new `User` object.
  - `self.name = name` assigns the `name` parameter to the instance variable `self.name`.
  - Similarly, `email`, `age`, and `phone` are assigned to their respective instance variables.
  
- **Example Usage:**
  - `user = User(name="Ali Ahmed", email="ali@example.com", age=30, phone="1234567890")` creates a `User` object.
  - `print(user.name)` prints the user's name.

**Limitation:**
This class lacks any form of validation. You can provide any type of data, whether it's correct or not.


## ✅ Adding Validations with Pydantic

Now, let's modify this class using Pydantic to add runtime data validation.

### **Step 1: Import Pydantic**

Import `BaseModel` from Pydantic, which serves as the base for creating data models.

```python
from pydantic import BaseModel
```

**Explanation:**

- `from pydantic import BaseModel` imports the `BaseModel` class from Pydantic. This is the foundation for all Pydantic models.

### **Step 2: Define the User Class with Pydantic**

Now, inherit the `User` class from `BaseModel` and use type annotations.

```python
# user.py

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int
    phone: str
```

**Explanation:**

- **Inheritance:**
  - `class User(BaseModel):` means the `User` class now inherits from Pydantic's `BaseModel`. This brings in Pydantic's data validation capabilities.
  
- **Type Annotations:**
  - `name: str` specifies that the `name` field should be of type string.
  - `email: str` specifies that the `email` field should be of type string.
  - `age: int` specifies that the `age` field should be of type integer.
  - `phone: str` specifies that the `phone` field should be of type string.

### **Step 3: Adding Basic Validations**

Next, we'll add some basic validations such as ensuring the email format and setting an age range.

```python
# user.py

from pydantic import BaseModel, EmailStr, Field, validator

class User(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    age: int = Field(..., ge=0, le=120)  # age >= 0 and <= 120
    phone: str

    @validator('phone')
    def phone_must_be_digits(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits.')
        if len(v) != 10:
            raise ValueError('Phone number must be exactly 10 digits.')
        return v
```

**Explanation:**

- **Imports:**
  - `from pydantic import BaseModel, EmailStr, Field, validator` imports necessary components from Pydantic:
    - `EmailStr`: A special type that handles email validation.
    - `Field`: Allows adding additional configurations to fields.
    - `validator`: Used to define custom validation methods.
  
- **Field Definitions with Validations:**
  - **`name: str = Field(..., min_length=1)`**
    - Defines the `name` field as a string.
    - `Field(..., min_length=1)` specifies that `name` is required (denoted by `...`) and must have a minimum length of 1 character.
  
  - **`email: EmailStr`**
    - Defines the `email` field using `EmailStr`, which ensures the email has a valid format.
  
  - **`age: int = Field(..., ge=0, le=120)`**
    - Defines the `age` field as an integer.
    - `Field(..., ge=0, le=120)` specifies that `age` must be greater than or equal to 0 and less than or equal to 120.
  
  - **`phone: str`**
    - Defines the `phone` field as a string.
    - A custom validator will be added to enforce additional constraints.
  
- **Custom Validator:**
  
  ```python
  @validator('phone')
  def phone_must_be_digits(cls, v):
      if not v.isdigit():
          raise ValueError('Phone number must contain only digits.')
      if len(v) != 10:
          raise ValueError('Phone number must be exactly 10 digits.')
      return v
  ```
  
  - **Decorator `@validator('phone')`:**
    - Indicates that the following method is a validator for the `phone` field.
  
  - **Method `phone_must_be_digits`:**
    - `cls`: Reference to the class.
    - `v`: The value of the `phone` field being validated.
  
  - **Validation Logic:**
    - `if not v.isdigit():` checks if the phone number contains only digits.
      - If not, it raises a `ValueError` with the message `'Phone number must contain only digits.'`
    
    - `if len(v) != 10:` checks if the phone number is exactly 10 digits long.
      - If not, it raises a `ValueError` with the message `'Phone number must be exactly 10 digits.'`
    
    - `return v`: If all validations pass, it returns the validated value.


## 🔄 Viewing Runtime Validation

Now, let's test the runtime validation by creating `User` instances with both valid and invalid data.

### **Step 1: Instantiate the User Class with Valid Data**

```python
# user.py (continued)

def main():
    try:
        user = User(
            name="Ali Ahmed",
            email="ali@example.com",
            age=30,
            phone="1234567890"
        )
        print(user)
    except ValidationError as e:
        print(e.json())

if __name__ == "__main__":
        main()
```

**Explanation:**

- **Function `main`:**
  - **Try Block:**
    - Attempts to create a `User` instance with valid data:
      - `name="Ali Ahmed"`: Valid name (more than 1 character).
      - `email="ali@example.com"`: Valid email format.
      - `age=30`: Valid age (0 <= 30 <= 120).
      - `phone="1234567890"`: Valid phone number (only digits and exactly 10 digits).
  
    - `print(user)`: If the instantiation is successful, it prints the `User` object.
  
  - **Except Block:**
    - Catches any `ValidationError` that occurs during instantiation.
    - `print(e.json())`: Prints the validation errors in JSON format for detailed information.
  
- **Execution Guard:**
  - `if __name__ == "__main__":` ensures that the `main()` function runs only when the script is executed directly, not when imported as a module.

**Expected Output:**

```
name='Ali Ahmed' email='ali@example.com' age=30 phone='1234567890'
```

### **Step 2: Instantiate with Invalid Email**

```python
# user.py (continued)

def main():
    try:
        user = User(
            name="Ali Ahmed",
            email="aliexample.com",  # Invalid email
            age=30,
            phone="1234567890"
        )
        print(user)
    except ValidationError as e:
        print(e.json())
```

**Explanation:**

- **Invalid Data:**
  - `email="aliexample.com"`: Invalid email format (missing `@`).
  
- **Process:**
  - Attempts to create a `User` instance with an invalid email.
  
- **Output:**

```
[
  {
    "loc": ["email"],
    "msg": "value is not a valid email address",
    "type": "value_error.email"
  }
]
```

**Explanation:**

- **Validation Error:**
  - `loc`: Location of the error (`email` field).
  - `msg`: Error message (`value is not a valid email address`).
  - `type`: Type of error (`value_error.email`).

### **Step 3: Instantiate with Invalid Phone Number**

```python
# user.py (continued)

def main():
    try:
        user = User(
            name="Ali Ahmed",
            email="ali@example.com",
            age=30,
            phone="12345abc90"  # Invalid phone
        )
        print(user)
    except ValidationError as e:
        print(e.json())
```

**Explanation:**

- **Invalid Data:**
  - `phone="12345abc90"`: Phone number contains non-digit characters (`abc`).
  
- **Process:**
  - Attempts to create a `User` instance with an invalid phone number.
  
- **Output:**

```
[
  {
    "loc": ["phone"],
    "msg": "Phone number must contain only digits.",
    "type": "value_error"
  }
]
```

**Explanation:**

- **Validation Error:**
  - `loc`: Location of the error (`phone` field).
  - `msg`: Error message (`Phone number must contain only digits.`).
  - `type`: Type of error (`value_error`).

### **Step 4: Instantiate with Short Phone Number**

```python
# user.py (continued)

def main():
    try:
        user = User(
            name="Ali Ahmed",
            email="ali@example.com",
            age=30,
            phone="123456789"  # Only 9 digits
        )
        print(user)
    except ValidationError as e:
        print(e.json())
```

**Explanation:**

- **Invalid Data:**
  - `phone="123456789"`: Phone number is only 9 digits long, whereas 10 digits are required.
  
- **Process:**
  - Attempts to create a `User` instance with a short phone number.
  
- **Output:**

```
[
  {
    "loc": ["phone"],
    "msg": "Phone number must be exactly 10 digits.",
    "type": "value_error"
  }
]
```

**Explanation:**

- **Validation Error:**
  - `loc`: Location of the error (`phone` field).
  - `msg`: Error message (`Phone number must be exactly 10 digits.`).
  - `type`: Type of error (`value_error`).


## ❌ Handling Validation Errors

Gracefully handling Pydantic validation errors is crucial to prevent your application from crashing and to provide informative messages to users.

### **Step 1: Catching Validation Errors**

```python
# user.py (continued)

from pydantic import ValidationError

def main():
    try:
        user = User(
            name="",  # Invalid name
            email="ali@example.com",
            age=130,  # Invalid age
            phone="1234567890"
        )
        print(user)
    except ValidationError as e:
        print("Validation Error:")
        print(e.json())

if __name__ == "__main__":
        main()
```

**Explanation:**

- **Invalid Data:**
  - `name=""`: Name is an empty string.
  - `age=130`: Age exceeds the allowed maximum (120).
  
- **Process:**
  - Attempts to create a `User` instance with an invalid name and age.
  
- **Output:**

```
Validation Error:
[
  {
    "loc": ["name"],
    "msg": "ensure this value has at least 1 characters",
    "type": "value_error.any_str.min_length",
    "ctx": {
      "limit_value": 1
    }
  },
  {
    "loc": ["age"],
    "msg": "ensure this value is less than or equal to 120",
    "type": "value_error.number.not_le",
    "ctx": {
      "limit_value": 120
    }
  }
]
```

**Explanation:**

- **Validation Errors:**
  - `name`: Must have at least 1 character.
  - `age`: Must be less than or equal to 120.

### **Step 2: Providing User-Friendly Error Messages**

You can present validation errors in a user-friendly format to make it easier for users to understand what went wrong.

```python
# user.py (continued)

def main():
    try:
        user = User(
            name="",
            email="aliexample.com",  # Invalid email
            age=-5,  # Invalid age
            phone="12345abc"  # Invalid phone
        )
        print(user)
    except ValidationError as e:
        print("Validation Failed:")
        for error in e.errors():
            field = error['loc'][0]
            message = error['msg']
            print(f"Error in '{field}': {message}")
```

**Explanation:**

- **Invalid Data:**
  - `name=""`: Empty string.
  - `email="aliexample.com"`: Invalid email format.
  - `age=-5`: Negative age.
  - `phone="12345abc"`: Phone number contains non-digit characters.
  
- **Process:**
  - Attempts to create a `User` instance with multiple invalid fields.
  
- **Output:**

```
Validation Failed:
Error in 'name': ensure this value has at least 1 characters
Error in 'email': value is not a valid email address
Error in 'age': ensure this value is greater than or equal to 0
Error in 'phone': Phone number must contain only digits.
```

**Explanation:**

- **Custom Error Handling:**
  - Iterates through each validation error.
  - Extracts the field (`loc`) and the error message (`msg`).
  - Prints the errors in a readable format for users.


## 📝 Complete Code Example

Let's combine everything to see a complete example.

```python
# user.py

from pydantic import BaseModel, EmailStr, Field, validator, ValidationError
from typing import Optional

class User(BaseModel):
    name: str = Field(..., min_length=1, description="User's name")
    email: EmailStr = Field(..., description="User's valid email address")
    age: int = Field(..., ge=0, le=120, description="User's age, between 0 and 120")
    phone: str = Field(..., description="User's 10-digit phone number")

    @validator('phone')
    def phone_must_be_valid(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits.')
        if len(v) != 10:
            raise ValueError('Phone number must be exactly 10 digits.')
        return v

def main():
    # Valid User Example
    try:
        user = User(
            name="Ali Ahmed",
            email="ali@example.com",
            age=30,
            phone="1234567890"
        )
        print("Valid User Created:")
        print(user)
    except ValidationError as e:
        print("Validation Error for Valid User:")
        print(e.json())

    print("\n" + "-"*50 + "\n")

    # Invalid User Example
    try:
        user = User(
            name="",  # Invalid name
            email="aliexample.com",  # Invalid email
            age=130,  # Invalid age
            phone="12345abcde"  # Invalid phone
        )
        print("Invalid User Created:")
        print(user)
    except ValidationError as e:
        print("Validation Error for Invalid User:")
        for error in e.errors():
            field = error['loc'][0]
            message = error['msg']
            print(f"Error in '{field}': {message}")

if __name__ == "__main__":
    main()
```

### **Code Breakdown:**

1. **Imports:**

   ```python
   from pydantic import BaseModel, EmailStr, Field, validator, ValidationError
   from typing import Optional
   ```

   - **`BaseModel`**: Pydantic's base class for defining data models.
   - **`EmailStr`**: A special type for email validation.
   - **`Field`**: Used to add additional configurations to fields.
   - **`validator`**: Used to define custom validation methods.
   - **`ValidationError`**: Used to handle validation errors.
   - **`Optional`**: From the `typing` module, used if a field is optional.

2. **User Class Definition:**

   ```python
   class User(BaseModel):
       name: str = Field(..., min_length=1, description="User's name")
       email: EmailStr = Field(..., description="User's valid email address")
       age: int = Field(..., ge=0, le=120, description="User's age, between 0 and 120")
       phone: str = Field(..., description="User's 10-digit phone number")

       @validator('phone')
       def phone_must_be_valid(cls, v):
           if not v.isdigit():
               raise ValueError('Phone number must contain only digits.')
           if len(v) != 10:
               raise ValueError('Phone number must be exactly 10 digits.')
           return v
   ```

   **Explanation:**

   - **Field Definitions with Validations:**
     - **`name: str = Field(..., min_length=1, description="User's name")`**
       - Defines the `name` field as a string.
       - `Field(..., min_length=1)` specifies that `name` is required and must have a minimum length of 1 character.
       - `description="User's name"` provides a description for the field, useful for documentation.
     
     - **`email: EmailStr = Field(..., description="User's valid email address")`**
       - Defines the `email` field using `EmailStr`, ensuring a valid email format.
       - `Field(..., description="User's valid email address")` specifies that this field is required and provides a description.
     
     - **`age: int = Field(..., ge=0, le=120, description="User's age, between 0 and 120")`**
       - Defines the `age` field as an integer.
       - `Field(..., ge=0, le=120)` ensures that `age` is greater than or equal to 0 and less than or equal to 120.
       - `description="User's age, between 0 and 120"` provides a description.
     
     - **`phone: str = Field(..., description="User's 10-digit phone number")`**
       - Defines the `phone` field as a string.
       - `Field(..., description="User's 10-digit phone number")` specifies that this field is required and provides a description.
   
   - **Custom Validator:**
     
     ```python
     @validator('phone')
     def phone_must_be_valid(cls, v):
         if not v.isdigit():
             raise ValueError('Phone number must contain only digits.')
         if len(v) != 10:
             raise ValueError('Phone number must be exactly 10 digits.')
         return v
     ```
     
     - **Decorator `@validator('phone')`:**
       - Indicates that this method is a validator for the `phone` field.
     
     - **Method `phone_must_be_valid`:**
       - `cls`: Reference to the class.
       - `v`: Value of the `phone` field being validated.
     
     - **Validation Logic:**
       - `if not v.isdigit():` checks if the phone number contains only digits.
         - If not, it raises a `ValueError` with the message `'Phone number must contain only digits.'`
       
       - `if len(v) != 10:` checks if the phone number is exactly 10 digits long.
         - If not, it raises a `ValueError` with the message `'Phone number must be exactly 10 digits.'`
       
       - `return v`: If all validations pass, it returns the validated value.

3. **Main Function:**

   ```python
   def main():
       # Valid User Example
       try:
           user = User(
               name="Ali Ahmed",
               email="ali@example.com",
               age=30,
               phone="1234567890"
           )
           print("Valid User Created:")
           print(user)
       except ValidationError as e:
           print("Validation Error for Valid User:")
           print(e.json())

       print("\n" + "-"*50 + "\n")

       # Invalid User Example
       try:
           user = User(
               name="",  # Invalid name
               email="aliexample.com",  # Invalid email
               age=130,  # Invalid age
               phone="12345abcde"  # Invalid phone
           )
           print("Invalid User Created:")
           print(user)
       except ValidationError as e:
           print("Validation Error for Invalid User:")
           for error in e.errors():
               field = error['loc'][0]
               message = error['msg']
               print(f"Error in '{field}': {message}")
   ```

   **Explanation:**

   - **Valid User Example:**
     - **Try Block:**
       - Attempts to create a `User` instance with valid data:
         - `name="Ali Ahmed"`: Valid name (more than 1 character).
         - `email="ali@example.com"`: Valid email format.
         - `age=30`: Valid age (0 <= 30 <= 120).
         - `phone="1234567890"`: Valid phone number (only digits and exactly 10 digits).
     
       - `print("Valid User Created:")` prints a message indicating a valid user was created.
       - `print(user)` prints the details of the `User` object.
     
     - **Except Block:**
       - Catches any `ValidationError` that occurs during instantiation.
       - `print(e.json())` prints the validation errors in JSON format for detailed information.
   
   - **Separator:**
     - `print("\n" + "-"*50 + "\n")` prints a line of dashes to separate the output of the valid and invalid user examples.
   
   - **Invalid User Example:**
     - **Try Block:**
       - Attempts to create a `User` instance with invalid data:
         - `name=""`: Invalid name (empty string).
         - `email="aliexample.com"`: Invalid email format (missing `@`).
         - `age=130`: Invalid age (130 > 120).
         - `phone="12345abcde"`: Invalid phone number (contains non-digit characters).
     
       - `print("Invalid User Created:")` prints a message indicating an invalid user was attempted to be created.
       - `print(user)` attempts to print the `User` object, but since validation fails, this line won't execute.
     
     - **Except Block:**
       - Catches the `ValidationError`.
       - Iterates through each validation error using `for error in e.errors():`.
       - Extracts the field (`loc`) and the error message (`msg`).
       - Prints the errors in a readable format: `Error in 'field': message`.

4. **Execution Guard:**

   ```python
   if __name__ == "__main__":
       main()
   ```

   **Explanation:**

   - `if __name__ == "__main__":` ensures that the `main()` function runs only when the script is executed directly, not when imported as a module.
   - `main()` function is called, which handles both valid and invalid user examples.

### **Running the Code:**

1. **Ensure Virtual Environment is Activated:**

   ```bash
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate     # Windows
   ```

2. **Run the Script:**

   ```bash
   python user.py
   ```

### **Expected Output:**

```
Valid User Created:
name='Ali Ahmed' email='ali@example.com' age=30 phone='1234567890'
--

Validation Error for Invalid User:
Error in 'name': ensure this value has at least 1 characters
Error in 'email': value is not a valid email address
Error in 'age': ensure this value is less than or equal to 120
Error in 'phone': Phone number must contain only digits.
```

**Explanation:**

- **First Part:**
  - With valid data, the `User` instance is created successfully and its details are printed.

- **Second Part:**
  - With invalid data, the `User` instance fails to be created.
  - Validation errors are caught and printed in a user-friendly format, specifying which fields have issues and what the issues are.


## 📌 Summary

In this guide, we learned how to apply runtime validations in a simple **User Profile** class using Pydantic. Here's what we covered:

1. **Installed Pydantic:** Used `pip` to install Pydantic.
2. **Defined the User Class:** Inherited the `User` class from Pydantic's `BaseModel`.
3. **Added Validations:** Used type hints and Pydantic validators to impose restrictions on fields.
4. **Tested Runtime Validation:** Provided both valid and invalid data to observe Pydantic's validation in action.
5. **Handled Validation Errors:** Caught errors and displayed user-friendly messages.

### 🌟 **Key Takeaways:**

- **Powerful Data Validation with Pydantic:** Pydantic allows you to implement complex data validations effortlessly.
- **Importance of Type Hints:** Utilizing Python's type hints helps in writing cleaner and more reliable code.
- **Essential of Error Handling:** Gracefully handling validation errors makes your application robust.
- **Flexibility:** Pydantic offers flexibility from simple to complex validations, making it suitable for various use-cases.

### 🎯 **Final Thoughts:**

**Pydantic** streamlines data validation in your Python projects, which is especially crucial for sensitive domains like banking applications. By adopting it, you can ensure data integrity, boost developer productivity, and enhance the overall reliability of your applications.

**Happy Coding!** 🚀😊🎉


## 🌐 Additional Resources

If you want to delve deeper into Pydantic, explore the following resources:

- [**Pydantic Official Documentation**](https://pydantic-docs.helpmanual.io/) 📘
  - A comprehensive guide covering all features and use-cases of Pydantic.
  
- [**Real Python: Pydantic Data Validation in Python**](https://realpython.com/pydantic-python/) 🛠️🔍
  - A practical tutorial that explains Pydantic's features with examples.
  
- [**Pydantic Tutorial by Sebastián Ramírez**](https://pydantic-docs.helpmanual.io/usage/models/) 🧑‍💻✨
  - Detailed explanations and advanced usage scenarios.
  
- [**Effective Python: 59 Specific Ways to Write Better Python**](https://effectivepython.com/) 📚🧠
  - Tips for writing efficient and maintainable Python code.
  
- [**Python Type Hints Guide**](https://docs.python.org/3/library/typing.html) 📄🔧
  - Official Python documentation on type hints, which are foundational for Pydantic's functionality.
  
- [**Design Patterns in Python**](https://refactoring.guru/design-patterns/python) 🛠️🔍
  - Methods to apply design patterns in Python, complementing Pydantic's capabilities.
  
- [**Mypy Official Documentation**](https://mypy.readthedocs.io/en/stable/) 📈🔧
  - Integrate type checking into your development workflow.
  
- [**Secure Coding in Python**](https://realpython.com/python-secure/) 🔐🐍
  - Best practices for writing secure Python applications, essential when handling sensitive data.

!
## 📝 Final Notes
Implementing runtime data validation is indispensable for developing secure and reliable banking applications. **Pydantic** streamlines this process by allowing developers to define clear, concise, and robust data models that enforce data integrity automatically. By integrating Pydantic into your projects, you can significantly reduce the risk of data-related errors, enhance security, and improve overall system reliability.

However, it's essential to balance strict validation with flexibility. Overly rigid models might impede legitimate data flows, while too lenient models can introduce vulnerabilities. Always tailor your validation logic to align with your application's specific requirements and business rules.


Feel free to **integrate Pydantic and runtime validation** into your Python banking projects to harness the full potential of **robust data management**, **security**, and **maintainable code design**! 🚀😊🎉


## 📝 Final Notes

Runtime data validation is indispensable for developing secure and reliable banking applications. **Pydantic** streamlines this process by allowing developers to define clear, concise, and robust data models that enforce data integrity automatically. By integrating Pydantic into your projects, you can significantly reduce the risk of data-related errors, enhance security, and improve overall system reliability.

However, it's essential to balance strict validation with flexibility. Overly rigid models might impede legitimate data flows, while too lenient models can introduce vulnerabilities. Always tailor your validation logic to align with your application's specific requirements and business rules.

## 🌐 Additional Resources

To further enhance your understanding of runtime data validation with Pydantic and its application in Python projects, explore the following **valuable resources**:

- [**Pydantic Official Documentation**](https://pydantic-docs.helpmanual.io/) 📘
- [**Real Python: Pydantic Data Validation in Python**](https://realpython.com/pydantic-python/) 🛠️🔍
- [**Pydantic Tutorial by Sebastián Ramírez**](https://pydantic-docs.helpmanual.io/usage/models/) 🧑‍💻✨
- [**Effective Python: 59 Specific Ways to Write Better Python**](https://effectivepython.com/) 📚🧠
- [**Python Type Hints Guide**](https://docs.python.org/3/library/typing.html) 📄🔧
- [**Design Patterns in Python**](https://refactoring.guru/design-patterns/python) 🛠️🔍
- [**Mypy Official Documentation**](https://mypy.readthedocs.io/en/stable/) 📈🔧
- [**Secure Coding in Python**](https://realpython.com/python-secure/) 🔐🐍

