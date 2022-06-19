import random

limit = input(" Enter the range: ")

if limit.isdigit():
    limit = int(limit)

if limit <= 0:
    print("Please enter the number greater than 0 next time.")
    quit()
else:
    print(" Please enter a number next time.")
    quit()

random_number = random.randint(0, limit)
count = 0

while True:
    count += 1
    guess = input(" Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print(" Please enter a number next time.")
        continue

    if guess == random_number:
        print("Your Guess is correct!")
        break
    elif guess < random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in ", count, "guesses")