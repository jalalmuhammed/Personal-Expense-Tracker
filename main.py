import data_manager
import utils

def print_menu():
    print(
        """
     === Personal Expense Tracker ===
    1. Add new expense
    2. View all expenses
    3. Filter expenses by date range
    4. Filter expenses by category
    5. Edit an expense
    6. Delete an expense
    7. Show monthly summary
    8. Show category summary
    9. Export summaries to CSV
    0. Exit
        """
    )

#Add new expense
def add_entry():
    amount = float(utils.validate_input("Enter Amount: ", utils.validate_amount))
    category = str(utils.validate_input("Enter Category.\n (Food,Travel,Misc,Entertainment): ",
                                        utils.validate_category)).lower()
    description = input("Enter Description,(Press Enter if not): ")
    data_manager.add_new_exp(amount, category, description)

#show all expense
def view_all_exp():
    show_data = data_manager.load_data()
    for doc in show_data:
        print(doc)

#Edit an expense entry
def edit_exp():
    try:
        target_id = input("Enter Expense Id To Edit: ").strip()
        expenses = data_manager.load_data()
        id_list = [e.get("id") for e in expenses]
        if target_id in id_list:
            print("Enter Details To Update entry.\nClick Enter If You Don't Want To Change.")

            while True:
                date = input("Enter New Date: ").strip()
                if date and not utils.validate_date(date):
                    print("enter valid date")
                else:
                    break

            while True:
                amount = input("Enter New Amount: ").strip()
                if amount and not utils.validate_amount(amount):
                    print("Enter valid positive number")
                else:
                    break

            while True:
                category = input("Enter New Category.\n (Food,Travel,Misc,Entertainment): ").strip().lower()
                if category and not utils.validate_category(category):
                    print("Enter valid Category")
                else:
                    break

            description = input("Enter New Description: ")

            if data_manager.edit_expense(target_id,date,amount,category,description):
                print(f"Expense Entry ID: {target_id} Updated Successfully.")

                #Option to verify,whether it got updated
                user_assurance = input("Do You Want To See The Update(Y/N): ").lower()
                if user_assurance == "y":
                    reloaded_expense = data_manager.load_data()
                    updated_exp = [exp for exp in reloaded_expense if exp.get("id") == target_id]
                    print(updated_exp)
                else:
                    print("Thank You.")
            else:
                print(f"Nothing Changed in the ID:{target_id}")

        else:
            print(f"There is No Expense Entry with ID:{target_id}")

    except Exception as e:
        print(f"Error is: {e}")


#delete an expense entry
def delete_entry():
    removable_id = str(input("Enter the id to remove the expense: ").strip())
    if data_manager.delete_expense(removable_id):
        print(f"Expense Entry Deletion Successful.\n ID No: {removable_id} ")

    # user verifying the deletion
    see_update = input("Do you want to see the Updated expense List (y/n): ")
    if see_update.lower() == "y":
        updated_expense = data_manager.load_data()
        for doc in updated_expense:
            print(doc)

#Main loop for menu
def main_loop():
    while True:
        #showing options and taking user input.
        try:
            print_menu()
            choose = int(input("Choose an option: "))

            #Exit the loop
            if choose == 0:
                break

            #Add new expense
            elif choose == 1:
                add_entry()

            #View all expenses
            elif choose == 2:
               view_all_exp()
               break

            #edit an expense
            elif choose == 5:
                edit_exp()

            #Delete an expense
            elif choose == 6:
                delete_entry()
                break

            else:
                print("Invalid option. Please choose a valid menu item.")

        except ValueError:
            print("Enter valid Numerical Value!")


if __name__ == "__main__":
    main_loop()