import re
from config import language_keywords, languages_colors
from tkinter import messagebox

def translate_code(text_1, text_2, combo_box_1, combo_box_2, translation_rules, languages_colors):
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
    text_2.bind("<KeyRelease>", lambda event: change_color_2(text_2, combo_box_2, language_lock_2))

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