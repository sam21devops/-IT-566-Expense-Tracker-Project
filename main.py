# expense tracker - still learning

expenses = []

def main():
    print("Welcome To Expense Tracker Project")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        # I think this is how to store it
        expenses.append(amount)
        expenses.append(category)
        expenses.append(date)
        print("expense added!!")
    elif choice == "2":
        print("here are your expenses:")
        print(expenses)
    elif choice == "3":
        print("bye")
    else:
        print("wrong choice")

if __name__ == "__main__":
    main()
