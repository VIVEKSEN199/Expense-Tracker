# Expense-Tracker
# 💰 Smart Expense Tracker with Category Analytics

An advanced, terminal-based *Expense Tracker* application built with Python. This project is designed to help users log their daily expenses, automatically calculate total spending, and view a dynamic *category-wise financial summary* using persistent JSON storage.

---

## 🚀 Key Features

- *➕ Add Expense:* Quick entry for expenses with Title, Category, and Amount (supports decimals).
- *📋 View Expenses:* Displays a clean list of all expenses along with an auto-calculated *Grand Total*.
- *📊 Category Wise Summary:* Smartly aggregates and displays total spending per category (e.g., Food, Travel, Rent) using Python dictionary tracking.
- *❌ Case-Insensitive Delete:* Safely deletes expenses by title without worrying about uppercase or lowercase errors.

---

## 🛠️ Tech Stack & Advanced Concepts

* *Language:* Python 3
* *Database/Storage:* JSON File Handling (json.dump & json.load) for structured and lightweight data persistence.
* *Data Types:* Utilizes *Lists of Dictionaries* for storing records, and *Dynamic Dictionaries* for compiling category-wise totals.
* *Data Robustness:* Implements float() conversion for accurate financial math and .lower() for robust text-matching during deletion.

---

## 📂 Code Logic & Architecture

1. *load_expenses()*: Safely checks for the existence of expenses.json using the os module to prevent crashes on the first run.
2. *category_wise_expense()*: Loops through the database and dynamically builds a key-value dictionary (category: total_amount) to provide instant financial analytics.
3. *Data Integrity*: Automatically overwrites and syncs the JSON file with proper indentation (indent=4) whenever an expense is added or deleted.

---

## 💻 How To Run

1. Clone or download the
2.
