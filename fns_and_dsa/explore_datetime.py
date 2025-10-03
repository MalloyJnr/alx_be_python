from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and display it
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        # Prompt user for number of days
        days = int(input("Enter the number of days to add to the current date: "))
        # Calculate future date
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        # Display future date in YYYY-MM-DD format
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
