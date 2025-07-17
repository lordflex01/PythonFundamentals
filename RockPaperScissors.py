import random 

name = input("Enter your name: \n");

print("Hi "+name+". Welcome to this game.");

age = int(input("How old are you?\n"));

print("Great! Let's start");

choice_list = ['rock', 'paper', 'scissors'];
computer_choice = random.choice(choice_list);
user_choice = input("Choose between rock, paper or scissors\n");

if (computer_choice == user_choice):
    print ("TIE");
elif (user_choice == 'paper' and computer_choice == 'rock') : 
    print ("You win! The computer choice was "+computer_choice);
elif (user_choice == 'rock' and computer_choice == 'scissors') :
    print ("You win! The computer choice was "+computer_choice);
elif (user_choice == 'scissors' and computer_choice == 'paper') :
    print ("You win! The computer choice was "+computer_choice);
else : 
    print ("You lose! The computer choice was "+computer_choice);

print("Let's play another game");

choice_dice = random.randint(1,6); 

user_guess = int(input("The computer has chosen a number between 1 and 6. Guess what it is:\n"));

if(choice_dice == user_guess):
    print("Congrats!!!");
else:
    print("Sorry! The computer choice was "+str(choice_dice));

print("We are going to end up here");