from expense import Expense
import time

def main():
    print("Welcome to Personal Expense Tracker")

    #get user input
    expense = user_input()

    #write to csv file
    file_path = "Expense.csv"
    write_to_csv(file_path, expense)

    #summary to the user
    summary(file_path)

def user_input():
    print("Getting user input")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount ($): "))

    categories = {
        "1": "Food",
        "2": "Home",
        "3": "Work",
        "4": "Fun",
        "5": "Misc"
    }
    for keys, values in categories.items():
        print(f"{keys}. {values}")
    while True:
        try:
            selection_range = f"1 - {len(categories)}"
            selected_category = int(input(f"Enter a category number ({selection_range}): "))
            print(f"You have added {categories[str(selected_category)]}, (${expense_amount:.2f}) to your expense.")
            new_expense = Expense(
                name = expense_name,
                category = categories[str(selected_category)],
                amount = expense_amount
            )
            return new_expense
        except KeyError:
            print("Enter the number form the range")
        except ValueError:
            print("Please! Enter a number")
        else:
            print("Invalid Category")


def write_to_csv(path, expenses):
    with open(path, "a") as f:
        f.write(f"{expenses.name},{expenses.amount},{expenses.category} \n")


def summary(file_path):
    print("writing summary")
    with open(file_path, "r") as f:
        lines = f.readlines()
        total_expense = 0
       # print(lines)            #['khaja,34.0,Home \n', 'kahaja,34.0,Home \n', 'khaja,23.0,Home \n']
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, categories = stripped_line.split(",")
            total_expense +=  float(expense_amount)
        print(f"Your total expenditure this month is {total_expense}.")

if __name__ == "__main__":
    main()