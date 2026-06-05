# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# TODO Import random so you can randomise the word

# VALUES
# TODO Create a list of at least 5 different 5-letter words
# TODO Create a variable called play and set it to True
play="True"
name_list= [ "White", "Table", "Black", " House", " Train" ]
# INTRODUCTION
# TODO Tell your user how to play wordle (make sure they know they must input 5 letter words)
print(" Welcome to Wordle")
print(" Guess the secert 5 letters word")
print(" You must input 5 letter in your answer")

# MAIN
# TODO Create a while loop that runs if play is true
while play== True: 
 word= name_list

    # TODO Create word variable and store a random word from your list (using random.choice)

    # USER INPUT
    # TODO Get user's first guess and save it into a variable
    # TODO Create a while loop if the guess is not 5 characters long
        # TODO Tell them it's not 5 letters and to try again
guess= input (" Enter a 5 letter word:") 
    # TODO Check if they got it correct and if they did, tell them so and then break the loop

    # TODO Create a for loop that loops 5 times
        # TODO Check if the current letter of user_input (user_input[i]) is the same as the i letter of the word and if it is tell them they got that letter correct
print( "Not the one ( think of a color), try again")
guess = input( "Enter a 5 letter word: ")
        # TODO Otherwise check if the current letter of user_input is in the word and if it is, tell them that letter is in the wrong position
if guess== word: 
  print ( "correct! you won.")
else: 
  print( " Try again")
guess = input( "Enter a 5 letter word: ")
print( " Try again")
guess = input( "Enter a 5 letter word: ")
print( " Try again")
guess = input( "Enter a 5 letter word: ")

        # TODO Else tell them that letter is wrong

# TODO Ask if they want to play again. If they don't, set play to false.