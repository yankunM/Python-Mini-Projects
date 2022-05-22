print("Welcome to THE quiz!")
print("------------------------------------------")
playing = input("Do you want to play this game? ")
print("------------------------------------------")
if playing.lower() != "yes":
    print("Goodbye T.T")
    quit() # quit the program

# quiz starts------------------------------------------
print("\nOkay! Lets get started!!")
print("If you want to quit the program at anytime, just type Q or q!!\n")
score = 0

# question 1
print("------------------------------------------")
answer = input("What does CPU stand for? \n")
if answer.lower() == "central processing unit":
    print("\nyou got it right!!\n")
    score += 1
elif answer.lower() == "q":
    print("Thank you for playing!!")
    quit()
else:
    print("\nsorry, incorrect\n")

# question 2
print("------------------------------------------")
answer = input("What does GPU stand for? \n")
if answer.lower() == "graphics processing unit":
    print("\nyou got it right!!\n")
    score += 1
elif answer.lower() == "q":
    print("Thank you for playing!!")
    quit()
else:
    print("\nsorry, incorrect\n")

# question 3
print("------------------------------------------")
answer = input("What does RAM stand for? \n")
if answer.lower() == "random access memory":
    print("\nyou got it right!!\n")
    score += 1
elif answer.lower() == "q":
    print("Thank you for playing!!")
    quit()
else:
    print("\nsorry, incorrect\n")

# question 4
print("------------------------------------------")
answer = input("What does PSU stand for? \n")
if answer.lower() == "power supply unit":
    print("\nyou got it right!!\n")
    score += 1
elif answer.lower() == "q":
    print("Thank you for playing!!")
    quit()
else:
    print("\nsorry, incorrect\n")

print("------------------------------------------")
print("You got " + str(score) + "/4 questions correct.")
print("Your score is: ", str((score/4) * 100) + "%")
print("------------------------------------------")
