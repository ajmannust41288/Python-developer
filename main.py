# import cv2 as cv
# import numpy as np
# W = 400
# def my_ellipse(img, angle):
#     thickness = 2
#     line_type = 8
#     cv.ellipse(img,
#                 (W // 2, W // 2),
#                 (W // 4, W // 16),
#                 angle,
#                 0,
#                 360,
#                 (255, 0, 0),
#                 thickness,
#                 line_type)
# def my_filled_circle(img, center):
#     thickness = -1
#     line_type = 8
#     cv.circle(img,
#                center,
#                W // 32,
#                (0, 0, 255),
#                thickness,
#                line_type)
# def my_polygon(img):
#     line_type = 8
#     # Create some points
#     ppt = np.array([[W / 4, 7 * W / 8], [3 * W / 4, 7 * W / 8],
#                     [3 * W / 4, 13 * W / 16], [11 * W / 16, 13 * W / 16],
#                     [19 * W / 32, 3 * W / 8], [3 * W / 4, 3 * W / 8],
#                     [3 * W / 4, W / 8], [26 * W / 40, W / 8],
#                     [26 * W / 40, W / 4], [22 * W / 40, W / 4],
#                     [22 * W / 40, W / 8], [18 * W / 40, W / 8],
#                     [18 * W / 40, W / 4], [14 * W / 40, W / 4],
#                     [14 * W / 40, W / 8], [W / 4, W / 8],
#                     [W / 4, 3 * W / 8], [13 * W / 32, 3 * W / 8],
#                     [5 * W / 16, 13 * W / 16], [W / 4, 13 * W / 16]], np.int32)
#     ppt = ppt.reshape((-1, 1, 2))
#     cv.fillPoly(img, [ppt], (255, 255, 255), line_type)
#     # Only drawind the lines would be:
#     # cv.polylines(img, [ppt], True, (255, 0, 255), line_type)
# def my_line(img, start, end):
#     thickness = 2
#     line_type = 8
#     cv.line(img,
#              start,
#              end,
#              (0, 0, 0),
#              thickness,
#              line_type)
# atom_window = "Drawing 1: Atom"
# rook_window = "Drawing 2: Rook"
# # Create black empty images
# size = W, W, 3
# atom_image = np.zeros(size, dtype=np.uint8)
# rook_image = np.zeros(size, dtype=np.uint8)
# # 1.a. Creating ellipses
# my_ellipse(atom_image, 90)
# my_ellipse(atom_image, 0)
# my_ellipse(atom_image, 45)
# my_ellipse(atom_image, -45)
# # 1.b. Creating circles
# my_filled_circle(atom_image, (W // 2, W // 2))
# # 2. Draw a rook
# # ------------------
# # 2.a. Create a convex polygon
# my_polygon(rook_image)
# cv.rectangle(rook_image,
#               (0, 7 * W // 8),
#               (W, W),
#               (0, 255, 255),
#               -1,
#               8)
# #  2.c. Create a few lines
# my_line(rook_image, (0, 15 * W // 16), (W, 15 * W // 16))
# my_line(rook_image, (W // 4, 7 * W // 8), (W // 4, W))
# my_line(rook_image, (W // 2, 7 * W // 8), (W // 2, W))
# my_line(rook_image, (3 * W // 4, 7 * W // 8), (3 * W // 4, W))
# cv.imshow(atom_window, atom_image)
# cv.moveWindow(atom_window, 0, 200)
# cv.imshow(rook_window, rook_image)
# cv.moveWindow(rook_window, W, 200)
# cv.waitKey(0)
# cv.destroyAllWindows()
# ================================================================list break
from tempfile import template

# noun = input("Enter a noun: ")
# verb = input("Enter a verb: ")
# story = template.format(noun, verb)
# print(story)
# play_again = True
# while play_again:
#     # Generate the story using the steps above
#
#     # Ask the user if they want to play again
#     play_again_input = input("Do you want to play again? (yes/no): ")
#     if play_again_input.lower() != "yes":
#         play_again = False
#
#==========================================
# noun = input("Enter a noun: ")
# while not noun.isalpha():
#     print("Invalid input. Please enter a noun.")
#     noun = input("Enter a noun: ")
# play_again = True
# while play_again:
#     # Generate the story using the steps above
#
#     # Ask the user if they want to play again
#     play_again_input = input("Do you want to play again? (yes/no): ")
#     while play_again_input.lower() not in ["yes", "no"]:
#         print("Invalid input. Please enter 'yes' or 'no'.")
#         play_again_input = input("Do you want to play again? (yes/no): ")
#
#     if play_again_input.lower() == "no":
#         play_again = False
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
# ====================================Rolling a dice game
# import random
#
#
# def roll_dice():
#     num_dice = int(input("Enter the number of dice to roll: "))
#     num_sides = int(input("Enter the number of sides on each die: "))
#
#     for _ in range(num_dice):
#         result = random.randint(1, num_sides)
#         print("Roll:", result)
#
#
# roll_dice()
#======================================================hangman game
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
#=========================================hospital management system
# Hospital Management Software in Python

# class Patient:
#     def __init__(self, patient_id, name, age, gender):
#         self.patient_id = patient_id
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class Doctor:
#     def __init__(self, doctor_id, name, department):
#         self.doctor_id = doctor_id
#         self.name = name
#         self.department = department
#
# class Appointment:
#     def __init__(self, patient, doctor, date, time):
#         self.patient = patient
#         self.doctor = doctor
#         self.date = date
#         self.time = time
#
# class Hospital:
#     def __init__(self):
#         self.patients = []
#         self.doctors = []
#         self.appointments = []
#
#     def add_patient(self, patient):
#         self.patients.append(patient)
#
#     def add_doctor(self, doctor):
#         self.doctors.append(doctor)
#
#     def create_appointment(self, patient_id, doctor_id, date, time):
#         patient = next((p for p in self.patients if p.patient_id == patient_id), None)
#         doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)
#         if not patient or not doctor:
#             return "Patient or Doctor not found."
#         appointment = Appointment(patient, doctor, date, time)
#         self.appointments.append(appointment)
#         return "Appointment created successfully."
#
#     def view_appointments(self):
#         if not self.appointments:
#             return "No appointments found."
#         for appointment in self.appointments:
#             print(f"Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date: {appointment.date}, Time: {appointment.time}")
#
# # Example usage:
# if __name__ == "__main__":
#     hospital = Hospital()
#
#     patient1 = Patient("P001", "John Smith", 35, "Male")
#     patient2 = Patient("P002", "Alice Johnson", 42, "Female")
#     hospital.add_patient(patient1)
#     hospital.add_patient(patient2)
#
#     doctor1 = Doctor("D001", "Dr. Emily White", "Cardiology")
#     doctor2 = Doctor("D002", "Dr. Michael Brown", "Neurology")
#     hospital.add_doctor(doctor1)
#     hospital.add_doctor(doctor2)
#
#     hospital.create_appointment("P001", "D001", "2023-07-20", "15:30")
#     hospital.create_appointment("P002", "D002", "2023-07-22", "11:00")
#
#     hospital.view_appointments()
# =====================================gui based hospital management system
import tkinter as tk
from tkinter import messagebox

class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")

        self.patient_label = tk.Label(root, text="Patient ID:")
        self.patient_label.grid(row=0, column=0)
        self.patient_entry = tk.Entry(root)
        self.patient_entry.grid(row=0, column=1)

        self.doctor_label = tk.Label(root, text="Doctor ID:")
        self.doctor_label.grid(row=1, column=0)
        self.doctor_entry = tk.Entry(root)
        self.doctor_entry.grid(row=1, column=1)

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=2, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=2, column=1)

        self.time_label = tk.Label(root, text="Time (HH:MM):")
        self.time_label.grid(row=3, column=0)
        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=3, column=1)

        self.create_appointment_btn = tk.Button(root, text="Create Appointment", command=self.create_appointment)
        self.create_appointment_btn.grid(row=4, column=0, columnspan=2)

    def create_appointment(self):
        patient_id = self.patient_entry.get()
        doctor_id = self.doctor_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        # Add your hospital management logic here
        # For simplicity, I'll show a message box with the appointment details
        appointment_details = f"Patient ID: {patient_id}\nDoctor ID: {doctor_id}\nDate: {date}\nTime: {time}"
        messagebox.showinfo("Appointment Details", appointment_details)


if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()




