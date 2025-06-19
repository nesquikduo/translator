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

from ui_elements import create_text_area, create_combo
from config import languages_colors, translation_rules, language_keywords
from logic_file import change_color_1, change_color_2, translate_code, import_text, save_text, refresh_all, check_unrecognized_words, check_mixed_languages



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

refresh_all(text_1, text_2, combo_box_1, combo_box_2))
refresh_button.pack(pady=5)

# Добавляем кнопку для явного обучения нейронной сети
train_button = tk.Button(button_frame, text="Train Neural", command=train_neural_detector)
train_button.pack(pady=5)

# Добавляем кнопку для показа примеров перевода
examples_button = tk.Button(button_frame, text="Show Examples", command=show_translation_examples)
examples_button.pack(pady=5)


refresh_all( text_1, text_2, combo_box_1, combo_box_2))
refresh_button.pack(pady=5)



text_2.bind("<Return>", lambda e: check_mixed_languages(text_2, language_keywords))
text_2.bind("<Return>", lambda e: check_unrecognized_words(text_2, language_keywords), add="+")

print("Интерфейс приложения успешно инициализирован")

if __name__ == "__main__":
    print("Запуск главного цикла приложения")
    root.mainloop()
    print("Приложение завершило работу")

text_2.bind("<Return>", lambda e: check_mixed_languages(text_2, language_keywords))
text_2.bind("<Return>", lambda e: check_unrecognized_words(text_2, language_keywords), add="+")


root.mainloop()

