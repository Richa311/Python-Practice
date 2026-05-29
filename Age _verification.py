# =====================================================================
# PROGRAM: Age verification
#           Verify the user's age is over 18 to give access (or deny access)
#           Keep asking for input until they've given a valid age
# =====================================================================

# VARIABLES
# TODO Create a variable for valid input and set it to false
# TODO Create a variable to old the user's age and set it to "" (blank)
vaild_input = False
user_age = ""

# GET INPUT
# TODO Start a loop while the input is invalid

    # TODO Ask the user for their age and save it
while vaild_input :
    user_age = input ("How old are you?")
    #TRY
try : 
    user_age = int ((user_age))
    user_age = True
except :
    print(" Your input was invalid ")

    # TODO Create a Try statement
        # TODO Change the input into an integer and resave it
        # TODO Set the valid input variable to true

    # FAIL TO CONVERT TO INTEGER
    # TODO Add an except statement
    # TODO Tell the user their input was invalid
# Unindented = Loop has finished so the input must be valid now
access = "denied"
# CHECK AGE

# TODO Check if they are older than 18 and tell them they have access if they are.
if user_age >= 18 :
  print ( "You have access")
# TODO Check if they are older than 13 and tell them they have partial access if they are.
elif user_age >= 13 :
  print (" You have partical access")
# TODO Otherwise tell them access has been denied
else : 
   print("Access has been denied" )

# ===================================================================
# EXTENSION
# Create a avatar creator for them to use if they get access. There should be 2 versions (full and partial)
# Eg. Full can choose: character class (warrior, rogue), hair colour, eye colour; partial just character class (with animal classes?)