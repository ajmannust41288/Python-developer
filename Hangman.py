# import random
#
# def hangman():
#     words = ['python', 'hangman', 'programming', 'computer', 'software'] # List of words for the game
#     chosen_word = random.choice(words) # Randomly select a word from the list
#     guessed_letters = [] # List to store the letters guessed by the player
#     tries = 6 # Number of tries the player has
#
#     while tries > 0:
#         print("\n")
#         for letter in chosen_word:
#             if letter in guessed_letters:
#                 print(letter, end=" ")
#             else:
#                 print("_", end=" ")
#         print("\n")
#
#         guess = input("Guess a letter: ").lower() # Prompt the player to guess a letter
#
#         if guess.isalpha() and len(guess) == 1: # Check if the input is a single letter
#             if guess in guessed_letters:
#                 print("You've already guessed that letter!")
#             elif guess in chosen_word:
#                 print("Correct guess!")
#                 guessed_letters.append(guess)
#             else:
#                 print("Wrong guess!")
#                 tries -= 1
#                 guessed_letters.append(guess)
#         else:
#             print("Invalid input! Please enter a single letter.")
#
#         if set(chosen_word) == set(guessed_letters):
#             print("\nCongratulations! You guessed the word:", chosen_word)
#             break
#
#     if tries == 0:
#         print("\nSorry, you lost! The word was:", chosen_word)
#
# hangman()
# ===================================adding features more
# import random
# from tkinter import *
#
# def hangman():
#     # Initialize the game window
#     root = Tk()
#     root.title("Hangman")
#     root.geometry("400x400")
#
#     # List of words for the game
#     words = ['python', 'hangman', 'programming', 'computer', 'software']
#
#     # Initialize game variables
#     chosen_word = random.choice(words)
#     guessed_letters = []
#     tries = 6
#     score = 0
#
#     def update_word_label():
#         # Update the word label with the current guessed letters
#         displayed_word = ""
#         for letter in chosen_word:
#             if letter in guessed_letters:
#                 displayed_word += letter + " "
#             else:
#                 displayed_word += "_ "
#         word_label.config(text=displayed_word)
#
#     def make_guess():
#         # Process the player's guess
#         guess = guess_entry.get().lower()
#         guess_entry.delete(0, END)
#
#         if guess.isalpha() and len(guess) == 1:
#             if guess in guessed_letters:
#                 message_label.config(text="You've already guessed that letter!")
#             elif guess in chosen_word:
#                 message_label.config(text="Correct guess!")
#                 guessed_letters.append(guess)
#                 update_word_label()
#             else:
#                 message_label.config(text="Wrong guess!")
#                 tries -= 1
#                 guessed_letters.append(guess)
#                 update_word_label()
#
#                 if tries == 0:
#                     message_label.config(text="Sorry, you lost! The word was: " + chosen_word)
#                     root.after(2000, restart_game)
#
#         else:
#             message_label.config(text="Invalid input! Please enter a single letter.")
#
#         if set(chosen_word) == set(guessed_letters):
#             message_label.config(text="Congratulations! You guessed the word: " + chosen_word)
#             score_label.config(text="Score: " + str(score))
#             score += 1
#             root.after(2000, restart_game)
#
#     def restart_game():
#         # Reset game variables and start a new game
#         nonlocal chosen_word, guessed_letters, tries
#         chosen_word = random.choice(words)
#         guessed_letters = []
#         tries = 6
#         update_word_label()
#         message_label.config(text="")
#         score_label.config(text="Score: " + str(score))
#
#     # Create game interface elements
#     title_label = Label(root, text="Hangman", font=("Arial", 24))
#     title_label.pack(pady=10)
#
#     word_label = Label(root, text="", font=("Arial", 18))
#     word_label.pack(pady=20)
#
#     guess_entry = Entry(root, font=("Arial", 14))
#     guess_entry.pack(pady=10)
#
#     guess_button = Button(root, text="Guess", command=make_guess, font=("Arial", 14))
#     guess_button.pack(pady=5)
#
#     message_label = Label(root, text="", font=("Arial", 14))
#     message_label.pack(pady=10)
#
#     score_label = Label(root, text="Score: " + str(score), font=("Arial", 14))
#     score_label.pack(pady=5)
#
#     update_word_label()
#
#     root.mainloop()
#
# hangman()