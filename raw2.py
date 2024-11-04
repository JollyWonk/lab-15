import tkinter as tk

def change_color():
    selected_color = color_var.get()
    root.configure(bg=selected_color)

root = tk.Tk()
root.geometry("250x400")
root.configure(bg="white")

color_var = tk.StringVar(value="white")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Radiobutton(frame, text="Червоний", variable=color_var, value="red").pack(anchor="w")
tk.Radiobutton(frame, text="Зелений", variable=color_var, value="green").pack(anchor="w")
tk.Radiobutton(frame, text="Синiй", variable=color_var, value="blue").pack(anchor="w")

btn_change_color = tk.Button(root, text="Змінити колір", command=change_color)
btn_change_color.pack()

root.mainloop()
