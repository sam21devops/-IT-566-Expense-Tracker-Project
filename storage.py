# storage helper - save and load expenses

import json

def load_expenses():
    try:
        f = open("expenses.json", "r")
        data = json.load(f)
        f.close()
        return data
    except:
        print("no saved file found, starting empty")
        return []

def save_expenses(expenses):
    f = open("expenses.json", "w")
    json.dump(expenses, f)
    f.close()
    print("saved to expenses.json")
