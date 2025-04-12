import re
from config import language_keywords, languages_colors

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