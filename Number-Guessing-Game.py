import random


print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")

# Generate Number
secret_number = random.randint(1,100)
attempts = 0

# Game Loop
while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
