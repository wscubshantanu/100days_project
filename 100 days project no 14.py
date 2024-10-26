logo = """
_
_
_
| | __(_)
__
_ | | __
___
_
__
| '_ \| |/ _` | '
_ \ / _ \ '__|
| | | | | (_ | | | | | __ / |
           | _ | | _ | _ |\__, | _ | | _ | \___ | _ |
           | | _____ | ___ / _____ _ __
           | | / _ \ \ / \ / / _ \ '__|
           | | (_) \ V
V / __ / |
| _ |\___ / \_ /\_ / \___ | _ |
"""

vs ="""
__
_____
\ \ / / __ |
\ V /\__ \
    \_ / | ___ /
  """

from random import random

print(logo)

def format_data(account):
   """format the account data into printable format."""
   account_name = account['name']
   account_descr = account['description']
   account_country = account['country']
   return(f"{account_name},a {account_descr},from {account_country}")

def check_answer(user_guess, a_followers , b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(logo)


while game_should_continue:
    #generate a random account from the game data
    account_a = account_b
    account_b = random.choice(logo)

    if account_a == account_b:
     account_b = random.choice(logo)

    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"compare B: {format_data(account_b)}")

    #ask user for a guess
    guess = input("who has more followers? type 'a' or 'b':").lower()

    #clear the screen
    print("\n" * 20)
    print(logo)

    #- get follower  count of each account
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers, b_followers)

    #give user feedback on their guess
    #score keeping
    if is_correct:
      score += 1
      print("you're right! current score {score}")
    else:
      print(f"sorry,that's wrong.final score:{score}.")
      game_should_continue = False

