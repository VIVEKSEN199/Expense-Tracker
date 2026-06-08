import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    expenses = load_expenses()

    expense = {
        "title": input("Expense Title: "),
        "category": input("Category: "),
        "amount": float(input("Amount: "))
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense Added Successfully!")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No Expenses Found")
        return

    total = 0

    for expense in expenses:
        print("-" * 30)
        print("Title:", expense["title"])
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])

        total += expense["amount"]

    print("-" * 30)
    print("Total Expense:", total)

def category_wise_expense():
    expenses = load_expenses()

    category_total = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    print("\nCategory Wise Expenses")
    print("-" * 30)

    for category, total in category_total.items():
        print(category, ":", total)

def delete_expense():
    expenses = load_expenses()

    title = input("Enter Expense Title to Delete: ")

    for expense in expenses:
        if expense["title"].lower() == title.lower():
            expenses.remove(expense)
            save_expenses(expenses)

            print("Expense Deleted Successfully!")
            return

    print("Expense Not Found")

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Wise Summary")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_wise_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")