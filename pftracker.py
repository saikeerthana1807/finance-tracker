import json
import os
from datetime import datetime

DATA_FILE = "transactions.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_transaction(data):
    t_type = input("Type (income/expense): ").strip().lower()
    amount = float(input("Amount: "))
    category = input("Category: ")
    desc = input("Description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    data.append({
        "type": t_type,
        "amount": amount,
        "category": category,
        "description": desc,
        "date": date
    })
    print("Transaction added successfully!\n")

def view_balance(data):
    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")
    print(f"\nCurrent Balance: ₹{income - expense:.2f}\n")

def view_transactions(data):
    print("\n--- All Transactions ---")
    for t in data:
        print(f"{t['date']} | {t['type'].capitalize():8} | ₹{t['amount']:7.2f} | {t['category']} - {t['description']}")
    print()

def summary_by_category(data):
    summary = {}
    for t in data:
        if t["type"] == "expense":
            summary[t["category"]] = summary.get(t["category"], 0) + t["amount"]
    print("\n--- Expenses by Category ---")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt:.2f}")
    print()

def main():
    data = load_data()
    while True:
        print("==== Personal Finance Tracker ====")
        print("1. Add Transaction")
        print("2. View Balance")
        print("3. View All Transactions")
        print("4. View Summary by Category")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            add_transaction(data)
        elif choice == '2':
            view_balance(data)
        elif choice == '3':
            view_transactions(data)
        elif choice == '4':
            summary_by_category(data)
        elif choice == '5':
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid input. Try again.\n")

if __name__ == "__main__":
    main()