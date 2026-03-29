#While loop guess numbers game
import random
target = random.randint(1,100)

print("Welcome to Guess Number Game(1~100)")
while True:
    num = int(input("Enter your guess:"))
    if num >target:
        print("Too big! Try again. ")
    elif num <target:
        print("Too small,Try again.")
    else:
        print("Congratulations! You guessed it right!")
        break