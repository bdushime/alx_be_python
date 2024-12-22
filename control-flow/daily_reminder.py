
# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case to handle priority levels
match priority:
    case "high":
        message = f"'{task}' is a high priority task."
    case "medium":
        message = f"'{task}' is a medium priority task."
    case "low":
        message = f"'{task}' is a low priority task."
    case _:
        message = "Invalid priority entered."

# Add time sensitivity to the message
if time_bound == "yes":
    message += " It requires immediate attention today!"
elif time_bound == "no":
    message += " Consider completing it when you have free time."

# Display the reminder
print("\nReminder:")
print(message)
