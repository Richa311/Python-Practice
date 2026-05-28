
print (" Guess the country!")
country = "Canada"

guess = input ('What is your guess?')
print ('Checking if your guess is a match…')

while guess != country:
 print (" It's a match!")
 print ("Welcome! You guessed the country!")
 if guess== "":
  print("Try again")
  input ('What is your guess?')
 else:
  print ('Incorrect')

















































print("Guess the country!")
country = "Canada"

# Keep looping until the user types the correct country
while True:
    guess = input("What is your guess? ").strip()
    print("Checking if your guess is a match…")

    if guess.lower() == country.lower():
        print("It's a match!")
        print("Welcome! You guessed the country!")
        break  # This exits the loop when they win
    elif guess == "":
        print("Try again (cannot be blank).")
    else:
        print("Incorrect")
