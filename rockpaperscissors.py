import random
user_input=int(input("Enter your choice: 0=Rock, 1=Paper, 2=Scissors "))
if user_input>=3 or user_input<0:
    print("enter a valid option")
else:
 computer_choice=random.randint(0,2)
 print("computer choice:")
 print(computer_choice)
 if user_input == computer_choice:
    print("Draw")
 elif computer_choice == 0 and user_input == 2:
    print("You lose")
 elif computer_choice ==2 and user_input == 0:
    print("You win")
 elif computer_choice > user_input:
    print("You lose")
 elif user_input > computer_choice:
    print("You win")