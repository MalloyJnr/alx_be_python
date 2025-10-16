# daily_reminder.py

def get_user_input():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unknown priority level"

    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    return message

# Main Loop (confirming input)
while True:
    task, priority, time_bound = get_user_input()

    print("\nYou entered:")
    print(f"Task: {task}")
    print(f"Priority: {priority}")
    print(f"Time-bound: {time_bound}")

    confirm = input("Is this correct? (yes/no): ").strip().lower()
    if confirm == "yes":
        break
    else:
        print("\nLet's try again.\n")

# Display Reminder (correct format)
reminder = generate_reminder(task, priority, time_bound)
print(f"Reminder: {reminder}")
