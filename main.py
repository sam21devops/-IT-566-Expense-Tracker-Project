# expense tracker - trying to make menu loop

expenses = []

def main():
    print("Welcome To Expense Tracker Project")
    
    while True:
        print()
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            expense = {"amount": amount, "category": category, "date": date}
            expenses.append(expense)
            print("expense added!!")
        elif choice == "2":
            print("here are your expenses:")
            if len(expenses) == 0:
                print("no expenses yet")
            else:
                for e in expenses:
                    print(e)
        elif choice == "3":
            print("bye")
            break
        else:
            print("wrong choice try again")

if __name__ == "__main__":
    main()
