def generate_daily_reminder():
    """
    Prompts the user for a task, its priority, and time-sensitivity,
    then provides a customized reminder using match-case and if statements.
    """
    # 1. Prompt for a Single Task
    task = input("Enter your task: ")
    
    # Standardize priority input for comparison
    priority = input("Priority (high/medium/low): ").lower().strip()
    
    # Standardize time_bound input for boolean check
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Determine the base reminder message using match-case based on priority
    base_message = f"Note: '{task}' is a {priority} priority task."
    
    match priority:
        case 'high':
            # High priority tasks need strong phrasing
            base_message = f"Reminder: '{task}' is a high priority task"
        case 'medium':
            base_message = f"Reminder: '{task}' is a medium priority task. Try to schedule it soon."
        case 'low':
            base_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            # Handle unknown priority input
            base_message = f"Warning: '{task}' has an unrecognized priority ('{priority}')."

    # 2. Process the Task Based on Priority and Time Sensitivity
    final_message = base_message
    
    # Use an if statement to modify the message if the task is time-bound
    if time_bound == 'yes':
        # Check if the base message structure allows appending the immediate attention phrase
        if priority in ['high', 'medium', 'low']:
            # For known priorities, specifically add the immediate attention phrase
            # This is particularly effective for high and medium priority tasks.
            # We explicitly replace the end of the high priority message to fit the required phrase.
            if priority == 'high':
                 final_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            elif priority == 'medium':
                final_message = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
            elif priority == 'low':
                # Even if low, if it's time-bound, it gets a slight bump
                final_message = f"Note: '{task}' is a time-bound low priority task. Aim to complete it today."
        else:
            # For unrecognized priority, just add the time-bound note
            final_message += " It is also marked as time-bound."

    # 3. Provide a Customized Reminder
    print("\n" + final_message)

    # Required conclusion text
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("🚀 Click here to tweet! 🚀")


# Execute the function
if __name__ == "__main__":
    generate_daily_reminder()
