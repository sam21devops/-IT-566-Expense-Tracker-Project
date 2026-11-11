# expense tracker - load and save

import json

expenses = []

def load_expenses():
    try:
        f = open("expenses.json", "r")
        data = json.load(f)
        f.close()
        return data
    except:
        return []

def main():
    global expenses
    expenses = load_expenses()
    print("Welcome To Expense Tracker Project")
    print("loaded", len(expenses), "expenses from file")
    
    while True:
        print()
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Filter by category")
        print("4. Save to file")
        print("5. Exit")
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
                    print(e["date"], "-", e["category"], "-", e["amount"])
        elif choice == "3":
            cat = input("enter category to filter: ")
            print("filtered expenses:")
            found = False
            for e in expenses:
                if e["category"].lower() == cat.lower():
                    print(e["date"], e["category"], e["amount"])
                    found = True
            if found == False:
                print("nothing found")
        elif choice == "4":
            f = open("expenses.json", "w")
            json.dump(expenses, f)
            f.close()
            print("saved to expenses.json")
        elif choice == "5":
            print("bye")
            break
        else:
            print("wrong choice try again")

if __name__ == "__main__":
    main()
