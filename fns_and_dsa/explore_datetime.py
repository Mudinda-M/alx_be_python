from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    date_formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", date_formatted)
    return current_date

def calculate_future_date(current_date):
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
