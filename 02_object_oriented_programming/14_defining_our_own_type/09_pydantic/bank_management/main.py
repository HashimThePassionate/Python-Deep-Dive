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
        print("\n--- Bank Details ---")
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
