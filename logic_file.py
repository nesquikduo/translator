import re
from config import language_keywords, languages_colors
from tkinter import messagebox, filedialog

def import_text(text_1, text_2, combo_box_1, combo_box_2, change_color_1, change_color_2,
                language_lock_1, language_lock_2, active_text_widget):
    file_path = filedialog.askopenfilename(
        title="Выберите файл для импорта",
        filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
    )
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        if active_text_widget == 'left':
            text_1.delete("1.0", "end")
            text_1.insert("1.0", content)
            change_color_1(text_1, combo_box_1, language_lock_1)
        elif active_text_widget == 'right':
            text_2.delete("1.0", "end")
            text_2.insert("1.0", content)
            change_color_2(text_2, combo_box_2, language_lock_2)

def translate_code(text_1, text_2, combo_box_1, combo_box_2, translation_rules, languages_colors, language_lock_2):
    source_lang = combo_box_1.get()
    target_lang = combo_box_2.get()
    source_code = text_1.get("1.0", "end").strip()

    if not source_lang or not target_lang:
        messagebox.showerror("Ошибка", "Выберите оба языка для перевода.")
        return

    if not source_code:
        messagebox.showinfo("Информация", "Левое поле пустое, нечего переводить.")
        return

    rules = translation_rules.get((source_lang, target_lang), {})
    translated = source_code
    for old, new in rules.items():
        translated = translated.replace(old, new)

    text_2.unbind("<KeyRelease>")
    text_2.delete("1.0", "end")
    text_2.insert("1.0", translated)
    text_2.configure(bg=languages_colors.get(target_lang, 'white'))

    text_2.bind(
        "<KeyRelease>",
        lambda event: translate_code(text_1, text_2, combo_box_1, combo_box_2, translation_rules, languages_colors, language_lock_2)
        if not language_lock_2.get() else None
    )

def detect_language(content):
    matches = {}
    words = re.findall(r'\b[\w:#<>]+\b', content)
    for language, keywords in language_keywords.items():
        matches[language] = sum(word in words for word in keywords)
    detected_language = max(matches, key=matches.get) if matches else None
    return detected_language if matches.get(detected_language, 0) > 0 else "Не распознано"

def change_color_1(text_widget, combo_box, lock_var):
    content = text_widget.get("1.0", "end").strip()
    if not content:
        if not lock_var.get():
            text_widget.configure(bg="white")
        return
    detected_language = detect_language(content)
    if not lock_var.get():
        combo_box.set(detected_language)
        text_widget.configure(bg=languages_colors.get(detected_language, 'white'))
    else:
        text_widget.configure(bg=languages_colors.get(combo_box.get(), 'white'))

def change_color_2(text_widget, combo_box, lock_var):
    content = text_widget.get("1.0", "end").strip()
    if not content:
        if not lock_var.get():
            text_widget.configure(bg="white")
        return
    detected_language = detect_language(content)
    if not lock_var.get():
        combo_box.set(detected_language)
        text_widget.configure(bg=languages_colors.get(detected_language, 'white'))
    else:
        text_widget.configure(bg=languages_colors.get(combo_box.get(), 'white'))

def save_text(text_1, text_2, combo_box_1, combo_box_2, active_text_widget):
    from tkinter import messagebox

    if active_text_widget == 'left':
        selected_language = combo_box_1.get()
        text_content = text_1.get("1.0", "end").strip()
    elif active_text_widget == 'right':
        selected_language = combo_box_2.get()
        text_content = text_2.get("1.0", "end").strip()
    else:
        messagebox.showerror("Ошибка", "Ни одно текстовое поле не активно!")
        return

    if not selected_language:
        messagebox.showerror("Ошибка", "Язык не выбран.")
        return

    if not text_content:
        messagebox.showinfo("Информация", "Поле пустое, нечего сохранять.")
        return

    file_name = f"{selected_language}.txt"
    try:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(text_content + "\n\n")
        messagebox.showinfo("Успех", f"Сохранено в {file_name}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить: {e}")