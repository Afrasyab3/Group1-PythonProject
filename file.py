def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num2 / num1
    else:
        return "Invalid operator! Use +, -, *, or /"
import random

def guessing_game():
    while True:
        secret_number = random.randint(1, 50)
        attempts = 0

        print("I have selected a number between 1 and 50. Try to guess it!")

        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break

        play_again = input("Do you want to play again? yes/no: ")

        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break
