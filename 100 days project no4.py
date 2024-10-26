import random

rock = """
  _______
 /      /|
/______/ |
|      | |
|  ROCK | |
|      | /
|______|/
"""

paper = """
 ________
|        |
|  PAPER |
|        |
|________|
"""

scissors = """
  ______
 /     /|
/_____/ |
|     | |
|     | |
|_____|/
   ||
   ||
   ||
"""

game_images = [rock,paper,scissors]

user_choice = int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissors"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 0:
    print("you win!")
elif computer_choice == 0 and user_choice == 0:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a draw!")
else:
    print("you typed an invalid number, you lose!")

