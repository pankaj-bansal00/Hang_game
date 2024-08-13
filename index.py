"""This is Hangman Game"""
import random
import logging

WORDS = ['python','java','html','javascript','angular']
lifeline = 5                     

print(f"""Welcome to the Hangman Game.
            we will pick up random word and you have to guess it
             you will get {lifeline} chances if you put the wrong input""")

WORD = random.choice(WORDS)
WORD_LENGTH = len(WORD)

display_string = '_'* WORD_LENGTH

while True:
   print(F"Welcome to the Hangman Game:- { '_'*WORD_LENGTH }")
   letter = input("input a letter:- ")

   if letter in WORD:
     new_string = ""
     print("exist")
     for index, chracter in enumerate(WORD):
        if letter == chracter:
          new_string += letter
         
        else:
           new_string += display_string[index]

     display_string = new_string
     print(f" Game won: {new_string}")
   
   else:
        lifeline = lifeline -1
        logging.warning("Doesn't exist. You lost a lifefline")
        if lifeline == 0:
           logging.info(f"You lost a Game. The word was{WORD}")
           break
   logging.warning(f"remaining lifeline: {lifeline}")

logging.info("Game is finished") 

