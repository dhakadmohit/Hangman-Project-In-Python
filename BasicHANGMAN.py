#Step 1 
word_list = ["aardvark", "baboon", "camel","manisha","yashwant"]
new_list = []
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
import hangman_words
import hangman_art

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
for letter in chosen_word:
        new_list.append("_")
print(new_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_the_game = False
lives = 6
while not end_of_the_game:
    print("\n")
    guess = input("Guess a letter: ").lower()
    
    if guess in  new_list:
      print("\n")
      print("You already choose the letter!")
      
    for i in range(0,len(chosen_word)):
        if(guess == chosen_word[i]):
            new_list[i] = guess
            print("\n")
  
    if guess not in chosen_word:
        print("\n")
        print(f"The letter you guessed {guess}, thats not in the word!") 
        lives -= 1
        
        print("Oops! You loose one life :(")
        print(stages[lives])


    print(f"{' '.join(new_list)}")
    if (lives == 0):
        
        print("Oops! You Lose")
        end_of_the_game = True
        
    
    if "_" not in new_list:
        end_of_the_game = True
        
        print("Hurrah!! You Won the Game :) ") 