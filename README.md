# 💰 Personal Expense Tracker

A command-line expense management application built with Python that helps users record, manage, search, and analyze their expenses.

## ✨ Features

* **Add Expenses:** Record amounts, categories, descriptions, and dates.
* **View Expenses:** Display saved expense records.
* **Edit Expenses:** Update existing expenses while keeping unchanged fields.
* **Delete Expenses:** Remove unwanted records.
* **Total Spending:** Calculate total expenditure.
* **Category Summary:** Analyze spending by category.
* **Search Expenses:** Find expenses by category or description.
* **Monthly Budget:** Set and monitor a monthly spending budget.
* **Spending Statistics:** Calculate average, highest, and lowest expenses.
* **Spending Charts:** Visualize category-wise and monthly spending.
* **Input Validation:** Handle invalid amounts, dates, and other incorrect inputs.
* **Data Persistence:** Save expenses and budget information in JSON files.

## 🛠️ Technologies Used

* Python
* JSON for data storage
* Matplotlib for data visualization
* `datetime` for date handling

## 📁 Project Structure

```text
ExpenseTracker/
├── expense_tracker.py
├── expenses.json
├── budget.json
├── requirements.txt
└── README.md
```

The JSON files store your expense records and budget. They may be created when the application first saves data.

## ⚙️ Installation and Setup

### Prerequisites

* Python 3 installed
* pip package manager

### Steps

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd ExpenseTracker
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python expense_tracker.py
   ```

## ▶️ How to Use

1. Run the Python file.
2. Choose an option from the menu.
3. Enter the requested expense or budget details.
4. Use the search, summary, statistics, and chart options to analyze spending.
5. Select Exit when finished.

## 📊 Data Visualization

Matplotlib generates charts to help visualize category-wise and monthly spending.

## 🎯 Learning Outcomes

This project demonstrates practical use of:

* Object-oriented programming and classes
* Functions and input validation
* Lists and dictionaries
* File handling and JSON serialization
* Exception handling
* Date parsing and formatting
* Data analysis and visualization

## 🔮 Future Improvements

* Export expense reports to CSV
* Add a graphical user interface
* Support multiple users
* Add expense filtering by custom date ranges

## 👩‍💻 Author

**Riya Girdhar**

* GitHub: [RiyaGirdhar30](https://github.com/RiyaGirdhar30)
* LinkedIn: [Riya Girdhar](https://www.linkedin.com/in/riya-girdhar-a6074124a)
