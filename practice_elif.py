# --- THE TRAFFIC LIGHT SIMULATOR ---

# Section 1
light_color = "Yellow"
user_input= input( "What is the traffic light color?").strip()
if user_input == "Red":
    print("STOP!")
elif user_input == "Yellow":
    print("SLOW DOWN!")
elif user_input =="Green": 
    print("GO!")


# Section 2
driver_speed = 45
user_input= int(input(" What speed do you drive?"))
if user_input >= 50:
    print("You are speeding! Ticket issued.")
elif user_input <= 40:
    print("You're slowing traffic.")
else:
    print("Safe speed. Have a good day!")



# Section 3
score = 85
user_input= int(input(" What is your total score?"))
if user_input >= 90:
    print("Grade: A")
elif user_input >= 80:
    print("Grade: B")
elif user_input>= 70:
    print("Grade: C")
else:
    print("Grade: F")