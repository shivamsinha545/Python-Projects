# rock paper scissor game
import random

print("Welcome to rock paper and scissor game\n")
name = input("Enter your name: ")
user_score = 0
computer_score = 0
options = ["rock", "paper", 'scissor']
print("Please use all small letters for providing input\n")
while True:
    user_input = str(input("Enter your choice (rock/paper/scissor),(in case of exit type done) :"))
    if user_input == 'done' or user_input == "Done":
        break
    computer_input = random.choice(options)
    if user_input == computer_input:
        print("Tie!")
        user_score += 0.5
        computer_score += 0.5
    elif user_input=='rock':
        if computer_input=='scissor':
            user_score+=1
            print(name," Won!")
        elif computer_input=='paper':
            computer_score+=1
            print("You Loose!")
    elif user_input=='paper':
        if computer_input=='rock':
            user_score+=1
            print(name," Won")
        elif computer_input=='scissor':
            computer_score+=1
            print("You Loose")
    elif user_input=='scissor':
        if computer_input=='rock':
            computer_score+=1
            print("You Loose")
        elif computer_input=='paper':
            user_score+=1
            print(name," Won")
    else:
        print("Invalid option, Try again!")




print("\n\nThankyou for playing with us.")
print("The final scores are as follows:")
print(name,"'s Score: ",user_score)
print("Computer's Score: ",computer_score)