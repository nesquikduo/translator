import tkinter as tk

root = tk.Tk()
root.title("Языки программирования")
root.minsize(400, 400)
left_frame = tk.Frame(root)
right_frame = tk.Frame(root)
button_frame = tk.Frame(root)

left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
button_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
root.mainloop()