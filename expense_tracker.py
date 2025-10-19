# Define the class to manage expenses
class ExpensesTracker:
    
    # Constructor: initializes empty dictionaries for tracking expenses and categories
    def __init__(self):
        self.expenses = {}      # Stores total expenses per category
        self.categories = {}    # Stores detailed expenses for each category

    # Method to add a new expense
    def add_expense(self, amount, category, description=""):
        # If category doesn't exist, create it
        if category not in self.categories:
            self.categories[category] = []
        
        # Create a new expense entry
        expense = {
            "amount": amount,
            "description": description
        }
        
        # Add expense to the category list
        self.categories[category].append(expense)
        
        # Initialize category total if it doesn't exist
        self.expenses.setdefault(category, 0)
        
        # Add the new expense amount to the category total
        self.expenses[category] += amount
        
        # Print confirmation message
        print(f"✅ Added to category: {category}")

    # Method to get all expenses by category
    def get_expenses_by_category(self, category):
        return self.categories.get(category, [])

    # Method to calculate total expenses across all categories
    def get_total_expenses(self):
        return sum(self.expenses.values())


# ===============================
# Main Program starts here
# ===============================
if __name__ == "__main__":
    # Create a new instance of the tracker
    tracker = ExpensesTracker()

    # Infinite loop until user chooses to exit
    while True:
        print("\n💰 Expense Tracker Menu:")
        print("1️⃣  Add Expense")
        print("2️⃣  View Expenses by Category")
        print("3️⃣  View Total Expenses")
        print("4️⃣  Exit")

        # Ask for user choice
        choice = input("👉 Choose an option: ")

        # Option 1: Add a new expense
        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description (optional): ")
            tracker.add_expense(amount, category, description)
            print("✅ Expense added successfully!")

        # Option 2: View all expenses in a specific category
        elif choice == '2':
            category = input("Enter category to view expenses: ")
            expenses = tracker.get_expenses_by_category(category)
            
            # Check if category has any expenses
            if expenses:
                print(f"\n📂 Expenses in category '{category}':")
                for exp in expenses:
                    print(f"- Amount: {exp['amount']}, Description: {exp['description']}")
            else:
                print(f"⚠️ No expenses found in category '{category}'.")

        # Option 3: Show total expenses across all categories
        elif choice == '3':
            total = tracker.get_total_expenses()
            print(f"💵 Total expenses: {total}")

        # Option 4: Exit the program
        elif choice == '4':
            print("👋 Exiting Expense Tracker. Goodbye!")
            break

        # Handle invalid input
        else:
            print("❌ Invalid choice. Please try again.")
