
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