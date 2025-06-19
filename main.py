import tkinter as tk
import sys
import io
import os
import locale

# Настройка кодировки консоли для корректного отображения русского языка
try:
    # Для Windows
    if os.name == 'nt':
        os.system('chcp 65001')  # UTF-8
    # Для Linux/Mac/Unix
    else:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
except:
    pass

# Настройка кодировки вывода консоли
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
except:
    pass

from ui_elements import create_text_area, create_combo
from config import languages_colors, translation_rules, language_keywords
from logic_file import change_color_1, change_color_2, translate_code, import_text, save_text, refresh_all, check_unrecognized_words, check_mixed_languages
from neural_language_detector import neural_detector

# Обучаем нейронную сеть при запуске приложения, если она еще не обучена
print("Инициализация нейронной сети...")
neural_detector.train()

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

def set_active_widget(name):
    global active_text_widget
    active_text_widget = name

# Добавляем функцию для явного обучения модели с помощью кнопки
def train_neural_detector():
    from tkinter import messagebox
    try:
        print("Запуск обучения нейронной сети...")
        accuracy = neural_detector.train(force=True)
        print(f"Обучение завершено. Точность: {accuracy:.2%}")
        messagebox.showinfo("Обучение", f"Модель успешно обучена! Точность: {accuracy:.2%}")
    except Exception as e:
        print(f"Ошибка при обучении модели: {e}")
        messagebox.showerror("Ошибка обучения", f"Ошибка при обучении модели: {e}")

# Добавляем функцию для показа примеров перевода
def show_translation_examples():
    from tkinter import messagebox
    
    source_lang = combo_box_1.get()
    target_lang = combo_box_2.get()
    
    if not source_lang or not target_lang:
        messagebox.showerror("Ошибка", "Выберите оба языка для примеров перевода.")
        return
    
    examples = neural_detector.get_translation_examples(source_lang, target_lang)
    if not examples:
        messagebox.showinfo("Информация", f"Не удалось создать примеры перевода с {source_lang} на {target_lang}.")
        return
    
    # Показываем первый пример
    example = examples[0]
    text_1.delete("1.0", tk.END)
    text_1.insert("1.0", example[0])
    text_2.delete("1.0", tk.END)
    text_2.insert("1.0", example[1])
    
    # Устанавливаем соответствующие цвета
    text_1.configure(bg=languages_colors.get(source_lang, 'white'))
    text_2.configure(bg=languages_colors.get(target_lang, 'white'))
    
    print(f"\n===== ПРИМЕР ПЕРЕВОДА {source_lang} -> {target_lang} =====")
    print("Исходный код:")
    print(example[0])
    print("\nПереведенный код:")
    print(example[1])
    print("=======================================\n")

print("Запуск приложения 'Языки программирования'")
root = tk.Tk()
root.title("Языки программирования")
root.minsize(400, 400)
language_lock_1 = tk.BooleanVar(value=False)
language_lock_2 = tk.BooleanVar(value=False)
active_text_widget = None
left_frame = tk.Frame(root)
right_frame = tk.Frame(root)
button_frame = tk.Frame(root)

combo_box_1 = create_combo(left_frame, languages_list)
text_1 = create_text_area(left_frame)
combo_box_2 = create_combo(right_frame, languages_list)
text_2 = create_text_area(right_frame)

lock_check_1 = tk.Checkbutton(left_frame, text="Lock", variable=language_lock_1)
lock_check_1.grid(row=0, column=2)
lock_check_2 = tk.Checkbutton(right_frame, text="Lock", variable=language_lock_2)
lock_check_2.grid(row=0, column=2)

swap_button = tk.Button(button_frame, text="<<-->>", command=swap_text)
swap_button.pack(pady=5)

translate_button = tk.Button(button_frame, text="Translate", command=lambda:
translate_code(text_1, text_2, combo_box_1, combo_box_2, translation_rules, languages_colors, language_lock_2))
translate_button.pack(pady=5)

import_button = tk.Button(button_frame, text="Import", command=lambda:
import_text(text_1, text_2, combo_box_1, combo_box_2, change_color_1,
            change_color_2, language_lock_1, language_lock_2, active_text_widget))
import_button.pack(pady=5)

save_button = tk.Button(button_frame, text="Save", command=lambda:
save_text(text_1, text_2, combo_box_1, combo_box_2, active_text_widget))
save_button.pack(pady=5)

refresh_button = tk.Button(button_frame, text="Refresh", command=lambda:
refresh_all(text_1, text_2, combo_box_1, combo_box_2))
refresh_button.pack(pady=5)

# Добавляем кнопку для явного обучения нейронной сети
train_button = tk.Button(button_frame, text="Train Neural", command=train_neural_detector)
train_button.pack(pady=5)

# Добавляем кнопку для показа примеров перевода
examples_button = tk.Button(button_frame, text="Show Examples", command=show_translation_examples)
examples_button.pack(pady=5)

left_frame.grid(row=0, column=0, padx=3, pady=10, sticky="nsew")
button_frame.grid(row=0, column=1, padx=2, pady=10, sticky="nsew")
right_frame.grid(row=0, column=2, padx=3, pady=10, sticky="nsew")


combo_box_1.bind("<<ComboboxSelected>>", lambda event: on_combo_select(1))
combo_box_2.bind("<<ComboboxSelected>>", lambda event: on_combo_select(2))
text_1.bind("<FocusIn>", lambda e: set_active_widget('left'))
text_2.bind("<FocusIn>", lambda e: set_active_widget('right'))
text_1.bind("<KeyRelease>", lambda event: change_color_1(text_1, combo_box_1, language_lock_1))
text_2.bind("<KeyRelease>", lambda event: change_color_2(text_2, combo_box_2, language_lock_2))
text_1.bind("<Return>", lambda e: check_mixed_languages(text_1, language_keywords))
text_1.bind("<Return>", lambda e: check_unrecognized_words(text_1, language_keywords), add="+")

text_2.bind("<Return>", lambda e: check_mixed_languages(text_2, language_keywords))
text_2.bind("<Return>", lambda e: check_unrecognized_words(text_2, language_keywords), add="+")

print("Интерфейс приложения успешно инициализирован")

if __name__ == "__main__":
    print("Запуск главного цикла приложения")
    root.mainloop()
    print("Приложение завершило работу")