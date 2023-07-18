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
