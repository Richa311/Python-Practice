print (" This is basic Science quiz. There are some question related to Chemistry and Equations ")
score =  0
total_questions = 9
Quiz_running = True 

ans1 = input (" What is the Symbol of Sodium in Periodic Table? ") .strip ().upper()
if ans1 == "NA":
    print ("Correct answer")
    score += 1
else: 
    print (" Incorrect. The symbol of Sodium is NA" )

ans2 = input (" What is the Symbol of Potassium in Periodic Table? ") .strip ().upper()
if ans2 == "K":
    print (" Good job ")
    score += 1
else:
    print (" Inccorect. The symbol of Potassium is K. ")

ans3 = input(" How many electerons does Oxygen have?  ").strip ().upper()
if ans3 == "8" or ans3.lower == "eight":
    print (" Correct! great job ")
    score += 1
else:
    print (" Wrong. Oxygen have 8 electrons. ")
ans4 = input(" What is the Symbol of Argon in Periodic Table? ") .strip ().upper()
if ans4 =="AR": 
    print (" Great job!")
    score += 1
else:
    print (" Incorrect. It is AR. ")

ans5 = input (" What is the Symbol of Einsteinium in Periodic Table? ").strip ().upper()
if ans5 ==" es":
    print (" Correct!")
    score += 1
else: 
    print (" Wrong. It is ES. ")

ans6 = input(" How many electerons does Carbon have?  ").strip ().upper()
if ans6 == "6" or ans6.lower == "six":
    print (" Correct answer ")
    score += 1
else:
    print (" Incorrect. Carbon have 6 electrons. ")
ans7 = input ("What is the Symbol of Bohrium in Periodic Table?").strip ().upper()
if ans7 ==" BH":  #need to debug # 
    print (" Good job")
    score += 1
else: 
    print (" Wrong. It is BH")
    
ans8 = input("What is the Symbol of Neon in Periodic Table?").strip ().upper()
if ans8 == "N":
    print (" Correct answer!")
    score += 1
else:
    print (" Incorrect. It is N")
    
ans9 = input(" How many electerons does Argon have?  ").strip ().upper()
if ans9 == "18" or ans9.lower == "eighteen":
    print (" Correct! great job ")
    score += 1
else:
    print (" Wrong. Argon have 18 electrons. ")
ans10= (input("What is the atomic number of Argon?").strip ().upper())
if ans10==16 or ans10== " sixteen ": # need tp debug
    print(" Correct answer!")
    score+=1
else: 
    print( "Wrong, Agron's atmic number is 16.")

print( "The end. Your results are down below")
print(f"Your score: { score}/ { total_questions}") 
sucess_rate= (score/ total_questions ) * 100 
if sucess_rate == 100:
    print( " Rank: Great work! You know your elements well.")
elif sucess_rate >=70:
    print(" Rank: Good job! keep styding to reach the top score!")
else:
    print(" Rank: Beginner. Keep practicing on periodic table ")
    Quiz_running= False  