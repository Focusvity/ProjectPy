import random

number = random.randint(1, 100)
print("Hello user, I'm thinking of a number between 1 and 100.\nYou have 15 guesses...")
guessUsed = 0

while guessUsed < 15:
    if guessUsed == 0:
        guess = int(input("What is your first guess? "))
    elif guessUsed == 14:
        guess = int(input("What is your last guess? "))
    else:
        guess = int(input("What is your next guess? "))

    guessUsed += 1

    if guess > number:
        print("The number is too high")
    elif guess < number:
        print("The number is too low")
    else:
        break
    if guessUsed == 5 or guessUsed == 10:
        remaining = str(15 - guessUsed)
        print("You have " + remaining + " left!")

if guess == number:
    guessUsed = str(guessUsed)
    print("Congratulations, you have guessed the number correctly in " + guessUsed + " tries!")
else:
    number = str(number)
    print("You have ran out of guesses, the number I was thinking was " + number)
