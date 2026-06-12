# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# TODO Import random module

# Wild Pokemon
# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
pokemon_list = {" name" : "Blissey", " health" : 714 }, {" name" : "Chansey", " health" : 704, }, {" name " :"Guzzlord", "health" :650, }, {"name ":"Zygarde", " health" : 636}
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage
attack_list = {"name" :"Hyper Beam", "damage" : 150 }, { "name" : "Draco Meteor","health" : 130 }, { "name " : "Earthquake", " health" :100 }, { "name" : "Flamethrower", "health" : 90 } 
# TODO Create a variable to hold a randomised wild pokemon
# for i in range( len(attack_list)): 

# TODO Create a current_health variable and set it to the max health of the random pokemon
current_health= pokemon_list[1]
# TODO Tell the user what pokemon they're facing
input( " What pokemon are you facing currently? ")
# TODO Create a while loop that continues until current health <= 0
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
input( " Which attack they'd like to use "(attack_list) ) 

    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health

# TODO Tell the user they defeated the pokemon

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.