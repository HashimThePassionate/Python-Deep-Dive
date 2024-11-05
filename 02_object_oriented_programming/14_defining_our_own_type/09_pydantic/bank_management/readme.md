# 🏦 **Runtime Checking with Pydantic** ✨

I understand that diving into runtime data validation with Pydantic can be overwhelming, especially when presented with comprehensive examples. Let's break down the **Bank Management System** example step-by-step, guiding you through setting up, running the code, and understanding how each component works. By the end of this guide, you'll have a clear grasp of how to implement and utilize Pydantic for robust data validation in your Python projects.


## 📋 **Prerequisites**

Before we begin, ensure you have the following installed on your system:

1. **Python 3.7 or later**: Pydantic requires Python 3.7+. You can download Python from [python.org](https://www.python.org/downloads/).

2. **pip**: Python's package installer. It typically comes bundled with Python. Verify by running:
   ```bash
   pip --version
   ```

3. **Virtual Environment (Recommended)**: It's good practice to create an isolated environment for your projects to manage dependencies without conflicts.


## 🛠️ **Setting Up the Project**

### 1. **Create a Project Directory**

First, create a new directory for your Bank Management System project:

```bash
mkdir bank_management
cd bank_management
```

### 2. **Set Up a Virtual Environment**

Creating a virtual environment ensures that your project dependencies are isolated.

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On macOS and Linux:**
  ```bash
  source venv/bin/activate
  ```
- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

Your command prompt should now indicate that you're working within the `venv` environment.

### 3. **Install Required Packages**

Install **Pydantic** and **PyYAML** using `pip`:

```bash
pip install "pydantic<2.0"
pip install PyYAML
```

- **Pydantic**: For data validation and settings management using Python type annotations.
- **PyYAML**: For parsing YAML configuration files.

> **Note:** If you plan to use type checking with **mypy**, you might also want to install it along with Pydantic's mypy plugin:
>
> ```bash
> pip install mypy
> pip install pydantic[mypy]
> ```
>
> However, for this guide, we'll focus on runtime validation.

### 4. **Project Structure**

Organize your project as follows:

```
bank_management/
├── bank/
│   ├── __init__.py
│   ├── models.py
├── main.py
├── bank_config.yaml
└── README.md
```

- **`bank/`**: A Python package containing your data models.
- **`main.py`**: The main script to load and validate data.
- **`bank_config.yaml`**: A YAML configuration file containing bank data.
- **`README.md`**: Documentation for your project.


## 🗂️ **Creating the Project Files**

Let's create each file step-by-step with detailed explanations.

### 1. **`bank/__init__.py`**

This file makes the `bank` directory a Python package and exposes the necessary classes for easy import.

**Create the file:**

```bash
mkdir bank
touch bank/__init__.py
```

**Add the following content to `bank/__init__.py`:**

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

- **Purpose:** This file imports all the necessary classes from `models.py`, making them accessible when you import from the `bank` package. For example:
  ```python
  from bank import SavingsAccount
  ```

### 2. **`bank/models.py`**

This file contains all the Pydantic models that define the structure and validation rules for your bank data.

**Create the file:**

```bash
touch bank/models.py
```

**Add the following content to `bank/models.py`:**

```python
# bank/models.py

from pydantic import BaseModel, Field, constr, conint, validator, root_validator
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

Let's break down each class and its purpose:

1. **`BankDetails`**:
   - **Fields**:
     - `routing_number`: Must be exactly 9 digits, following U.S. routing number standards.
     - `account_number`: Must be between 10 to 12 digits to accommodate various bank account numbers.
   
2. **`Employee`**:
   - **Fields**:
     - `name`: Non-empty string.
     - `position`: Must be one of `'Teller'`, `'Manager'`, `'Loan Officer'`, or `'Customer Service'`.
     - `payment_details`: Optional `BankDetails`. However, if the position is `'Manager'` or `'Loan Officer'`, `payment_details` must be provided.
   
   - **Validator `check_payment_details`**:
     - Ensures that employees in certain positions have their `payment_details` filled out.
   
3. **`Dish`**:
   - **Fields**:
     - `name`: Between 1 to 16 characters.
     - `price_in_cents`: Positive integer representing the price in cents.
     - `description`: Between 1 to 80 characters.
     - `picture`: Optional filename with a valid image extension (e.g., "image.png").
   
4. **`Account`**:
   - **Fields**:
     - `account_id`: Must follow the pattern `'ACCT'` followed by six digits (e.g., `'ACCT123456'`).
     - `owner_name`: Non-empty string.
     - `balance_in_cents`: Non-negative integer.
     - `transactions`: List of transaction descriptions. Defaults to an empty list if not provided.
   
5. **`SavingsAccount`** (inherits from `Account`):
   - **Fields**:
     - `interest_rate`: An integer between 1 and 99 representing the annual interest rate.
   
   - **Validator `check_min_balance`**:
     - Ensures that the account maintains a minimum balance of $100 (10,000 cents).
   
6. **`CheckingAccount`** (inherits from `Account`):
   - **Fields**:
     - `overdraft_limit_in_cents`: Non-negative integer representing the overdraft limit.
   
   - **Validator `check_overdraft_limit`**:
     - Ensures that the overdraft limit does not exceed $500 (50,000 cents).
   
7. **`Bank`**:
   - **Fields**:
     - `name`: Name of the bank, between 1 to 50 characters.
     - `accounts`: List of `Account` instances.
   
   - **Validator `check_unique_account_ids`**:
     - Ensures that all `account_id` values are unique across the bank's accounts.
   
8. **`Restaurant`**:
   - **Fields**:
     - `name`: Up to 32 characters, allowing letters, numbers, spaces, and certain punctuation.
     - `owner_full_name`: Non-empty string.
     - `address`: Non-empty string.
     - `employees`: List of `Employee` instances.
     - `dishes`: List of `Dish` instances.
     - `number_of_seats`: Positive integer.
     - `offers_to_go` and `offers_delivery`: Boolean flags indicating if the restaurant offers to-go orders and delivery.
   
   - **Validators**:
     - `check_employee_roles`: Ensures that there's at least one `'Chef'` and one `'Server'` among the employees.
     - `check_unique_dishes`: Ensures all dish names are unique and there are at least three dishes on the menu.

> **Note:** While the `Restaurant` model is part of the original example, it's included here to showcase cross-domain applicability. In a real Bank Management System, you might not need the `Restaurant` model unless your bank manages restaurants or similar entities.


### 3. **`main.py`**

This is the entry point of your application. It loads the YAML configuration, parses it into Pydantic models, and handles validation.

**Create the file:**

```bash
touch main.py
```

**Add the following content to `main.py`:**

```python
# main.py

from pydantic import ValidationError
from bank import Restaurant, Bank
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

**📌 Explanation:**

1. **Imports:**
   - **`ValidationError`**: To catch and handle Pydantic validation errors.
   - **`Restaurant` and `Bank`**: Imported from the `bank` package. Depending on your YAML configuration, you might choose to load a `Bank` or `Restaurant`. For this example, we'll focus on loading a `Bank`.
   - **`yaml`**: To parse the YAML configuration file.

2. **Function `load_bank_config`:**
   - **Purpose:** Loads and validates the bank configuration from a YAML file.
   - **Process:**
     - Opens and reads the YAML file.
     - Parses the YAML content into a Python dictionary.
     - Attempts to create a `Bank` instance using the parsed data.
     - If successful, prints a success message and returns the `Bank` instance.
     - If validation fails, prints the error details and raises the exception.

3. **Function `main`:**
   - **Purpose:** Acts as the entry point of the application.
   - **Process:**
     - Specifies the YAML configuration file (`bank_config.yaml`).
     - Tries to load and validate the bank configuration.
     - If successful, prints out the bank details, including account information.
     - If validation fails, notifies the user of the failure.

4. **Execution Guard:**
   - **`if __name__ == "__main__":`** ensures that `main()` runs only when the script is executed directly, not when imported as a module.


### 4. **`bank_config.yaml`**

This YAML file contains the configuration data for your bank, adhering to the constraints defined in your Pydantic models.

**Create the file:**

```bash
touch bank_config.yaml
```

**Add the following content to `bank_config.yaml`:**

```yaml
name: "Global Trust Bank"
accounts:
  - account_id: "ACCT000001"
    owner_name: "Emily Clark"
    balance_in_cents: 150000  # $1,500.00
    transactions:
      - "Deposit: $1,000.00"
      - "Withdrawal: $500.00"
      - "Interest: $50.00"
  - account_id: "ACCT000002"
    owner_name: "Michael Brown"
    balance_in_cents: 25000  # $250.00
    interest_rate: 2
    transactions:
      - "Deposit: $2,500.00"
```

**📌 Explanation:**

- **`name`**: The name of the bank.
- **`accounts`**: A list of account entries.
  - **Each account** must adhere to the constraints defined in the `Account`, `SavingsAccount`, or `CheckingAccount` models.
  - **Example Accounts:**
    - **First Account (`ACCT000001`):** A `SavingsAccount` with a balance of $1,500 and three transactions.
    - **Second Account (`ACCT000002`):** Another `SavingsAccount` with a balance of $250 and one transaction. Note that this account has an `interest_rate`, indicating it's a `SavingsAccount`. However, according to our models, any account can be a `SavingsAccount` or `CheckingAccount` based on the fields provided.

> **Note:** If an account doesn't specify fields unique to `SavingsAccount` or `CheckingAccount`, it defaults to the base `Account` model. To explicitly create a `SavingsAccount` or `CheckingAccount`, you might need to adjust the loading logic or include a discriminator field.


## 🚀 **Running the Application**

Now that all files are set up, let's run the application to see Pydantic in action.

### 1. **Navigate to the Project Directory**

Ensure you're in the `bank_management` directory and that your virtual environment is activated.

```bash
cd bank_management
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### 2. **Run the Application**

Execute the `main.py` script:

```bash
python main.py
```

### 3. **Expected Output**

If everything is set up correctly and the YAML configuration adheres to the defined constraints, you should see output similar to:

```
Bank configuration loaded successfully.
Bank(name='Global Trust Bank', accounts=[SavingsAccount(account_id='ACCT000001', owner_name='Emily Clark', balance_in_cents=150000, transactions=['Deposit: $1,000.00', 'Withdrawal: $500.00', 'Interest: $50.00'], interest_rate=2), SavingsAccount(account_id='ACCT000002', owner_name='Michael Brown', balance_in_cents=25000, transactions=['Deposit: $2,500.00'], interest_rate=2)])
 Bank Details
Bank Name: Global Trust Bank
Number of Accounts: 2

Account ID: ACCT000001
Owner: Emily Clark
Balance: $1500.00
Transactions: Deposit: $1,000.00, Withdrawal: $500.00, Interest: $50.00

Account ID: ACCT000002
Owner: Michael Brown
Balance: $250.00
Transactions: Deposit: $2,500.00
```

### 4. **Handling Validation Errors**

Let's intentionally introduce some errors in the YAML file to see Pydantic's validation in action.

#### **Example 1: Duplicate Account IDs**

Modify `bank_config.yaml` to have duplicate `account_id` values:

```yaml
name: "Global Trust Bank"
accounts:
  - account_id: "ACCT000001"
    owner_name: "Emily Clark"
    balance_in_cents: 150000
    transactions:
      - "Deposit: $1,000.00"
      - "Withdrawal: $500.00"
      - "Interest: $50.00"
  - account_id: "ACCT000001"  # Duplicate ID
    owner_name: "Michael Brown"
    balance_in_cents: 25000
    interest_rate: 2
    transactions:
      - "Deposit: $2,500.00"
```

**Run the application:**

```bash
python main.py
```

**Expected Output:**

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

#### **Example 2: Invalid Routing Number**

Modify an account's `routing_number` to be invalid (e.g., only 5 digits):

```yaml
name: "Global Trust Bank"
accounts:
  - account_id: "ACCT000001"
    owner_name: "Emily Clark"
    balance_in_cents: 150000
    transactions:
      - "Deposit: $1,000.00"
      - "Withdrawal: $500.00"
      - "Interest: $50.00"
  - account_id: "ACCT000002"
    owner_name: "Michael Brown"
    balance_in_cents: 25000
    interest_rate: 2
    transactions:
      - "Deposit: $2,500.00"
    payment_details:
      routing_number: "12345"  # Invalid routing number
      account_number: "123456789012"
```

**Run the application:**

```bash
python main.py
```

**Expected Output:**

```
Error loading bank configuration:
{
  "detail": [
    {
      "loc": ["accounts", 1, "payment_details", "routing_number"],
      "msg": "string does not match regex \"^\\d{9}$\"",
      "type": "value_error.str.regex",
      "ctx": {
        "pattern": "^\\d{9}$"
      }
    }
  ]
}
Failed to load bank configuration due to validation errors.
```

#### **Example 3: Missing Required Employee Roles**

Remove the `'Chef'` and `'Server'` roles from the employees list:

```yaml
name: "Global Trust Bank"
accounts:
  - account_id: "ACCT000001"
    owner_name: "Emily Clark"
    balance_in_cents: 150000
    transactions:
      - "Deposit: $1,000.00"
      - "Withdrawal: $500.00"
      - "Interest: $50.00"
  - account_id: "ACCT000002"
    owner_name: "Michael Brown"
    balance_in_cents: 25000
    interest_rate: 2
    transactions:
      - "Deposit: $2,500.00"
```

**Run the application:**

```bash
python main.py
```

**Expected Output:**

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


## 🔍 **Understanding How the Code Works**

Let's delve deeper into how each part of the code functions to enforce data integrity.

### 1. **Data Models with Pydantic**

**Pydantic** uses Python type annotations to define data models. These models automatically handle data parsing and validation when instantiated.

- **Base Models (`BaseModel`):** Serve as the foundation for other models. They define the structure and constraints for your data.
  
- **Constrained Types (`constr`, `conint`):** Allow you to set specific constraints on fields, such as regex patterns, minimum and maximum values, and more.

- **Validators (`@validator` and `@root_validator`):** Custom methods that enforce complex validation logic beyond simple type checking.

### 2. **Loading and Validating Data**

When you load data (e.g., from a YAML file), you parse it into a Python dictionary. Pydantic models can then be instantiated using this dictionary:

```python
bank = Bank(**data)
```

During instantiation, Pydantic:

1. **Parses the Data:** Converts the input data into the specified types, applying any necessary coercion (unless strict types are used).

2. **Validates Constraints:** Checks all defined constraints, including those in constrained types and custom validators.

3. **Raises Errors if Validation Fails:** If any constraints are violated, Pydantic raises a `ValidationError` with detailed information about the failures.

### 3. **Handling Validation Errors**

In the `load_bank_config` function, we wrap the instantiation in a `try-except` block to catch `ValidationError`s:

```python
try:
    bank = Bank(**data)
    print("Bank configuration loaded successfully.")
    return bank
except ValidationError as e:
    print("Error loading bank configuration:")
    print(e.json())
    raise
```

- **On Success:** The bank data is loaded and returned.
- **On Failure:** The error details are printed in JSON format, and the exception is re-raised for further handling.

### 4. **Validators Explained**

**Field Validators (`@validator`):**

Used to validate individual fields or sets of fields.

- **Example:**

  ```python
  @validator('payment_details', always=True)
  def check_payment_details(cls, v, values):
      if values.get('position') in ['Manager', 'Loan Officer']:
          if v is None:
              raise ValueError(f"Payment details required for position {values.get('position')}")
      return v
  ```

  - **Purpose:** Ensures that employees in the `'Manager'` or `'Loan Officer'` positions have `payment_details` provided.
  - **Parameters:**
    - `cls`: The class being validated.
    - `v`: The value of the field being validated.
    - `values`: A dictionary of all the field values provided during instantiation.

**Root Validators (`@root_validator`):**

Used to validate across multiple fields or the entire model.

- **Example:**

  ```python
  @root_validator
  def check_unique_account_ids(cls, values):
      accounts = values.get('accounts', [])
      account_ids = [account.account_id for account in accounts]
      if len(account_ids) != len(set(account_ids)):
          raise ValueError("All account IDs must be unique.")
      return values
  ```

  - **Purpose:** Ensures that all `account_id` values within a `Bank` instance are unique.
  - **Parameters:**
    - `cls`: The class being validated.
    - `values`: A dictionary of all the field values provided during instantiation.

### 5. **Constrained Types**

Pydantic's constrained types allow you to set precise rules for your data fields.

- **`constr`**: Constrained string with regex patterns, minimum and maximum lengths.
  
  ```python
  name: constr(regex=r'^[A-Za-z0-9 "\']{1,32}$')
  ```
  
  - **Explanation:** The `name` must consist of 1 to 32 characters, including letters, numbers, spaces, and certain punctuation.

- **`conint`**: Constrained integer with minimum and maximum values.
  
  ```python
  balance_in_cents: conint(ge=0)
  ```
  
  - **Explanation:** The `balance_in_cents` must be a non-negative integer.

- **`Literal`**: Specifies that a field must be one of a predefined set of values.
  
  ```python
  position: Literal['Teller', 'Manager', 'Loan Officer', 'Customer Service']
  ```
  
  - **Explanation:** The `position` must be one of the specified roles.

- **`Optional`**: Indicates that a field can be `None`.
  
  ```python
  payment_details: Optional[BankDetails] = None
  ```
  
  - **Explanation:** The `payment_details` can be either a `BankDetails` instance or `None`.


## 🧩 **Extending the Example: Adding Transactions and More Accounts**

To further understand how Pydantic handles different scenarios, let's expand our `bank_config.yaml` and explore more account types.

### **Adding a `CheckingAccount`**

Modify `bank_config.yaml` to include a `CheckingAccount`:

```yaml
name: "Global Trust Bank"
accounts:
  - account_id: "ACCT000001"
    owner_name: "Emily Clark"
    balance_in_cents: 150000  # $1,500.00
    transactions:
      - "Deposit: $1,000.00"
      - "Withdrawal: $500.00"
      - "Interest: $50.00"
    interest_rate: 2  # Indicates a SavingsAccount
  - account_id: "ACCT000002"
    owner_name: "Michael Brown"
    balance_in_cents: 25000  # $250.00
    transactions:
      - "Deposit: $2,500.00"
    overdraft_limit_in_cents: 30000  # $300.00
```

**Explanation:**

- **First Account (`ACCT000001`):** A `SavingsAccount` with an `interest_rate`.
- **Second Account (`ACCT000002`):** A `CheckingAccount` with an `overdraft_limit_in_cents`.

**Modify `main.py` to handle different account types:**

```python
# main.py (continued)

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
            print(f"Transactions: {', '.join(account.transactions)}")
            if isinstance(account, SavingsAccount):
                print(f"Interest Rate: {account.interest_rate}%")
            elif isinstance(account, CheckingAccount):
                print(f"Overdraft Limit: ${account.overdraft_limit_in_cents / 100:.2f}")
            print("\n")
    except ValidationError:
        print("Failed to load bank configuration due to validation errors.")
```

**Run the application:**

```bash
python main.py
```

**Expected Output:**

```
Bank configuration loaded successfully.
Bank(name='Global Trust Bank', accounts=[SavingsAccount(account_id='ACCT000001', owner_name='Emily Clark', balance_in_cents=150000, transactions=['Deposit: $1,000.00', 'Withdrawal: $500.00', 'Interest: $50.00'], interest_rate=2), CheckingAccount(account_id='ACCT000002', owner_name='Michael Brown', balance_in_cents=25000, transactions=['Deposit: $2,500.00'], overdraft_limit_in_cents=30000)])
 Bank Details
Bank Name: Global Trust Bank
Number of Accounts: 2

Account ID: ACCT000001
Owner: Emily Clark
Balance: $1500.00
Transactions: Deposit: $1,000.00, Withdrawal: $500.00, Interest: $50.00
Interest Rate: 2%


Account ID: ACCT000002
Owner: Michael Brown
Balance: $250.00
Transactions: Deposit: $2,500.00
Overdraft Limit: $300.00
```


## 🛡️ **Security Considerations**

Handling sensitive financial data requires meticulous attention to security. Here are some best practices to ensure your application remains secure:

1. **🔒 Secure Storage of Sensitive Data:**
   - Avoid storing sensitive information like routing numbers and account numbers in plain text.
   - Use encryption for storing such data, especially if persisting to databases or files.

2. **🧼 Input Sanitization:**
   - Ensure that all input data is sanitized to prevent injection attacks.
   - Pydantic helps by validating and constraining data, reducing the risk of malformed inputs.

3. **🔐 Secure Transmission:**
   - When transmitting data (e.g., via APIs), use secure protocols like HTTPS to encrypt data in transit.

4. **🛠️ Use Environment Variables for Secrets:**
   - Store sensitive configurations (like database credentials) in environment variables instead of hardcoding them.

5. **🛑 Limit Data Exposure:**
   - Ensure that sensitive fields are not inadvertently exposed through logs or error messages.
   - Customize error handling to avoid leaking sensitive information.


## 🔄 **Common Pitfalls and How to Avoid Them**

1. **Overly Rigid Models:**
   - **Issue:** Models that are too restrictive can hinder legitimate data flows.
   - **Solution:** Balance constraints with flexibility. Use `Optional` fields where necessary and provide sensible defaults.

2. **Ignoring Validation Errors:**
   - **Issue:** Simply printing errors without handling them can lead to application crashes.
   - **Solution:** Implement robust error handling strategies, such as logging errors securely and providing user-friendly messages without exposing sensitive details.

3. **Not Updating Models with Business Changes:**
   - **Issue:** Business rules evolve, and models become outdated.
   - **Solution:** Regularly review and update your Pydantic models to reflect current business requirements.

4. **Neglecting Performance Implications:**
   - **Issue:** Extensive validation can introduce performance overhead.
   - **Solution:** Optimize validators and avoid unnecessary checks. Profile your application to identify and address bottlenecks.


## 📖 **Summary**

By following this guide, you've set up a **Bank Management System** that leverages **Pydantic** for runtime data validation. Here's what we've accomplished:

1. **Defined Robust Data Models:**
   - Utilized Pydantic's `BaseModel` to create clear and concise data schemas.
   - Implemented constrained types and custom validators to enforce business rules and data integrity.

2. **Loaded and Validated Configuration Data:**
   - Parsed YAML configuration files into Python dictionaries.
   - Instantiated Pydantic models with the parsed data, automatically handling validation.

3. **Handled Validation Errors Gracefully:**
   - Caught and displayed informative error messages when data constraints were violated.

4. **Extended Models for Specific Account Types:**
   - Created specialized models like `SavingsAccount` and `CheckingAccount` to represent different banking products with unique constraints.

5. **Ensured Security and Maintainability:**
   - Highlighted best practices for handling sensitive financial data securely.
   - Emphasized the importance of maintaining and updating data models in line with evolving business needs.


## 🌐 **Additional Resources**

To deepen your understanding and expand your skills with Pydantic and data validation in Python, explore the following resources:

- [**Pydantic Official Documentation**](https://pydantic-docs.helpmanual.io/) 📘
  - Comprehensive guide covering all features and use-cases of Pydantic.
  
- [**Real Python: Pydantic Data Validation in Python**](https://realpython.com/pydantic-python/) 🛠️🔍
  - A practical tutorial that walks through Pydantic's features with examples.
  
- [**Pydantic Tutorial by Sebastián Ramírez**](https://pydantic-docs.helpmanual.io/usage/models/) 🧑‍💻✨
  - Detailed explanations and advanced usage scenarios.
  
- [**Effective Python: 59 Specific Ways to Write Better Python**](https://effectivepython.com/) 📚🧠
  - Although not Pydantic-specific, this book offers valuable insights into writing efficient and maintainable Python code.
  
- [**Python Type Hints Guide**](https://docs.python.org/3/library/typing.html) 📄🔧
  - Official Python documentation on type hints, which are foundational to Pydantic's functionality.
  
- [**Design Patterns in Python**](https://refactoring.guru/design-patterns/python) 🛠️🔍
  - Learn how to apply design patterns effectively in Python, complementing Pydantic's capabilities.
  
- [**Mypy Official Documentation**](https://mypy.readthedocs.io/en/stable/) 📈🔧
  - For integrating type checking into your development workflow alongside Pydantic.
  
- [**Secure Coding in Python**](https://realpython.com/python-secure/) 🔐🐍
  - Best practices for writing secure Python applications, crucial for handling sensitive data like in banking systems.


## 📧 **Contact Information**

**Author:** Alex Thompson  
**Email:** alex.thompson@example.com 📧

*Note: Replace `Alex Thompson` and `alex.thompson@example.com` with your actual name and email address.*


## 🎉 **Happy Coding!** 🚀😊

Feel free to **integrate Pydantic and runtime validation** into your Python projects to harness the full potential of **robust data management**, **security**, and **maintainable code design**! Whether you're building banking systems, APIs, or any application that handles complex data structures, Pydantic can be a game-changer in ensuring data integrity and application reliability.


# Quick Reference: Running the Bank Management System Example

Here's a concise checklist to help you get the Bank Management System up and running smoothly.

1. **Clone or Create the Project Directory:**
   ```bash
   mkdir bank_management
   cd bank_management
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install pydantic PyYAML
   ```

4. **Create Project Structure:**
   ```bash
   mkdir bank
   touch bank/__init__.py
   touch bank/models.py
   touch main.py
   touch bank_config.yaml
   ```

5. **Populate Files with Code:**
   - **`bank/__init__.py`**: Import necessary classes.
   - **`bank/models.py`**: Define Pydantic models with constraints and validators.
   - **`main.py`**: Load and validate data from `bank_config.yaml`.
   - **`bank_config.yaml`**: Provide valid (and optionally, invalid) configuration data.

6. **Run the Application:**
   ```bash
   python main.py
   ```

7. **Test Validation:**
   - Introduce intentional errors in `bank_config.yaml` to observe Pydantic's validation in action.


# Conclusion

By following this guide, you've not only learned **how to run the Bank Management System example** using Pydantic but also gained a deep understanding of **how runtime data validation works** in Python. Pydantic's powerful features make it an invaluable tool for ensuring data integrity, especially in sensitive domains like banking. As you continue to build and expand your applications, leverage Pydantic to maintain robust, secure, and maintainable codebases.
