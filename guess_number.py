# ===================================number guessing
# import random
#
# def guess_number():
#     secret_number = random.randint(1, 100)
#     attempts = 0
#
#     print("Welcome to the Number Guessing Game!")
#     print("I have picked a number between 1 and 100. Can you guess it?")
#
#     while True:
#         try:
#             guess = int(input("Enter your guess: "))
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             continue
#
#         attempts += 1
#
#         if guess < secret_number:
#             print("Too low! Try guessing a higher number.")
#         elif guess > secret_number:
#             print("Too high! Try guessing a lower number.")
#         else:
#             print(f"Congratulations! You guessed the number in {attempts} attempts!")
#             break
#
# guess_number()