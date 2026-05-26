# --- THE ROLLERCOASTER TICKET CHECKER ---

# Section 1
rider_height = 45

if rider_height == 48:
    print("You are exactly tall enough!")


# Section 2
ticket_type = "VIP"

if ticket_type == "Standard":
 print("Please head to the normal line.")

# Section 3
rider_age = int(input(" What is your age? ")) 
if rider_age < 12:
 print("Child ticket price: $5")
else: 
 print("Adult ticket price: $10")