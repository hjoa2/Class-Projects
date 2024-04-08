expenses = []
categories = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Clothing', 'Other']

def add():
    try:
        name = input("Enter expense name: ")
        print("Choose a category:")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")
        category_choice = int(input("Enter category number: "))
        if category_choice < 1 or category_choice > len(categories):
            print("Invalid category choice.")
            return
        amount = float(input("Enter expense amount: "))
        category = categories[category_choice - 1]
        expenses.append({'name': name, 'category': category, 'amount': amount})
        print("Expense added successfully.")
    except ValueError:
        print("Error: Amount must be a number.")

def display():
    if not expenses:
        print("No expenses added yet.")
    else:
        print("List of Expenses:")
        print("Name\tCategory\tAmount")
        for expense in expenses:
            print(f"{expense['name']}\t{expense['category']}\t${expense['amount']:.2f}")

def calculate():
    if not expenses:
        print("No expenses added yet.")
    else:
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: ${total:.2f}")

def save():
    file_name = input("Enter file name to save expenses (example: expenses.txt): ")
    try:
        with open(file_name, 'w') as f:
            f.write("Name\tCategory\tAmount\n")
            for expense in expenses:
                f.write(f"{expense['name']}\t{expense['category']}\t{expense['amount']}\n")
        print(f"Expenses saved to {file_name} successfully.")
    except Exception as e:
        print(f"Error occurred while saving expenses: {e}")

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Show Expense")
    print("3. Calculate Total")
    print("4. Save File")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add()
    elif choice == '2':
        display()
    elif choice == '3':
        calculate()
    elif choice == '4':
        save()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
