import data_manager
from datetime import datetime

import utils


#filter by category
def filter_by_category(category):
    expenses = data_manager.load_data()
    category = category.strip()
    try:
        filtered_list = []
        for exp in expenses:
            if exp.get("category") == category:
                filtered_list.append(exp)

        if filtered_list is not None:

            #if expense found in given category,displaying to the user by sorting by the date.
            sorted_list = utils.sort_by_date(filtered_list)

            print(f"Expense Entry Found In The Category '{category}'")
            for exp in sorted_list:
                print(exp)

        else:
            print(f"No Expense Entry Found In The Category '{category}'")

    except Exception as e:
        print(f"Error Occurred: {e}")

#filter by date range
def filter_by_date(start_date,end_date):
    expenses = data_manager.load_data()
    filtered_exp_list = []

    # checking whether an expense lies between start and end date.
    for expense in expenses:
        if start_date <= expense["date"] <= end_date:
            filtered_exp_list.append(expense)

    #if expense found in the given date range,display them by sorting by date.
    if filtered_exp_list is not None:
        sorted_list = utils.sort_by_date(filtered_exp_list)

        print(f"Expense Found From {start_date} to {end_date}.")
        for exp in sorted_list:
            print(exp)
    else:
        print(f"No Expense Found From {start_date} to {end_date}.")
