import random
stages = ['''
     ------
     |    |
          |
          |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
          |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
     |    |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
    /|    |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    ''' ]
word_list = ["aardvark","baboon","camel"]

#todo-1: - create a variable called 'lives' to keep track of the number of lives left.
# set 'lives' to equal 6.
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display =""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in chosen_word:
            display += letter
        else:
           display =""

    print(display)

    #Todo-2: - tf guess is not a letter in the chosen_word,then reduce ' lives' by 1.
    #if lives goes down to 0 then the game should stop and it should print "you lose."
    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        game_over = True
        print("You lose!")

      if "_" not in display:
       game_over = True
      print("You win!")

   #Todo-3: - print the ascii art from 'stages'
   #That corresponds to the current number of 'lives the user hs remaining.

print(stages[lives])


