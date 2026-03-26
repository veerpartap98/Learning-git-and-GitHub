import csv
import os



FILENAME = str(input('Enter your account name(account name must end with .csv) : '))


def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Amount", "Category"])

def add_transaction():
    trans_type = input("Enter type (income/expense): ").strip().lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g. food, salary, bills): ").strip()

    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([trans_type, amount, category])

    print("Transaction added successfully!\n")


def view_transactions():
    print("\n=== Transaction History ===")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            print(f"{row[0].capitalize()} of ₹{row[1]} - Category: {row[2]}")
    print()


def view_balance():
    balance = 0
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == "income":
                balance += float(row[1])
            elif row[0] == "expense":
                balance -= float(row[1])
    print(f"\n💰 Current Balance: ₹{balance}\n")


def main():
    init_file()
    while True:
        print("=== Personal Finance Tracker ===")
        print("1. Add Income/Expense")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            view_balance()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
    
main()

