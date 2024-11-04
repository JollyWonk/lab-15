import tkinter as tk
from tkinter import Text, messagebox
import random

def generate_numbers():
    try:
        lower_bound = int(entry_lower.get())
        upper_bound = int(entry_upper.get())
        
        if lower_bound > upper_bound:
            messagebox.showerror("Помилка", "Нижня межа має бути меншою за верхню")
            return

        random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(8)]

        with open("random_numbers.txt", "w") as file:
            file.write(", ".join(map(str, random_numbers)))

        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, ", ".join(map(str, random_numbers)))
        
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення для меж")

root = tk.Tk()
root.geometry("250x400")
root.configure(bg="orange")

tk.Label(root, text="Нижня межа:", bg="orange").pack()
entry_lower = tk.Entry(root)
entry_lower.pack()

tk.Label(root, text="Верхня межа:", bg="orange").pack()
entry_upper = tk.Entry(root)
entry_upper.pack()

btn_generate = tk.Button(root, text="Згенерувати числа", command=generate_numbers)
btn_generate.pack()

text_widget = Text(root, width=25, height=10)
text_widget.pack()

root.mainloop()
