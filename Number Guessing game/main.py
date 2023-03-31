from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it. The answer is {answer}.")        
        



def set_difficulty():
    level = input("Type 'easy' or 'hard' to set difficulty :  ")
    if level == "easy" :
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    




def game():
    print("Welcome to Number Guessing Game.\nPick a number between 1 to 100")
    answer = randint(1, 100)
    turns = set_difficulty() 
    
    guess = 0 
    
    while guess != answer:
        print(f"You have {turns} attempts remining to go . ")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess , answer , turns )

        if turns == 0 :
            print("You have run out of guesses.You lose ." )
            return 
        elif guess != answer:
            print("Guess Again . ")    
    

game()