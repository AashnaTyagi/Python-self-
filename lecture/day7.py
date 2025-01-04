import random
print("Welcome to Hangman")
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

stages=['''


      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 jgs_|___ 
        ''' ,
        
'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 jgs_|___  
 ''',
   '''     

      _______
     |/      |
     |      (_)
     |      \|/
     |      
     |      
     |
 jgs_|___   
 ''',
        
'''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 jgs_|___  
 ''',
  '''      
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 jgs_|___
       '''  ,
  '''      
      _______
     |/      |
     |     
     |     
     |       
     |      
     |
 jgs_|___  
        ''']

word_list=["aardvark","baboon","camel"]
lives=6

chosen_word=random.choice(word_list)
print(chosen_word)

# for number of blanks:
placeholder=""
for position in range(1,len(chosen_word)+1):
    placeholder += "_"
print(placeholder)

# to guess letter from random choosen word
game_over=False
correct_letter=[]
while not game_over:
    guess_letter=input("guess a letter from word: ").lower()
    

# to print rgt wrong if letter matches
    display=""
    for i in chosen_word:
        if i==guess_letter:
            display+= i
            # so that previous letter stays also make list for correct lettr list
            correct_letter.append(guess_letter)
        elif i in correct_letter:
            display+=i
        else:
            display+="_"
    print(display)

    # if letter is not in the given chosen word
    if guess_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("Game Over! You Lose!!")

    if "_" not in display:
        game_over=True
        print("You Win")
# this laST LINE GIVES ERROR
    print(stages[lives])