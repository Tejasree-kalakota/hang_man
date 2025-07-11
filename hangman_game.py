import random
import hangman
words=['honey','moon','sun','love','mom','dad','hello','hai','bye','money','umbrella','icecream','chocolate','dress','hand','cap','teju','school','bag','pen','pencil','book','lunch','light','lamp','talk','happy','walk','speed','walk','girl','eat','meat','flesh']
choosen_word=random.choice(words)
display=[]
lives=6
for i in range(len(choosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over: 
    guessed_letter=input('guess a letter :').lower()
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)       
    if guessed_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print('you lose!!')
            print('the answer is: ',choosen_word)
    if '_' not in display:
         game_over=True
         print('you win')
    print(hangman.stages[lives])

