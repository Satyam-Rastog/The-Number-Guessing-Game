import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("you guessed it wrong! Enter a larger number")
print(f"You guessed the number in {guesses} guesses")     
