print(" This is basic Science quiz. There are some question related to Chemistry and Equations")
score= 0
ans1= input("What is the Symbol of Sodium in Periodic Table? ").strip ().upper()
if ans1 == "NA":
    print("Correct answer")
    score+=1
else: 
    print( "Incorrect. The symbol of Sodium is NA")
ans2= input("What is the Symbol of Potassium in Periodic Table?").strip ().upper()
if ans2== "K":
    print(" Good job ")
    score+=1
else:
    print ("Inccorect. The symbol of Potassium is K.")
ans3= int(input("How many electrons does Oxygen have?").strip ().upper())
if ans3 == "8":
    print("Correct answer")
    score+=1
elif ans3== "eight":
    print(" Good job!")
    score+=1
else: 
    print(" Wrong! Oxygen have 8 electrons.")
ans4=input("What is the Symbol of Argon in Periodic Table?").strip ().upper()
if ans4=="AR":
    print(" Great job!")
    score+=1
else:
    print(" Incorrect. It is AR.")
ans5=input("What is the Symbol of Einsteinium in Periodic Table?").strip ().upper()
if ans5==" ES":
    print(" Correct!")
    score+=1
else: 
    print(" Wrong. It is ES.")
ans6=int(input("How many electrons does Carbon have? ").strip ().upper())
if ans6== "6":
    print("Correct answer")
    score+=1
elif ans6==" six":
    print( " Great work")
    score+=1
else:
    print(" Incorrect. Oxygen have 6 electrons")
ans7=input("What is the Symbol of Bohrium in Periodic Table?").strip ().upper()
if ans7=="BH":
    print(" Good job")
    score+=1
else: 
    print(" Wrong. It is BH")
ans8=input("What is the Symbol of Neon in Periodic Table?").strip ().upper()
if ans8== "N":
    print(" Correct answer!")
    score+=1
else:
    print(" Incorrect. It is N")
ans9=input("How many electerons does Argon have? ").strip ().upper()
if ans9==" 18":
    print("Correct! great job")
    score+=1
else:
    print(" Wrong. Argon have 18 electrons.")
ans10= int(input("What is the atomic number of Argon?").strip ().upper())
if ans10==" 16":
    print(" Correct answer!")
    score+=1
elif ans10== " Sixteen":
    print(" Correct answer!")
    score+=1
else: 
    print( "Wrong, Agron's atmic number is 16.")

print( "The end. Your results are down below")
print("=" * 60)
print(" final results". center(60, "="))
print("=" * 60 )
