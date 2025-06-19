import re
from config import language_keywords, languages_colors
from tkinter import messagebox, filedialog

from neural_language_detector import detect_language_neural, neural_detector

    from tkinter import messagebox
    from neural_language_detector import evaluate_translation_quality
    

    # Оценка качества перевода
    translation_score = evaluate_translation_quality(
        source_code, source_lang, target_lang, translated
    )
    
    # Выводим информацию о качестве перевода
    print(f"\n===== РЕЗУЛЬТАТ ПЕРЕВОДА =====")
    print(f"Исходный язык: {source_lang}")
    print(f"Целевой язык: {target_lang}")
    print(f"Оценка качества перевода: {translation_score:.1f}%")
    print("=============================\n")
    
    # Показываем сообщение пользователю
    messagebox.showinfo("Результат перевода", 
                        f"Перевод кода с {source_lang} на {target_lang}\n"
                        f"выполнен с точностью: {translation_score:.1f}%")


    """
    Определяет язык программирования, используя нейронную сеть.
    Если по какой-то причине нейронная сеть не смогла распознать язык,
    используется запасной метод на основе ключевых слов.
    """
    # Используем нейронную сеть для определения языка
    detected_lang = detect_language_neural(content)
    
    # Проверяем результат
    if detected_lang and detected_lang != "Не распознано":
        return detected_lang
    
    # Запасной метод (оригинальный)

    # Добавляем обратную связь для нейронной сети
    if text_content:
        neural_detector.feedback(text_content, selected_language)


    content = text_widget.get("1.0", "end-1c")
    words = re.findall(r'\b[\w#]+\b', content)

    allowed_symbols = {'(', ')', '{', '}', '[', ']', ':', ',', ';'}

    unrecognized = []

    for word in words:
        found = any(word in keywords for keywords in language_keywords.values())
        if not found and word not in allowed_symbols:
            unrecognized.append(word)

    import re
    from tkinter import messagebox

    content = text_widget.get("1.0", "end").strip()
    if not content:
        return

    content = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', '', content)
    words = re.findall(r'[\w\.\!\:\#\<\>\$\(\)\[\]]+', content)

    all_keywords = set()
    for keyword_list in language_keywords.values():
        all_keywords.update(keyword_list)

    unrecognized = [word for word in words if word not in all_keywords]
