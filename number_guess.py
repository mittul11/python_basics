import random
print("this is number guessing game ")
user= input("Do you want to play? ")
if user != "yes":
    quit()

print("ok lets play")
top_of_range = input("what is the number you wanna guess till ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

number = random.randint(0,top_of_range)



while True:
    ans = input("Enter a number? ")
    if ans.isdigit():
        ans = int(ans)
    if ans == number:
        print("Yay correct ")
        break 
    elif ans > number:
        print(" sorry the number you guess is bigger than the number")
        
    else:
        print("sorry the number is less ")
        