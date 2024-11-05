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
