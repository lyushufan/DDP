# File: EBEMS.py
# Author: 5550538
# Version: 1.0
# Description: This script implements an Event Management System for managing virtual events.

# Dependencies: This script requires the 'datetime' module.

# -------------------------------------------------------
# Code starts here
# -------------------------------------------------------

from datetime import datetime

# Define the structure of an event using a dictionary
event_template = {
    "event_id": "",  # Event ID, format as a string, e.g., "001"
    "event_name": "",  # Event name, format as a string, e.g., "Python Workshop"
    "speaker": "",  # Speaker's name, format as a string, e.g., "John Doe"
    "date": "",  # Event date, format as "YYYY-MM-DD", e.g., "2024-02-10"
    "capacity": 0,  # Event capacity, format as an integer, e.g., 50
    "attendees": []  # List of attendees, initially an empty list
}

# Event database using a dictionary, with event_id as keys
event_database = {}

def is_valid_date(date_str):
    """
    Validates if the date string is in the "YYYY-MM-DD" format.

    Parameters:
    date_str (str): The date string to validate.

    Returns:
    bool: True if the format is correct, False otherwise.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def create_event(event_id, event_name, speaker, date, capacity):
    """
    Create a new event and add it to the event database, after validating the date format.

    Parameters:
    event_id (str): A unique identifier for the event.
    event_name (str): Name of the event.
    speaker (str): Name of the speaker.
    date (str): Date of the event.
    capacity (int): Maximum number of participants for the event.
    """
    if event_id in event_database:
        print(f"Error: Event ID {event_id} already exists.")
        return False

    if not is_valid_date(date):
        print(f"Error: The date {date} is not in the correct format (YYYY-MM-DD).")
        return False

    event_database[event_id] = {
        "event_id": event_id,
        "event_name": event_name,
        "speaker": speaker,
        "date": date,
        "capacity": capacity,
        "attendees": []
    }
    print(f"Event '{event_name}' has been successfully created.")
    return True

# Example usage
if create_event("001", "Python Workshop", "John Doe", "2024-02-30", 50):
    print("Event creation successful.")
else:
    print("Event creation failed.")

# Functionality1: Event creation and Management Functions

# Allow users to create and modify event details, such as date, time, topic, speaker, capacity, etc
def modify_event(event_id, updated_info):
    """
    Modifies the details of a specified event.

    Parameters:
    event_id (str): The unique identifier of the event to be modified.
    updated_info (dict): A dictionary containing the updated information, which may include
                         event name, speaker, date, and capacity.

    Returns:
    bool: True if the modification is successful, False otherwise.
    """
    if event_id not in event_database:
        print(f"Error: Event ID {event_id} does not exist.")
        return False

    # Check the date format if a new date is provided
    if 'date' in updated_info and not is_valid_date(updated_info['date']):
        print(f"Error: The date {updated_info['date']} is not in the correct format (YYYY-MM-DD).")
        return False

    # Update the event information
    for key in updated_info:
        if key in event_database[event_id]:
            event_database[event_id][key] = updated_info[key]
        else:
            print(f"Warning: Key {key} is not a valid event attribute. This update will be ignored.")

    print(f"Event '{event_id}' has been successfully updated.")
    return True

# Example usage
updated_event_info = {
    "event_name": "Advanced Python Workshop",
    "date": "2024-03-15"
}
if modify_event("001", updated_event_info):
    print("Event update successful.")
else:
    print("Event update failed.")

# Enable users to register for events. The number of registrations should be tracked and limited based on capacity.
def register_for_event(event_id, participant_name):
    """
    Allows a user to register for a specified event.

    Parameters:
    event_id (str): The unique identifier of the event the user wants to register for.
    participant_name (str): The name of the participant.

    Returns:
    bool: True if the registration is successful, False otherwise.

    This function checks if the event exists in the event database. If the event exists,
    it then checks whether the event's capacity has been reached. If not, it adds the participant
    to the event's attendees list. If the event is at full capacity or does not exist,
    the function will return False and print an error message.
    """
    if event_id not in event_database:
        print(f"Error: Event ID {event_id} does not exist.")
        return False

    event = event_database[event_id]
    if len(event["attendees"]) >= event["capacity"]:
        print(f"Error: The event {event_id} is already at full capacity.")
        return False

    event["attendees"].append(participant_name)
    print(f"{participant_name} has been successfully registered for event {event_id}.")
    return True

# Example usage with comments
# Trying to register a participant named Alice for an event with ID "001".
if register_for_event("001", "Alice"):
    print("Registration successful.")
else:
    print("Registration failed.")

# Displaying the total loyalty points for each customer.
def display_loyalty_points(customer_name):
    """
    Displays the total loyalty points for a specified customer.

    Parameters:
    customer_name (str): The name of the customer.

    This function iterates through the event database, counts the number of events the specified
    customer has attended, and then calculates the total points based on this count.
    If the customer has not attended any events or does not exist in the records, it handles the error.
    """
    total_points = 0
    customer_found = False

    for event in event_database.values():


#Enable users to register for events. The number of registrations should be tracked and limited based on capacity.
def register_for_event(event_id, participant_name):
    """
    Allows a user to register for a specified event.

    Parameters:
    event_id (str): The unique identifier of the event the user wants to register for.
    participant_name (str): The name of the participant.

    Returns:
    bool: True if the registration is successful, False otherwise.

    This function checks if the event exists in the event database. If the event exists,
    it then checks whether the event's capacity has been reached. If not, it adds the participant
    to the event's attendees list. If the event is at full capacity or does not exist,
    the function will return False and print an error message.
    """
    if event_id not in event_database:
        print(f"Error: Event ID {event_id} does not exist.")
        return False

    event = event_database[event_id]
    if len(event["attendees"]) >= event["capacity"]:
        print(f"Error: The event {event_id} is already at full capacity.")
        return False

    event["attendees"].append(participant_name)
    print(f"{participant_name} has been successfully registered for event {event_id}.")
    return True

# Example usage with comments
# Trying to register a participant named Alice for an event with ID "001".
if register_for_event("001", "Alice"):
    print("Registration successful.")
else:
    print("Registration failed.")


#Displaying the total loyalty points for each customer.
def display_loyalty_points(customer_name):
    """
    Displays the total loyalty points for a specified customer.

    Parameters:
    customer_name (str): The name of the customer.

    This function iterates through the event database, counts the number of events the specified
    customer has attended, and then calculates the total points based on this count.
    If the customer has not attended any events or does not exist in the records, it handles the error.
    """
    total_points = 0
    customer_found = False

    for event in event_database.values():
        if customer_name in event["attendees"]:
            total_points += LOYALTY_POINTS_PER_EVENT
            customer_found = True

    if customer_found:
        print(f"{customer_name} has a total of {total_points} loyalty points.")
    else:
        print(f"Error: Customer '{customer_name}' not found or has no registered events.")
    return total_points

# Example usage
display_loyalty_points("Alice")


#Functionality2-Report Mechanism Functions: Generate a report on event attendance,participant feedback, and other useful metrics.
def generate_event_report(event_id):
    """
    Generates a report for a specified event.

    Parameters:
    event_id (str): The unique identifier of the event for which the report is generated.

    This function retrieves information about the specified event, including the list of attendees,
    and generates a report with details such as event name, date, total attendees, and participant feedback.
    """
    if event_id not in event_database:
        print(f"Error: Event ID {event_id} does not exist.")
        return

    event = event_database[event_id]
    event_name = event["event_name"]
    event_date = event["date"]
    attendees = event["attendees"]

    print(f"Event Report for '{event_name}' (Date: {event_date})")
    print(f"Total Attendees: {len(attendees)}")

    if len(attendees) > 0:
        print("Participant List:")
        for i, attendee in enumerate(attendees, start=1):
            print(f"{i}. {attendee}")
    else:
        print("No participants registered for this event.")

    # You can add additional report details as needed

# Example usage
generate_event_report("001")


#Functionalit3-Feedback Mechanism Functions: allow participants to provide post-event feedback to be used by event administrators when generating reports.
def collect_feedback(event_id, participant_name, feedback):
    """
    Allows participants to provide feedback for a specified event.

    Parameters:
    event_id (str): The unique identifier of the event for which feedback is provided.
    participant_name (str): The name of the participant providing feedback.
    feedback (str): The feedback provided by the participant.

    This function checks if the event exists and if the participant is registered for the event.
    If both conditions are met, the feedback is collected and stored in the event's feedback list.
    """
    if event_id not in event_database:
        print(f"Error: Event ID {event_id} does not exist.")
        return False

    event = event_database[event_id]
    if participant_name not in event["attendees"]:
        print(f"Error: {participant_name} is not registered for event {event_id}. Feedback cannot be collected.")
        return False

    if "feedback" not in event:
        event["feedback"] = []

    event["feedback"].append({"participant": participant_name, "feedback": feedback})
    print(f"Feedback from {participant_name} for event {event_id} has been successfully collected.")
    return True

# Example usage
collect_feedback("001", "Alice", "Great event! Very informative.")



# User Interface: Users can interact with the event management system.

def create_event():
    """
    Allows a user to create a new event and add it to the event database.

    This function should prompt the user for event details such as event ID, event name,
    speaker, date, and capacity, and then call the create_event() function to create the event.
    """
    event_id = input("Enter Event ID: ")
    event_name = input("Enter Event Name: ")
    speaker = input("Enter Speaker's Name: ")
    date = input("Enter Event Date (YYYY-MM-DD): ")
    capacity = int(input("Enter Event Capacity: "))
    
    if create_event(event_id, event_name, speaker, date, capacity):
        print("Event creation successful.")
    else:
        print("Event creation failed.")

def register_participant():
    """
    Allows a user to register for a specified event.

    This function prompts the user for the event ID and participant's name,
    and then calls the register_for_event() function to perform the registration.
    """
    event_id = input("Enter Event ID: ")
    participant_name = input("Enter Participant Name: ")

    if register_for_event(event_id, participant_name):
        print("Registration successful.")
    else:
        print("Registration failed. Please check the event ID and participant name.")

def display_loyalty_points():
    """
    Displays the total loyalty points for a specified customer.

    This function prompts the user for the customer's name and then calls
    the display_loyalty_points() function to display the loyalty points.
    """
    customer_name = input("Enter Customer Name: ")
    loyalty_points = calculate_loyalty_points(customer_name)
    
    if loyalty_points is not None:
        print(f"{customer_name} has a total of {loyalty_points} loyalty points.")
    else:
        print(f"Customer '{customer_name}' not found or has no registered events.")

def generate_event_report():
    """
    Generates a report for a specified event.

    This function prompts the user for the event ID and then calls
    the generate_event_report() function to generate the report.
    """
    event_id = input("Enter Event ID: ")
    generate_report(event_id)

def collect_feedback_menu():
    """
    Allows a user to collect feedback for a specified event.

    This function should prompt the user for the event ID, participant's name,
    and the feedback to be collected. Then it should call the collect_feedback() function.
    """
    event_id = input("Enter Event ID for feedback: ")
    participant_name = input("Enter Participant Name: ")
    feedback = input("Enter Feedback: ")

    if collect_feedback(event_id, participant_name, feedback):
        print("Feedback collection successful.")
    else:
        print("Feedback collection failed.")

def main_menu():
    """
    Displays the main menu options and handles user input.

    This function provides a simple text-based menu for the user to interact with the system.
    """
    while True:
        print("\nE-Business Event Management System")
        print("1. Create Event")
        print("2. Register Participant")
        print("3. Display Loyalty Points")
        print("4. Generate Event Report")
        print("5. Collect Feedback")
        print("6. Quit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            create_event()
        elif choice == "2":
            register_participant()
        elif choice == "3":
            display_loyalty_points()
        elif choice == "4":
            generate_event_report()
        elif choice == "5":
            collect_feedback()
        elif choice == "6":
            print("Exiting the E-Business Event Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")

# You can define the functions for menu options (create_event, register_participant, etc.) here.

# Example usage
main_menu()

