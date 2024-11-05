# 🏦 **Runtime Checking with Pydantic** ✨

Ensuring the integrity and correctness of data is paramount in developing robust software systems. In banking applications, where financial data is sensitive and critical, validating data at runtime becomes essential to prevent inconsistencies, fraud, and operational errors. This guide delves into **runtime checking** using the **Pydantic** library in Python, illustrating its application through a **Bank Management System** example. We'll explore key concepts, provide detailed code examples, discuss best practices, and highlight potential pitfalls to help you effectively implement runtime validation in your projects.


## 📚 **Table of Contents**

- [🏦 **Runtime Checking with Pydantic** ✨](#-runtime-checking-with-pydantic-)
  - [📚 **Table of Contents**](#-table-of-contents)
  - [🌟 Overview](#-overview)
    - [🌟 **Key Benefits of Runtime Checking with Pydantic:**](#-key-benefits-of-runtime-checking-with-pydantic)
  - [📂 Project Structure](#-project-structure)
  - [🔑 Key Concepts in Runtime Checking with Pydantic](#-key-concepts-in-runtime-checking-with-pydantic)
    - [👨‍👩‍👧 Defining Data Models with Pydantic](#-defining-data-models-with-pydantic)
    - [🛡️ Validation and Parsing](#️-validation-and-parsing)
    - [🔄 Constrained Types and Validators](#-constrained-types-and-validators)
  - [🏦 Practical Example: Bank Management System](#-practical-example-bank-management-system)
    - [📄 Defining the Base Models](#-defining-the-base-models)
    - [💳 Creating Derived Models: `SavingsAccount` and `CheckingAccount`](#-creating-derived-models-savingsaccount-and-checkingaccount)
    - [🗂️ Loading and Validating Data](#️-loading-and-validating-data)
  - [🔧 Advanced Pydantic Features](#-advanced-pydantic-features)
    - [🔍 Custom Validators](#-custom-validators)
    - [🛠️ Strict Types](#️-strict-types)
  - [✅ Best Practices for Using Pydantic in Banking Applications](#-best-practices-for-using-pydantic-in-banking-applications)
    - [🏗️ Designing Robust Models](#️-designing-robust-models)
    - [🧩 Separating Concerns](#-separating-concerns)
  - [💬 Discussion Topic](#-discussion-topic)
  - [🎯 Conclusion](#-conclusion)
    - [🌟 **Key Takeaways:**](#-key-takeaways)
    - [🎯 **Final Thoughts:**](#-final-thoughts)
  - [🌐 Additional Resources](#-additional-resources)
  - [🛠️ **Detailed Code Examples**](#️-detailed-code-examples)
    - [1. `bank/__init__.py`](#1-bank__init__py)
    - [2. `bank/models.py`](#2-bankmodelspy)
    - [3. `bank/main.py`](#3-bankmainpy)
  - [📝 Final Notes](#-final-notes)
  - [📝 Final Notes](#-final-notes-1)
  - [🌐 Additional Resources](#-additional-resources-1)


## 🌟 Overview

In software development, especially in domains like banking where data integrity is non-negotiable, **runtime checking** plays a crucial role in ensuring that the data flowing through the system adheres to expected formats and constraints. **Pydantic** is a powerful Python library that facilitates this by providing data validation and settings management using Python type annotations.

### 🌟 **Key Benefits of Runtime Checking with Pydantic:**

- **🔒 Data Integrity:** Ensures that all data entering the system meets predefined criteria, reducing the risk of errors and inconsistencies.
- **🚀 Developer Efficiency:** Minimizes the need for boilerplate validation code, allowing developers to focus on core functionalities.
- **🛡️ Security Enhancement:** Prevents malformed or malicious data from causing unforeseen issues or vulnerabilities.
- **📈 Improved Maintainability:** Centralizes validation logic within models, making the codebase easier to manage and understand.


## 📂 Project Structure

To illustrate the concepts, we'll structure our **Bank Management System** project as follows:

```
bank_management/
├── bank/
│   ├── __init__.py
│   ├── models.py
├── main.py
└── README.md
```


## 🔑 Key Concepts in Runtime Checking with Pydantic

### 👨‍👩‍👧 Defining Data Models with Pydantic

Pydantic allows you to define **data models** using Python's type annotations. These models not only serve as schemas for your data but also enforce validation rules automatically when data is instantiated.

### 🛡️ Validation and Parsing

While Python's type annotations provide a form of documentation and hint for developers, Pydantic leverages these annotations to perform **runtime validation**. It parses incoming data, ensuring that it conforms to the specified types and constraints, raising informative errors when violations occur.

### 🔄 Constrained Types and Validators

Pydantic offers **constrained types** (like `constr`, `conint`) that allow you to enforce additional restrictions on your data beyond basic type checking. Additionally, **validators** can be custom methods that perform more intricate validation logic, ensuring that your data meets complex business rules.


## 🏦 Practical Example: Bank Management System

Let's build a simple **Bank Management System** to demonstrate how Pydantic can be used for runtime data validation. We'll focus on modeling **accounts**, ensuring that all data conforms to banking regulations and business rules.

### 📄 Defining the Base Models

We'll start by defining the fundamental data structures required for our banking application.

```python
# bank/models.py

from pydantic import BaseModel, Field, constr, conint, validator
from typing import List, Optional, Literal
import re

class BankDetails(BaseModel):
    routing_number: constr(regex=r'^\d{9}$')  # Exactly 9 digits
    account_number: constr(regex=r'^\d{10,12}$')  # 10 to 12 digits

class Employee(BaseModel):
    name: constr(min_length=1)
    position: Literal['Teller', 'Manager', 'Loan Officer', 'Customer Service']
    payment_details: Optional[BankDetails] = None

    @validator('payment_details', always=True)
    def check_payment_details(cls, v, values):
        if values.get('position') in ['Manager', 'Loan Officer']:
            if v is None:
                raise ValueError(f"Payment details required for position {values.get('position')}")
        return v

class Dish(BaseModel):
    name: constr(min_length=1, max_length=16)
    price_in_cents: conint(gt=0)
    description: constr(min_length=1, max_length=80)
    picture: Optional[constr(regex=r'^[\w,\s-]+\.[A-Za-z]{3,4}$')] = None  # e.g., "image.png"

class Account(BaseModel):
    account_id: constr(regex=r'^ACCT\d{6}$')  # e.g., ACCT123456
    owner_name: constr(min_length=1)
    balance_in_cents: conint(ge=0)
    transactions: List[str] = Field(default_factory=list)

class Restaurant(BaseModel):
    name: constr(regex=r'^[A-Za-z0-9 "\']{1,32}$')
    owner_full_name: constr(min_length=1)
    address: constr(min_length=1)
    employees: List[Employee]
    dishes: List[Dish]
    number_of_seats: conint(gt=0)
    offers_to_go: bool
    offers_delivery: bool

    @validator('employees')
    def check_employee_roles(cls, v):
        positions = [employee.position for employee in v]
        if 'Chef' not in positions:
            raise ValueError("At least one Chef is required.")
        if 'Server' not in positions:
            raise ValueError("At least one Server is required.")
        return v

    @validator('dishes')
    def check_unique_dishes(cls, v):
        dish_names = [dish.name for dish in v]
        if len(dish_names) != len(set(dish_names)):
            raise ValueError("Each dish must have a unique name.")
        if len(v) < 3:
            raise ValueError("There must be at least three dishes on the menu.")
        return v
```

**📌 Explanation:**

- **`BankDetails` Model:**
  - **Fields:**
    - `routing_number`: Exactly 9 digits, matching the standard U.S. routing number format.
    - `account_number`: Between 10 to 12 digits to accommodate various bank account numbers.
  
- **`Employee` Model:**
  - **Fields:**
    - `name`: Non-empty string.
    - `position`: Must be one of the specified roles.
    - `payment_details`: Optional `BankDetails`. However, positions like 'Manager' and 'Loan Officer' require payment details.
  
  - **Validator `check_payment_details`:**
    - Ensures that certain positions have payment details provided.

- **`Dish` Model:**
  - **Fields:**
    - `name`: Between 1 to 16 characters.
    - `price_in_cents`: Positive integer representing the price in cents.
    - `description`: Between 1 to 80 characters.
    - `picture`: Optional filename with a valid image extension.

- **`Account` Model:**
  - **Fields:**
    - `account_id`: Must follow the pattern 'ACCT' followed by six digits.
    - `owner_name`: Non-empty string.
    - `balance_in_cents`: Non-negative integer.
    - `transactions`: List of transaction descriptions.

- **`Restaurant` Model:**
  - **Fields:**
    - `name`: Up to 32 characters, allowing letters, numbers, spaces, and certain punctuation.
    - `owner_full_name`: Non-empty string.
    - `address`: Non-empty string.
    - `employees`: List of `Employee` instances.
    - `dishes`: List of `Dish` instances.
    - `number_of_seats`: Positive integer.
    - `offers_to_go` and `offers_delivery`: Boolean flags.
  
  - **Validators:**
    - `check_employee_roles`: Ensures that there's at least one 'Chef' and one 'Server'.
    - `check_unique_dishes`: Ensures all dish names are unique and there are at least three dishes.

### 💳 Creating Derived Models: `SavingsAccount` and `CheckingAccount`

Building upon the base `Account` model, we can create specialized account types with additional constraints or fields.

```python
# bank/models.py (continued)

class SavingsAccount(Account):
    interest_rate: conint(gt=0, lt=100)  # Interest rate as a percentage

    @validator('balance_in_cents')
    def check_min_balance(cls, v):
        if v < 10000:  # Minimum balance of $100
            raise ValueError("Savings account must have a minimum balance of $100.")
        return v

class CheckingAccount(Account):
    overdraft_limit_in_cents: conint(ge=0)  # Overdraft limit

    @validator('overdraft_limit_in_cents')
    def check_overdraft_limit(cls, v):
        if v > 50000:  # Maximum overdraft limit of $500
            raise ValueError("Overdraft limit cannot exceed $500.")
        return v
```

**📌 Explanation:**

- **`SavingsAccount` Model:**
  - **Fields:**
    - `interest_rate`: An integer between 1 and 99 representing the annual interest rate.
  
  - **Validator `check_min_balance`:**
    - Ensures that the account maintains a minimum balance of $100.

- **`CheckingAccount` Model:**
  - **Fields:**
    - `overdraft_limit_in_cents`: Non-negative integer representing the overdraft limit.
  
  - **Validator `check_overdraft_limit`:**
    - Ensures that the overdraft limit does not exceed $500.

### 🗂️ Loading and Validating Data

Let's demonstrate how to load data from a YAML file, parse it into our Pydantic models, and handle validation errors gracefully.

**Sample YAML Configuration (`bank_config.yaml`):**

```yaml
name: "City Bank"
owner_full_name: "Alice Johnson"
address: "456 Elm Street, Metropolis, MT 54321"
employees:
  - name: "Bob Smith"
    position: "Teller"
  - name: "Carol White"
    position: "Manager"
    payment_details:
      routing_number: "987654321"
      account_number: "123456789012"
dishes:
  - name: "Grilled Chicken"
    price_in_cents: 1299
    description: "Juicy grilled chicken with herbs."
  - name: "Caesar Salad"
    price_in_cents: 899
    description: "Fresh romaine with Caesar dressing."
  - name: "Beef Burger"
    price_in_cents: 1499
    description: "Classic beef burger with cheese."
number_of_seats: 50
offers_to_go: true
offers_delivery: true
```

**Loading and Validating the Configuration:**

```python
# bank/main.py

from pydantic import ValidationError
from bank.models import Restaurant
import yaml

def load_bank_config(filename: str) -> Restaurant:
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    try:
        restaurant = Restaurant(**data)
        print("Bank configuration loaded successfully.")
        return restaurant
    except ValidationError as e:
        print("Error loading bank configuration:")
        print(e.json())
        raise

def main():
    config_file = 'bank_config.yaml'
    try:
        restaurant = load_bank_config(config_file)
        # Proceed with using the validated restaurant data
        print(restaurant)
    except ValidationError:
        print("Failed to load bank configuration due to validation errors.")

if __name__ == "__main__":
    main()
```

**📌 Explanation:**

- **Function `load_bank_config`:**
  - Reads the YAML configuration file.
  - Attempts to instantiate the `Restaurant` model with the loaded data.
  - Catches and prints validation errors if any constraints are violated.

- **Function `main`:**
  - Calls `load_bank_config` and handles potential validation failures gracefully.

**Sample Output on Successful Load:**

```
Bank configuration loaded successfully.
name='City Bank' owner_full_name='Alice Johnson' address='456 Elm Street, Metropolis, MT 54321' employees=[Employee(name='Bob Smith', position='Teller', payment_details=None), Employee(name='Carol White', position='Manager', payment_details=BankDetails(routing_number='987654321', account_number='123456789012'))] dishes=[Dish(name='Grilled Chicken', price_in_cents=1299, description='Juicy grilled chicken with herbs.', picture=None), Dish(name='Caesar Salad', price_in_cents=899, description='Fresh romaine with Caesar dressing.', picture=None), Dish(name='Beef Burger', price_in_cents=1499, description='Classic beef burger with cheese.', picture=None)] number_of_seats=50 offers_to_go=True offers_delivery=True
```

**Sample Output on Validation Error (e.g., Missing Chef):**

```yaml
# bank_config.yaml (modified to remove a Chef)
employees:
  - name: "Bob Smith"
    position: "Teller"
  - name: "Carol White"
    position: "Manager"
    payment_details:
      routing_number: "987654321"
      account_number: "123456789012"
```

```
Error loading bank configuration:
{
  "detail": [
    {
      "loc": ["employees"],
      "msg": "At least one Chef is required.",
      "type": "value_error"
    },
    {
      "loc": ["employees"],
      "msg": "At least one Server is required.",
      "type": "value_error"
    }
  ]
}
Failed to load bank configuration due to validation errors.
```


## 🔧 Advanced Pydantic Features

### 🔍 Custom Validators

While Pydantic provides a robust set of built-in validators, sometimes your application requires more nuanced validation logic. Custom validators allow you to implement bespoke validation rules tailored to your business needs.

**Example: Validating Unique Account IDs Across All Accounts**

```python
# bank/models.py (continued)

from pydantic import root_validator

class Bank(BaseModel):
    name: constr(min_length=1, max_length=50)
    accounts: List[Account]

    @root_validator
    def check_unique_account_ids(cls, values):
        accounts = values.get('accounts', [])
        account_ids = [account.account_id for account in accounts]
        if len(account_ids) != len(set(account_ids)):
            raise ValueError("All account IDs must be unique.")
        return values
```

**Explanation:**

- **`Bank` Model:**
  - **Fields:**
    - `name`: Name of the bank.
    - `accounts`: List of `Account` instances.
  
  - **`root_validator` `check_unique_account_ids`:**
    - Ensures that all `account_id` values are unique across the bank's accounts.

### 🛠️ Strict Types

By default, Pydantic is permissive in type coercion. However, for critical applications like banking, you might want to enforce stricter type checks to prevent unintended data transformations.

**Example: Enforcing Strict Integers for `balance_in_cents`**

```python
# bank/models.py (continued)

from pydantic import StrictInt

class Account(BaseModel):
    account_id: constr(regex=r'^ACCT\d{6}$')  # e.g., ACCT123456
    owner_name: constr(min_length=1)
    balance_in_cents: StrictInt  # Must be an integer, no coercion
    transactions: List[str] = Field(default_factory=list)
```

**Explanation:**

- **`balance_in_cents`:**
  - Changed from `conint(ge=0)` to `StrictInt`, ensuring that only integer types are accepted without coercion from other types like strings or floats.

**Attempting to Instantiate with a Float:**

```python
from bank.models import Account

try:
    account = Account(
        account_id="ACCT123456",
        owner_name="David Lee",
        balance_in_cents=1500.75  # Float instead of int
    )
except ValidationError as e:
    print(e.json())
```

**Output:**

```
[
  {
    "loc": ["balance_in_cents"],
    "msg": "value is not a valid integer",
    "type": "type_error.integer"
  }
]
```


## ✅ Best Practices for Using Pydantic in Banking Applications

### 🏗️ Designing Robust Models

1. **📄 Define Clear Schemas:**
   - Clearly outline the structure of your data models, specifying required fields and their types.
   
2. **🔄 Use Constrained Types:**
   - Leverage Pydantic's constrained types to enforce size, format, and value restrictions.

3. **🔍 Implement Comprehensive Validators:**
   - Utilize both built-in and custom validators to cover all business rules and data integrity constraints.

4. **🛡️ Enforce Strict Typing Where Necessary:**
   - Use `StrictInt`, `StrictStr`, etc., to prevent unintended type coercion, especially for sensitive fields.

### 🧩 Separating Concerns

1. **🔗 Modularize Models:**
   - Organize your models into separate modules/files based on their domain or functionality to enhance maintainability.

2. **🧱 Use Composition Over Inheritance When Appropriate:**
   - While inheritance is powerful, sometimes composing models (nesting) can lead to more flexible and manageable code.

3. **📝 Document Your Models:**
   - Provide clear docstrings and comments within your models to explain the purpose of each field and any validation logic.


## 💬 Discussion Topic

**Considerations for Handling Sensitive Financial Data:**

- **Data Privacy:** How do you ensure that sensitive information like account numbers and routing numbers are handled securely within your models and throughout your application?
  
- **Error Handling:** What strategies can you implement to gracefully handle validation errors without exposing sensitive information to end-users or logs?

- **Extensibility:** As banking regulations evolve, how can your Pydantic models adapt to incorporate new validation rules or data fields without disrupting existing functionalities?


## 🎯 Conclusion

Runtime data validation is a critical aspect of developing reliable and secure banking applications. **Pydantic** offers a streamlined and efficient way to enforce data integrity through its powerful modeling and validation capabilities. By leveraging Pydantic's features, developers can ensure that their applications handle data consistently and securely, reducing the likelihood of runtime errors and enhancing overall system robustness.

### 🌟 **Key Takeaways:**

1. **🔒 Ensure Data Integrity:**
   - Utilize Pydantic to enforce strict data schemas, preventing malformed or inconsistent data from propagating through your system.

2. **🚀 Enhance Developer Productivity:**
   - Reduce boilerplate validation code, allowing developers to focus on implementing core business logic.

3. **🛡️ Strengthen Security:**
   - Prevent potential vulnerabilities by validating and sanitizing all incoming data, especially from external sources.

4. **📈 Improve Maintainability:**
   - Centralize validation logic within data models, making the codebase easier to manage and extend.

### 🎯 **Final Thoughts:**

Integrating **Pydantic** into your Python projects, particularly in sensitive domains like banking, is a strategic move towards building more secure, reliable, and maintainable applications. Embrace Pydantic's capabilities to elevate your data validation practices, ensuring that your systems not only meet but exceed the standards required for handling critical financial data.

**Happy Coding!** 🚀😊🎉


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


**Author:** Alex Thompson  
**Email:** alex.thompson@example.com 📧

*Note: Replace `Alex Thompson` and `alex.thompson@example.com` with your actual name and email address.*


Feel free to **integrate Pydantic and runtime validation** into your Python projects to harness the full potential of **robust data management**, **security**, and **maintainable code design**! 🚀 Happy coding! 😊🎉


## 🛠️ **Detailed Code Examples**

To ensure clarity and ease of understanding, here's a breakdown of each module and class with complete code examples tailored for a **Bank Management System**.

### 1. `bank/__init__.py`

```python
# bank/__init__.py

from .models import (
    BankDetails,
    Employee,
    Dish,
    SavingsAccount,
    CheckingAccount,
    Account,
    Restaurant,
    Bank
)
```

**📌 Explanation:**

- **Purpose:** Imports essential classes, making them accessible when the package is imported.
- **Usage:** Allows users to import classes directly from the `bank` package, e.g., `from bank import SavingsAccount`.

### 2. `bank/models.py`

```python
# bank/models.py

from pydantic import BaseModel, Field, constr, conint, validator
from typing import List, Optional, Literal
import re

class BankDetails(BaseModel):
    routing_number: constr(regex=r'^\d{9}$')  # Exactly 9 digits
    account_number: constr(regex=r'^\d{10,12}$')  # 10 to 12 digits

class Employee(BaseModel):
    name: constr(min_length=1)
    position: Literal['Teller', 'Manager', 'Loan Officer', 'Customer Service']
    payment_details: Optional[BankDetails] = None

    @validator('payment_details', always=True)
    def check_payment_details(cls, v, values):
        if values.get('position') in ['Manager', 'Loan Officer']:
            if v is None:
                raise ValueError(f"Payment details required for position {values.get('position')}")
        return v

class Dish(BaseModel):
    name: constr(min_length=1, max_length=16)
    price_in_cents: conint(gt=0)
    description: constr(min_length=1, max_length=80)
    picture: Optional[constr(regex=r'^[\w,\s-]+\.[A-Za-z]{3,4}$')] = None  # e.g., "image.png"

class Account(BaseModel):
    account_id: constr(regex=r'^ACCT\d{6}$')  # e.g., ACCT123456
    owner_name: constr(min_length=1)
    balance_in_cents: conint(ge=0)
    transactions: List[str] = Field(default_factory=list)

class SavingsAccount(Account):
    interest_rate: conint(gt=0, lt=100)  # Interest rate as a percentage

    @validator('balance_in_cents')
    def check_min_balance(cls, v):
        if v < 10000:  # Minimum balance of $100
            raise ValueError("Savings account must have a minimum balance of $100.")
        return v

class CheckingAccount(Account):
    overdraft_limit_in_cents: conint(ge=0)  # Overdraft limit

    @validator('overdraft_limit_in_cents')
    def check_overdraft_limit(cls, v):
        if v > 50000:  # Maximum overdraft limit of $500
            raise ValueError("Overdraft limit cannot exceed $500.")
        return v

class Bank(BaseModel):
    name: constr(min_length=1, max_length=50)
    accounts: List[Account]

    @validator('accounts')
    def check_unique_account_ids(cls, v):
        account_ids = [account.account_id for account in v]
        if len(account_ids) != len(set(account_ids)):
            raise ValueError("All account IDs must be unique.")
        return v

class Restaurant(BaseModel):
    name: constr(regex=r'^[A-Za-z0-9 "\']{1,32}$')
    owner_full_name: constr(min_length=1)
    address: constr(min_length=1)
    employees: List[Employee]
    dishes: List[Dish]
    number_of_seats: conint(gt=0)
    offers_to_go: bool
    offers_delivery: bool

    @validator('employees')
    def check_employee_roles(cls, v):
        positions = [employee.position for employee in v]
        if 'Chef' not in positions:
            raise ValueError("At least one Chef is required.")
        if 'Server' not in positions:
            raise ValueError("At least one Server is required.")
        return v

    @validator('dishes')
    def check_unique_dishes(cls, v):
        dish_names = [dish.name for dish in v]
        if len(dish_names) != len(set(dish_names)):
            raise ValueError("Each dish must have a unique name.")
        if len(v) < 3:
            raise ValueError("There must be at least three dishes on the menu.")
        return v
```

**📌 Explanation:**

- **Models Overview:**
  - **`BankDetails`**: Captures routing and account numbers with strict regex patterns.
  - **`Employee`**: Represents bank employees with conditional payment details based on position.
  - **`Dish`**: (Included from previous example) Represents menu items, showing versatility in modeling different domains.
  - **`Account`**: Base account model with unique account IDs.
  - **`SavingsAccount` & `CheckingAccount`**: Derived models with additional constraints.
  - **`Bank`**: Aggregates accounts, ensuring uniqueness of account IDs.
  - **`Restaurant`**: (Included from previous example) Demonstrates cross-domain applicability.

- **Validators:**
  - **`check_payment_details`**: Ensures essential positions have payment details.
  - **`check_min_balance` & `check_overdraft_limit`**: Enforce financial constraints.
  - **`check_unique_account_ids`**: Prevents duplicate accounts within a bank.

### 3. `bank/main.py`

```python
# bank/main.py

from pydantic import ValidationError
from bank.models import Bank, SavingsAccount, CheckingAccount
import yaml

def load_bank_config(filename: str) -> Bank:
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    try:
        bank = Bank(**data)
        print("Bank configuration loaded successfully.")
        return bank
    except ValidationError as e:
        print("Error loading bank configuration:")
        print(e.json())
        raise

def main():
    config_file = 'bank_config.yaml'
    try:
        bank = load_bank_config(config_file)
        # Proceed with using the validated bank data
        print(bank)
    except ValidationError:
        print("Failed to load bank configuration due to validation errors.")

if __name__ == "__main__":
    main()
```

**📌 Explanation:**

- **Function `load_bank_config`:**
  - Reads the YAML configuration file.
  - Attempts to instantiate the `Bank` model with the loaded data.
  - Catches and prints validation errors if any constraints are violated.

- **Function `main`:**
  - Calls `load_bank_config` and handles potential validation failures gracefully.

**Sample YAML Configuration (`bank_config.yaml`):**

```yaml
name: "Global Trust Bank"
accounts:
  - account_id: "ACCT000001"
    owner_name: "Emily Clark"
    balance_in_cents: 150000  # $1,500.00
    transactions:
      - "Deposit: $1,000.00"
      - "Withdrawal: $500.00"
  - account_id: "ACCT000002"
    owner_name: "Michael Brown"
    balance_in_cents: 25000  # $250.00
    interest_rate: 2
    transactions:
      - "Deposit: $2,500.00"
```

**Loading and Validating the Configuration:**

```python
# bank/main.py (continued)

def main():
    config_file = 'bank_config.yaml'
    try:
        bank = load_bank_config(config_file)
        # Example Operations
        print("\ Bank Details")
        print(f"Bank Name: {bank.name}")
        print(f"Number of Accounts: {len(bank.accounts)}\n")

        for account in bank.accounts:
            print(f"Account ID: {account.account_id}")
            print(f"Owner: {account.owner_name}")
            print(f"Balance: ${account.balance_in_cents / 100:.2f}")
            print(f"Transactions: {', '.join(account.transactions)}\n")
    except ValidationError:
        print("Failed to load bank configuration due to validation errors.")

if __name__ == "__main__":
    main()
```

**Sample Output on Successful Load:**

```
Bank configuration loaded successfully.
Bank(name='Global Trust Bank', accounts=[SavingsAccount(account_id='ACCT000001', owner_name='Emily Clark', balance_in_cents=150000, transactions=['Deposit: $1,000.00', 'Withdrawal: $500.00'], interest_rate=2), SavingsAccount(account_id='ACCT000002', owner_name='Michael Brown', balance_in_cents=25000, transactions=['Deposit: $2,500.00'], interest_rate=2)])
 Bank Details
Bank Name: Global Trust Bank
Number of Accounts: 2

Account ID: ACCT000001
Owner: Emily Clark
Balance: $1500.00
Transactions: Deposit: $1,000.00, Withdrawal: $500.00

Account ID: ACCT000002
Owner: Michael Brown
Balance: $250.00
Transactions: Deposit: $2,500.00
```

**Sample Output on Validation Error (e.g., Duplicate Account ID):**

```yaml
# bank_config.yaml (modified to include a duplicate account_id)
accounts:
  - account_id: "ACCT000001"
    owner_name: "Emily Clark"
    balance_in_cents: 150000
    transactions:
      - "Deposit: $1,000.00"
      - "Withdrawal: $500.00"
  - account_id: "ACCT000001"  # Duplicate ID
    owner_name: "Michael Brown"
    balance_in_cents: 25000
    interest_rate: 2
    transactions:
      - "Deposit: $2,500.00"
```

```
Error loading bank configuration:
{
  "detail": [
    {
      "loc": ["accounts"],
      "msg": "All account IDs must be unique.",
      "type": "value_error"
    }
  ]
}
Failed to load bank configuration due to validation errors.
```


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

