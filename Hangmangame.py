import random
word_list = ['apple', 'banana', 'sapota','cherry','mango','grapes']
chosen_word = random.choice(word_list)
lives=6
stages=['''
    _____
      |
      0
     /|\\ 
     / \ 
    
    ''','''
    _____
      |
      0
     /|\\
     /  
     ''','''
    _____
      |
      0
     /|\\ 
       
     ''','''
    _____
      |
      0
     /|
      
     ''','''
    _____
      |
      0
      |  
     ''','''
    _____
      |
      0 
      
      
     ''','''
    _____
      |
       
       
        
     '''

]
display=[]
for x in chosen_word:
    display += '_'
print(display)
game_over= False
while not game_over:
    guess = input("Guess letter:").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            game_over=True
            print("You lose!")
    if '_' not in display:
     game_over=True
     print("You win!")
    print(stages[lives])