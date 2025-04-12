import tkinter as tk
from ui_elements import create_text_area, create_combo
from config import languages_colors

languages_list = ["C++", "C#", "Java", "Ruby",
                  "Pascal", "Java Script", "Swift",
                  "1C", "Rust", "PHP", "Scala", "CSS",
                  "Python", "HTML", "Не распознано"]

def on_combo_select(field):
    if field == 1:
        selected_language = combo_box_1.get()
        text_1.configure(bg=languages_colors.get(selected_language, 'white'))
    elif field == 2:
        selected_language = combo_box_2.get()
        text_2.configure(bg=languages_colors.get(selected_language, 'white'))

root = tk.Tk()
root.title("Языки программирования")
root.minsize(400, 400)
left_frame = tk.Frame(root)
right_frame = tk.Frame(root)
button_frame = tk.Frame(root)

combo_box_1 = create_combo(left_frame, languages_list)
text_1 = create_text_area(left_frame)
combo_box_2 = create_combo(right_frame, languages_list)
text_2 = create_text_area(right_frame)

left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
button_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

combo_box_1.bind("<<ComboboxSelected>>", lambda event: on_combo_select(1))
combo_box_2.bind("<<ComboboxSelected>>", lambda event: on_combo_select(2))

root.mainloop()