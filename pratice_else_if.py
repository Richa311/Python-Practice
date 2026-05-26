# --- THE PASSWORD SECURITY CHECK ---

# Section 1
correct_password = "admin123"
user_input= input( "What is your password?")
if user_input == correct_password: 
    print("Access Granted.")
elif user_input == " ": 
    print("Access Denied. Wrong password.")
else:
    print("Please try again.")



# Section 2
login_attempts = 3
user_input= int(input( " How many attempts have you had for login?"))
if user_input <= 5 :
  print("You have attempts remaining.")
else : 
 print("Your account is locked.")


# Section 3
password_length = 5
user_input= int(input(" What is the lenght of your password?"))
if user_input < 8:
    print("Weak password! Must be at least 8 characters.")
else:
    print("Strong password.")