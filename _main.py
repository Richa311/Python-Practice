# 1. Setup the secret target word
secret = "PYTHON"


# 2. Get inputs from the user
word = input("Enter the secret word: "). strip ()
response = input("Do you want to proceed to Mission Log?"). strip ()

# Standardise input
word = word.upper()
response = response.lower().strip()


# Check if they typed the secret word and want feedback
correct = (word == secret)
proceed = (response == "yes" or response == "y")

if correct and proceed:
    print("Access granted. Proceeding to Mission Log...")
elif not correct and proceed:
    print("Access denied. Secret word is incorrect")
elif correct and not proceed:
    print("Access granted. Proceeding to Menu...")
else:
    print("Shutting down...")
