import tkinter as tk
import random

secret_number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(guess_entry.get())
        if guess < secret_number:
            result_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Congratulations! You guessed it: {secret_number}")
    except ValueError:
        result_label.config(text="Invalid input. Enter a number.")

window = tk.Tk()
window.title("Guess the Number")

instructions_label = tk.Label(window, text="Guess a number between 1 and 100:")
instructions_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

check_button = tk.Button(window, text="Check", command=check_guess)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
