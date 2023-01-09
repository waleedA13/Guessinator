import random

logo = """
 _____                     _             _             
|  __ \                   (_)           | |            
| |  \/_   _  ___  ___ ___ _ _ __   __ _| |_ ___  _ __ 
| | __| | | |/ _ \/ __/ __| | '_ \ / _` | __/ _ \| '__|
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | || (_) | |   
 \____/\__,_|\___||___/___/_|_| |_|\__,_|\__\___/|_|   
                                                       
                                                       """

print(logo)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def guessed_number(guess, number, lives):
    if guess == number:
        print(f"You got it correct. The answer was {number}.")
        return 0
    else:
        lives -= 1
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        print("Guess again.")
        print(f"You have {lives} attempts remaining to guess the number.")
        return lives

        
game = True
while game:
    number = random.randint(1, 100)

    dif = False
    while not dif:
        difficulty = input("Type 'easy' or 'hard': ").lower()

        if difficulty == "easy":
            lives = 10
            dif = True
        elif difficulty == "hard":
            lives = 5
            dif = True
        else:
            print("Invalid! Try again!")



    while lives > 0:
        guess = int(input("Make a guess: "))
        lives = guessed_number(guess, number, lives)
        if lives == 0:
            print(f"You lost! The answer was {number}.")

    play_again = True
    while play_again:
        play = input("Type 'yes' to play again. Else type 'no'.").lower()
        if play == "yes":
            play_again = False
        elif play == "no":
            play_again = False
            game = False
        else:
            print("Invalid! Try again!")
