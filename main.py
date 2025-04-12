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

def swap_text():
    text_1_content = text_1.get("1.0", tk.END).strip()
    text_2_content = text_2.get("1.0", tk.END).strip()
    text_1.delete("1.0", tk.END)
    text_1.insert("1.0", text_2_content)
    text_2.delete("1.0", tk.END)
    text_2.insert("1.0", text_1_content)

    selected_1 = combo_box_1.get()
    selected_2 = combo_box_2.get()
    combo_box_1.set(selected_2)
    combo_box_2.set(selected_1)

    color_1 = languages_colors.get(selected_2, 'white')
    color_2 = languages_colors.get(selected_1, 'white')
    text_1.configure(bg=color_1)
    text_2.configure(bg=color_2)

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

swap_button = tk.Button(button_frame, text="<<-->>", command=swap_text)
swap_button.pack(pady=5)


left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
button_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

combo_box_1.bind("<<ComboboxSelected>>", lambda event: on_combo_select(1))
combo_box_2.bind("<<ComboboxSelected>>", lambda event: on_combo_select(2))

root.mainloop()