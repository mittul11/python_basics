# ask user a bunch of question and then at the end tell them the score 
print("Welcome to the comp quiz")

user = input("Do u want to play? ")
if user != "yes":
    quit()

print("Lets start")

score = 0
ques1 = int(input("what is 5 + 4? "))
if ques1 == 9:
    print("Correct")
    score = score+1
else:
    print("incorrect")

ques1 = int(input("what is 15 + 4? "))
if ques1 == 19:
    print("Correct")
    score = score+1
else:
    print("incorrect")

ques1 = int(input("what is 5 + 4? "))
if ques1 == 9:
    print("Correct")
    score = score+1
else:
    print("incorrect")

ques1 = (input("what is CPU? "))
if ques1.lower == "central processing unit":
    print("Correct")
    score = score+1
else:
    print("incorrect")

print("Game over, Your total score is " , score )
print("You got" , (score/4)*100 , "%")
