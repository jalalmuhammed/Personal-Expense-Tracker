# 💸 Personal Expense Tracker (Python CLI App)

This is a command-line based **Personal Expense Tracker** written in Python. It allows users to:

- Add, edit, and delete expense records
- Filter expenses by category or date range
- Summarize monthly or category-wise spending
- Export summaries to CSV
- View all transactions and total spending

---

## 📁 Project Structure

```
📂 PersonalExpenseTracker
├── main.py              # Entry point and CLI menu logic
├── utils.py             # Utility functions (validation, sorting, etc.)
├── data_manager.py      # Data CRUD operations
├── constants.py         # Constants and global settings
├── reporter.py          # Filtering and summarizing logic
├── data/Expenses.json   # Auto-generated storage for expenses
└── Exported summaries/  # Output folder for exported CSV files
```

---

## 🚀 Features

- ✅ Add new expenses with date, amount, category, and description
- 🔍 View all expenses (optionally sorted by date)
- 📅 Filter by date range or by category
- 📊 Summarize expenses by category and month
- 📁 Export reports to `.csv` format

---

## 🛠️ How to Run

Make sure you have Python 3.x installed.

```bash
git clone https://github.com/jalalmuhammed/Personal-Expense-Tracker
cd Personal-Expense-Tracker
python main.py
```

---

## 📦 Dependencies

No external libraries required. Uses only Python’s standard library:
- `json`
- `csv`
- `os`
- `uuid`
- `datetime`

---

## 🙌 Author

  Jalal_Muhammed
