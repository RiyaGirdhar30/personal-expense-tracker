import json
from datetime import date, datetime
import matplotlib.pyplot as plt


class ExpenseTracker:

    def __init__(self):
        self.expenses = []
        self.budget = 0

        self.load_expenses()
        self.load_budget()

    def get_valid_date(self, date_input):
        try:
            date_object = datetime.strptime(
                date_input,
                "%d-%m-%Y"
            )

            return date_object.strftime("%d-%m-%Y")

        except ValueError:
            return None

    # Load budget from JSON file
    def load_budget(self):
        try:
            with open("budget.json", "r") as file:
                data = json.load(file)

            self.budget = data["budget"]

        except FileNotFoundError:
            self.budget = 0

    # Save budget to JSON file
    def save_budget(self):
        with open("budget.json", "w") as file:
            json.dump({"budget": self.budget}, file, indent=4)

    # Set monthly budget
    def set_budget(self):

        try:
            budget = float(input("Enter your monthly budget: ₹"))

        except ValueError:
            print("\nPlease enter a valid number.")
            return

        self.budget = budget
        self.save_budget()

        print(f"\nMonthly budget set to ₹{budget}")

    # Show current month's budget status
    def budget_status(self):

        if self.budget == 0:
            print("\nNo monthly budget has been set.")
            return

        current_month = datetime.now().strftime("%m-%Y")

        spent = 0

        for expense in self.expenses:

            expense_date = expense.get("date")

            if expense_date:

                if expense_date[3:] == current_month:
                    spent += expense["amount"]

        remaining = self.budget - spent

        print("\n===== BUDGET STATUS =====")
        print(f"Monthly Budget: ₹{self.budget}")
        print(f"Spent This Month: ₹{spent}")

        if remaining >= 0:
            print(f"Remaining: ₹{remaining}")

        else:
            print(f"Exceeded By: ₹{abs(remaining)}")
            print("⚠️ You have exceeded your monthly budget!")

    # Load expenses from JSON file
    def load_expenses(self):

        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

        except FileNotFoundError:
            self.expenses = []

    # Save expenses to JSON file
    def save_expenses(self):

        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

    # Add an expense
    # Add an expense
    def add_expense(self):

        try:
            amount = float(input("Enter amount: ₹"))

        except ValueError:
            print("\nPlease enter a valid number.")
            return

        if amount <= 0:
            print("\nAmount must be greater than 0.")
            return

        category = input("Enter category: ").strip()

        if category == "":
            print("\nCategory cannot be empty.")
            return

        description = input("Enter description: ").strip()

        if description == "":
            print("\nDescription cannot be empty.")
            return

        date_input = input(
            "Enter date (DD-MM-YYYY) [Press Enter for today]: "
        )

        # If user doesn't enter a date, use today's date
        if date_input == "":
            date = datetime.now().strftime("%d-%m-%Y")

        else:
            date = self.get_valid_date(date_input)

        if date is None:
            print("\nInvalid date format.")
            print("Please use DD-MM-YYYY.")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        self.expenses.append(expense)
        self.save_expenses()

        print("\nExpense Added!")


    # View all expenses
    def view_expenses(self):

        print("\n===== YOUR EXPENSES =====")

        if len(self.expenses) == 0:
            print("No expenses found.")
            return

        for i, expense in enumerate(self.expenses, start=1):

            print(
                f"{i}. ₹{expense['amount']} | "
                f"{expense['category']} | "
                f"{expense['description']} | "
                f"{expense.get('date', 'No date')}"
            )

    # Delete an expense
    def delete_expense(self):

        if len(self.expenses) == 0:
            print("\nNo expenses to delete.")
            return

        self.view_expenses()

        try:
            number = int(input("\nEnter expense number to delete: "))

        except ValueError:
            print("\nPlease enter a valid number.")
            return

        if 1 <= number <= len(self.expenses):

            deleted_expense = self.expenses.pop(number - 1)

            self.save_expenses()

            print(
                f"\nDeleted: ₹{deleted_expense['amount']} "
                f"| {deleted_expense['category']}"
            )

        else:
            print("\nInvalid expense number.")

    # Calculate total spending
    def total_spending(self):

        total = 0

        for expense in self.expenses:
            total += expense["amount"]

        print(f"\nTotal Spending: ₹{total}")

        # Edit an expense
   
    def edit_expense(self):

        if len(self.expenses) == 0:
            print("\nNo expenses to edit.")
            return

        self.view_expenses()

        try:
            number = int(input("\nEnter expense number to edit: "))

        except ValueError:
            print("\nPlease enter a valid number.")
            return

        if number < 1 or number > len(self.expenses):
            print("\nInvalid expense number.")
            return

        expense = self.expenses[number - 1]

        print("\n===== EDIT EXPENSE =====")

        # Update amount
        amount_input = input(
            f"Enter new amount [{expense['amount']}]: ₹"
        )

        if amount_input == "":
            amount = expense["amount"]

        else:
            try:
                amount = float(amount_input)

            except ValueError:
                print("\nPlease enter a valid number.")
                return

            if amount <= 0:
                print("\nAmount must be greater than 0.")
                return

        # Update category
        category = input(
            f"Enter new category [{expense['category']}]: "
        ).strip()

        if category == "":
            category = expense["category"]

        # Update description
        description = input(
            f"Enter new description [{expense['description']}]: "
        ).strip()

        if description == "":
            description = expense["description"]

        # Update date
        date_input = input(
            f"Enter new date [{expense.get('date', 'No date')}]: "
        ).strip()

        if date_input == "":
            date = expense.get(
                "date",
                datetime.now().strftime("%d-%m-%Y")
            )

        else:
            date = self.get_valid_date(date_input)

            if date is None:
                print("\nInvalid date format.")
                print("Please use DD-MM-YYYY.")
                return

        # Save updated expense
        expense["amount"] = amount
        expense["category"] = category
        expense["description"] = description
        expense["date"] = date

        self.save_expenses()

        print("\nExpense updated successfully!")

        # Show spending statistics
    def spending_statistics(self):

        if len(self.expenses) == 0:
            print("\nNo expenses found.")
            return

        amounts = []

        for expense in self.expenses:
            amounts.append(expense["amount"])

        total = sum(amounts)
        average = total / len(amounts)
        highest = max(amounts)
        lowest = min(amounts)

        print("\n===== SPENDING STATISTICS =====")

        print(f"Total Expenses: {len(amounts)}")
        print(f"Total Spent: ₹{total:.2f}")
        print(f"Average Expense: ₹{average:.2f}")
        print(f"Highest Expense: ₹{highest:.2f}")
        print(f"Lowest Expense: ₹{lowest:.2f}")

        # Show spending chart
    def spending_chart(self):

        if len(self.expenses) == 0:
            print("\nNo expenses found.")
            return

        category_totals = {}

        for expense in self.expenses:

            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount

            else:
                category_totals[category] = amount

        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        plt.figure(figsize=(8, 5))

        plt.bar(categories, amounts)

        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")

        plt.xticks(rotation=30)

        plt.tight_layout()

        plt.show()

        # Show monthly spending chart
    def monthly_spending_chart(self):

        if len(self.expenses) == 0:
            print("\nNo expenses found.")
            return

        monthly_totals = {}

        for expense in self.expenses:

            date = expense.get("date")

            if not date:
                continue

            expense_date = datetime.strptime(date, "%d-%m-%Y")

            month = expense_date.strftime("%b-%Y")

            if month in monthly_totals:
                monthly_totals[month] += expense["amount"]

            else:
                monthly_totals[month] = expense["amount"]

        if len(monthly_totals) == 0:
            print("\nNo dated expenses found.")
            return

        months = list(monthly_totals.keys())
        amounts = list(monthly_totals.values())

        plt.figure(figsize=(8, 5))

        plt.plot(months, amounts, marker="o")

        plt.title("Monthly Spending")
        plt.xlabel("Month")
        plt.ylabel("Amount (₹)")

        plt.xticks(rotation=30)

        plt.tight_layout()

        plt.show()

    # Show category-wise spending
    def category_summary(self):

        category_totals = {}

        for expense in self.expenses:

            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount

            else:
                category_totals[category] = amount

        print("\n===== CATEGORY SUMMARY =====")

        if len(category_totals) == 0:
            print("No expenses found.")
            return

        for category, total in category_totals.items():
            print(f"{category}: ₹{total}")

    # Search expenses
    def search_expenses(self):

        search = input(
            "Enter category or description to search: "
        ).lower()

        found = False

        print("\n===== SEARCH RESULTS =====")

        for i, expense in enumerate(self.expenses, start=1):

            category = expense["category"].lower()
            description = expense["description"].lower()

            if search in category or search in description:

                print(
                    f"{i}. ₹{expense['amount']} | "
                    f"{expense['category']} | "
                    f"{expense['description']} | "
                    f"{expense.get('date', 'No date')}"
                )

                found = True

        if not found:
            print("No matching expenses found.")


# Create ExpenseTracker object
tracker = ExpenseTracker()


# Main menu
while True:

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Show Total Spending")
    print("6. Category Summary")
    print("7. Search Expenses")
    print("8. Set Monthly Budget")
    print("9. Budget Status")
    print("10. Spending Statistics")
    print("11. Spending Chart")
    print("12. Monthly Spending Chart")
    print("13. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.edit_expense()

    elif choice == "4":
        tracker.delete_expense()

    elif choice == "5":
        tracker.total_spending()

    elif choice == "6":
        tracker.category_summary()

    elif choice == "7":
        tracker.search_expenses()

    elif choice == "8":
        tracker.set_budget()

    elif choice == "9":
        tracker.budget_status()

    elif choice == "10":
        tracker.spending_statistics()

    elif choice == "11":
        tracker.spending_chart()

    elif choice == "12":
        tracker.monthly_spending_chart()

    elif choice == "13":
        print("\nThank you for using Expense Tracker!")
        break

    else:
        print("\nInvalid choice. Please try again.")