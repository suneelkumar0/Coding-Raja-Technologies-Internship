import os
import json

# File to store transactions
DATA_FILE = "budget_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        return data
    else:
        return {'income': 0, 'expenses': []}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

def display_menu():
    print("\n*** Budget Tracker Menu ***")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Budget")
    print("4. Expense Analysis")
    print("5. Exit")

def record_income(data):
    income_amount = float(input("Enter income amount: "))
    data['income'] += income_amount
    print(f"Income of ${income_amount} recorded successfully.")

def record_expense(data):
    expense_category = input("Enter expense category: ")
    expense_amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': expense_category, 'amount': expense_amount})
    print(f"Expense of ${expense_amount} in category '{expense_category}' recorded successfully.")

def view_budget(data):
    remaining_budget = data['income'] - sum(item['amount'] for item in data['expenses'])
    print(f"\nRemaining Budget: ${remaining_budget}")

def expense_analysis(data):
    expense_categories = set(item['category'] for item in data['expenses'])
    
    print("\n*** Expense Analysis ***")
    for category in expense_categories:
        category_expenses = [item['amount'] for item in data['expenses'] if item['category'] == category]
        total_category_expenses = sum(category_expenses)
        print(f"{category}: ${total_category_expenses}")

def main():
    data = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            record_income(data)
        elif choice == '2':
            record_expense(data)
        elif choice == '3':
            view_budget(data)
        elif choice == '4':
            expense_analysis(data)
        elif choice == '5':
            save_data(data)
            print("Budget data saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

