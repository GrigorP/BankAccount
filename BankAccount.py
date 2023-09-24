import json
import os

class BankAccount:
    def __init__(self):
        # Initialize an empty dictionary to store account information
        self.accounts = {}
        # Load existing accounts from a JSON file (if it exists)
        self.load_accounts()

    def load_accounts(self):
        # This function loads accounts from a JSON file into the accounts dictionary.
        if os.path.exists('accounts.json'):
            with open('accounts.json', 'r') as file:
                self.accounts = json.load(file)

    def save_accounts(self):
        # This function saves the account information to a JSON file.
        with open('accounts.json', 'w') as file:
            json.dump(self.accounts, file)

    def register(self, username, password):
        # Register a new user with the provided username and password.
        if username in self.accounts:
            print("Username already exists!")
            return False
        self.accounts[username] = {
            'password': password,
            'balance': 0
        }
        # Save the updated account information to the JSON file.
        self.save_accounts()
        print("Registration successful!")
        return True

    def login(self, username, password):
        # Log in a user with the provided username and password.
        if username not in self.accounts:
            print("Username does not exist!")
            return False
        if self.accounts[username]['password'] != password:
            print("Incorrect password!")
            return False
        print("Login successful!")
        return True

    def deposit(self, username, amount):
        # Deposit a specified amount into the user's account.
        if username not in self.accounts:
            print("Username does not exist!")
            return
        self.accounts[username]['balance'] += amount
        # Save the updated account balance to the JSON file.
        self.save_accounts()
        print(f"Deposited ${amount}. New balance: ${self.accounts[username]['balance']}")

    def withdraw(self, username, amount):
        # Withdraw a specified amount from the user's account.
        if username not in self.accounts:
            print("Username does not exist!")
            return
        if self.accounts[username]['balance'] < amount:
            print("Insufficient funds!")
            return
        self.accounts[username]['balance'] -= amount
        # Save the updated account balance to the JSON file.
        self.save_accounts()
        print(f"Withdrew ${amount}. New balance: ${self.accounts[username]['balance']}")

    def check_balance(self, username):
        # Check and display the current balance of the user's account.
        if username not in self.accounts:
            print("Username does not exist!")
            return
        print(f"Balance: ${self.accounts[username]['balance']}")

# Create an instance of the BankAccount class
bank = BankAccount()

# Example usage:
bank.register("superuser", "qwerty")
bank.login("superuser", "qwerty")
bank.deposit("superuser", 100)
bank.withdraw("superuser", 50)
bank.check_balance("superuser")

bank.register("user", 'qwert')
bank.login("user", "qwert")
bank.deposit("user", 200)
bank.withdraw("user", 30)
bank.check_balance("user")