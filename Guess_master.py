import random

print("🎮 Welcome to GUESS MASTER 🎮")
print("Try to guess the secret number!\n")

name = input("Enter your name: ")
print("Welcome", name)

secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess == secret:
        print("Correct! 🎉")
        print(name + ", you got it in", attempts, "tries")
        break
    elif guess < secret:
        print("Too low 📉")
    else:
        print("Too high 📈")