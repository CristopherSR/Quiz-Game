# Start of the game 
print("Welcome to my Quiz-Game")
play = input("Are you ready to play?")

if play.lower() != "yes":
    print("Okey run the game again, whenever your ready!")
    quit()

print("Let's play!")

# Questions and save the answers

correct = "Correct!"
incorrect = "Incorrect!"
score = 0

answer = input("What does PIP stand for ")
if answer.lower() == "python installer package":
    print(correct)
    score += 1
else:
    print(incorrect)

answer = input("What does the \"#\" symbol do in Python? ")
if answer.lower() == "comment a line":
    print(correct)
    score += 1
else:
    print(incorrect)

answer = input("Is indentation requiered in Python? ")
if answer.lower() == "yes":
    print(correct)
    score += 1
else:
    print(incorrect)

answer = input("To terminate the loop or a statement we use? ")
if answer.lower() == "break":
    print(correct)
    score += 1
else:
    print(incorrect)
    
answer = input("Name one of the pupular applications of Python. ")
if answer.lower() == "system scripting" or answer.lower() == "software development":
    print(correct)
    score += 1
else:
    print(incorrect)


print("Your final score is: " +str(score)+ "/5")
print(str((score / 5) * 100) + "%")


