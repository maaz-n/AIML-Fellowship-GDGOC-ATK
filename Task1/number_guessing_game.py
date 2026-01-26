import random

num = random.randint(1, 10)

guess = int(input("Number acquired! Enter your guess: "))
tries = 1

while (guess != num):
    tries+=1
    guess = int(input("Incorrect! Guess again: "))

print("You are correct! The number was ", num)
print("Number of attempts:", tries)