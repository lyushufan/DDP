"""
Write a Python function named speeding_ticket that evaluates whether a driver should receive a speeding ticket based on their driving speed and a special condition (their birthday).

The function should return one of three strings based on the driver's speed: "No Ticket", "Small Ticket", or "Big Ticket".
If the driver's speed is 60 mph or less, they should receive "No Ticket".
If the driver's speed is between 61 and 80 mph inclusive, they should receive a "Small Ticket".
If the driver's speed is 81 mph or more, they should receive a "Big Ticket".
On the driver's birthday, the speed limits for each ticket category are increased by 5 mph. For example, they can go up to 65 mph and still receive "No Ticket" if it is their birthday.
"""

def speeding_ticket(speed, is_birthday):
    # Adjust speed limits based on birthday
    if is_birthday:
        speed_limit_no_ticket = 65
        speed_limit_small_ticket = 85
    else:
        speed_limit_no_ticket = 60
        speed_limit_small_ticket = 80
    
    # Evaluate speeding conditions
    if speed <= speed_limit_no_ticket:
        return "No Ticket"
    elif speed <= speed_limit_small_ticket:
        return "Small Ticket"
    else:
        return "Big Ticket"


# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))  # Expected output: "No Ticket"
print(speeding_ticket(85, True))  # Expected output: "Small Ticket"

