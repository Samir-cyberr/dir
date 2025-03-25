import json
import os
from uuid import uuid4


class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nBalance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return None
        
        account_number = str(uuid4())
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created successfully. Your account number is: {account_number}")
        return account_number
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return False
        
        if account.deposit(amount):
            self.save_to_file()
            print(f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}")
            return True
        else:
            print("Invalid deposit amount.")
            return False
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return False
        
        if account.withdraw(amount):
            self.save_to_file()
            print(f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}")
            return True
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            return False
    
    def save_to_file(self):
        accounts_data = []
        for account in self.accounts.values():
            accounts_data.append({
                'account_number': account.account_number,
                'name': account.name,
                'balance': account.balance
            })
        
        with open('accounts.txt', 'w') as f:
            json.dump(accounts_data, f)
    
    def load_from_file(self):
        if not os.path.exists('accounts.txt'):
            return
        
        try:
            with open('accounts.txt', 'r') as f:
                accounts_data = json.load(f)
            
            for account_data in accounts_data:
                account = Account(
                    account_data['account_number'],
                    account_data['name'],
                    account_data['balance']
                )
                self.accounts[account.account_number] = account
        except Exception as e:
            print(f"Error loading accounts: {e}")


def bank_menu():
    bank = Bank()
    
    while True:
        print("\nBank Application Menu:")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: $"))
            bank.create_account(name, initial_deposit)
        
        elif choice == '2':
            account_number = input("Enter your account number: ")
            bank.view_account(account_number)
        
        elif choice == '3':
            account_number = input("Enter your account number: ")
            amount = float(input("Enter deposit amount: $"))
            bank.deposit(account_number, amount)
        
        elif choice == '4':
            account_number = input("Enter your account number: ")
            amount = float(input("Enter withdrawal amount: $"))
            bank.withdraw(account_number, amount)
        
        elif choice == '5':
            print("Thank you for using our bank application!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bank_menu()