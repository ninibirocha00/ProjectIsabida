import datetime
import json
import os

class ExpenseTracker:
    def __init__(self, file_name="transactions.json"):
        self.file_name = file_name
        self.transactions = []
        self.load_transactions()
    
    def load_transactions(self):
        # Load transactions from JSON file
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                try:
                    self.transactions = json.load(file)
                except json.JSONDecodeError:
                    self.transactions = []  # Handle empty or corrupted JSON file
        else:
            with open(self.file_name, 'w') as file:
                json.dump([], file)  # Initialize with empty list
    
    def save_transaction(self, transaction):
        # Save transaction to JSON file
        self.transactions.append(transaction)
        with open(self.file_name, 'w') as file:
            json.dump(self.transactions, file, indent=4)
    
    def add_transaction(self):
        transaction_type = input("Enter transaction type (income/expense): ").lower()
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., groceries, rent, salary, savings): ").lower()
        date = input("Enter date (YYYY-MM-DD): ")

        # Ensure the date is in the correct format
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")  # Check if the date is valid
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        transaction = {
            'type': transaction_type,
            'amount': amount,
            'category': category,
            'date': date
        }
        self.save_transaction(transaction)
        print("Transaction added successfully!")
    
    def view_transactions(self, period):
        income = 0
        expenses = {}
        for transaction in self.transactions:
            if period == 'all' or transaction['date'] == period:
                if transaction['type'] == 'income':
                    income += transaction['amount']
                elif transaction['type'] == 'expense':
                    if transaction['category'] not in expenses:
                        expenses[transaction['category']] = 0
                    expenses[transaction['category']] += transaction['amount']
        
        savings = income - sum(expenses.values())
        
        print(f"\n{period.capitalize()}:")
        print(f"Income: ${income:.2f}")
        print("Expenses:")
        for category, amount in expenses.items():
            print(f"  {category.capitalize()}: ${amount:.2f}")
        print(f"Savings: ${savings:.2f}\n")
    
    def calculate_totals(self, period):
        income = 0
        expenses = 0
        for transaction in self.transactions:
            if period == 'all' or transaction['date'] == period:
                if transaction['type'] == 'income':
                    income += transaction['amount']
                elif transaction['type'] == 'expense':
                    expenses += transaction['amount']
        
        savings = income - expenses
        print(f"\n{period.capitalize()} Totals:")
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Total Savings: ${savings:.2f}\n")
    
    def clear_transactions(self):
        self.transactions = []
        with open(self.file_name, 'w') as file:
            json.dump([], file)  # Clear the transactions file
        print("All transactions cleared!")
    
    def run(self):
        while True:
            print("\nExpense Tracker System")
            print("1. Add Transaction (income/expense)")
            print("2. View Transactions (day/month/all)")
            print("3. Calculate Totals (day/month/all)")
            print("4. Clear All Transactions")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_transaction()
            elif choice == '2':
                period = input("Enter period to view (day/month/all): ").lower()
                self.view_transactions(period)
            elif choice == '3':
                period = input("Enter period to calculate totals (day/month/all): ").lower()
                self.calculate_totals(period)
            elif choice == '4':
                self.clear_transactions()
            elif choice == '5':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

tracker = ExpenseTracker()
tracker.run()
