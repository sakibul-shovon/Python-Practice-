import random

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

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')


display = []
word_length = len(chosen_word)
lives = 6

for _ in range (len(chosen_word)):
    display +="_"
print(display)    


end_of_game = False

while not end_of_game:
    guess = input("Guess the letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    print(display) 

    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            print("You lose.")

   
    
    #print(f"{' '.join(display)}")       

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])    



    