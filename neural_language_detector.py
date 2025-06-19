import numpy as np
import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import pickle
import os
from config import language_keywords, translation_rules

class LanguageNeuralDetector:
    def __init__(self):
        self.model_file = "language_model.pkl"
        self.vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), 
                                           max_features=1000, lowercase=False)
        self.classifier = MLPClassifier(hidden_layer_sizes=(100, 50), 
                                       activation='relu', 
                                       solver='adam',
                                       max_iter=500,
                                       random_state=42)
        self.model = Pipeline([
            ('vectorizer', self.vectorizer),
            ('classifier', self.classifier)
        ])
        self.languages = list(language_keywords.keys())
        self.is_trained = False
        
        # Попытка загрузить существующую модель
        if os.path.exists(self.model_file):
            try:
                self.model = pickle.load(open(self.model_file, 'rb'))
                self.is_trained = True
                print("Модель успешно загружена из файла")
            except:
                print("Не удалось загрузить модель, будет выполнено новое обучение")
    
    def generate_training_data(self, samples_per_language=200, min_tokens=5, max_tokens=30):
        """Генерирует обучающие данные на основе ключевых слов языков и правил перевода"""
        X = []  # Тексты кода
        y = []  # Метки языков
        
        for language, keywords in language_keywords.items():
            # Создаем примеры для каждого языка
            for _ in range(samples_per_language):
                # Случайное количество токенов в примере
                num_tokens = random.randint(min_tokens, max_tokens)
                
                # Формируем пример кода
                code_sample = []
                for _ in range(num_tokens):
                    # С вероятностью 0.7 берем ключевое слово языка, иначе случайный идентификатор
                    if random.random() < 0.7 and keywords:
                        token = random.choice(keywords)
                    else:
                        # Генерируем случайный идентификатор
                        token = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') 
                                         for _ in range(random.randint(3, 10)))
                    
                    code_sample.append(token)
                
                # Добавляем характерные конструкции для языка
                self._add_language_specific_patterns(code_sample, language)
                
                # Перемешиваем токены и объединяем в строку
                random.shuffle(code_sample)
                code_text = ' '.join(code_sample)
                
                X.append(code_text)
                y.append(language)
        
        # Добавляем примеры из правил перевода для обогащения данных
        self._add_translation_examples(X, y)
        
        return X, y
    
    def _add_language_specific_patterns(self, code_sample, language):
        """Добавляет характерные для языка паттерны"""
        if language == "Python":
            code_sample.extend(["def", ":", "#", "import", "class"])
        elif language == "Java":
            code_sample.extend(["public", "class", "{", "}", "System.out.println"])
        elif language == "C++":
            code_sample.extend(["#include", "std::", "int", "{", "}"])
        elif language == "JavaScript" or language == "Java Script":
            code_sample.extend(["function", "console.log", "var", "const"])
        elif language == "PHP":
            code_sample.extend(["<?php", "echo", "$", "?>"])
        elif language == "Ruby":
            code_sample.extend(["def", "end", "puts", "#"])
        elif language == "Rust":
            code_sample.extend(["fn", "let", "mut", "println!"])
        elif language == "Swift":
            code_sample.extend(["func", "let", "var", "print"])
        elif language == "C#":
            code_sample.extend(["using", "namespace", "class", "Console.WriteLine"])
        elif language == "1C":
            code_sample.extend(["Процедура", "КонецПроцедуры", "Если", "Тогда"])
        elif language == "Pascal":
            code_sample.extend(["begin", "end", "writeln", "var"])
        elif language == "Scala":
            code_sample.extend(["def", "val", "var", "println"])
    
    def _add_translation_examples(self, X, y, n_examples=100):
        """Добавляет примеры, созданные на основе правил перевода"""
        languages = list(language_keywords.keys())
        
        for _ in range(n_examples):
            if not translation_rules:
                break
                
            # Выбираем случайную пару языков
            src_lang, tgt_lang = random.choice(list(translation_rules.keys()))
            rules = translation_rules[(src_lang, tgt_lang)]
            
            # Создаем пример кода на исходном языке
            src_keywords = language_keywords.get(src_lang, [])
            if not src_keywords:
                continue
                
            # Берем несколько ключевых слов и применяем к ним правила перевода
            sample_keywords = random.sample(src_keywords, min(5, len(src_keywords)))
            
            # Добавляем образец исходного языка
            src_sample = ' '.join(sample_keywords)
            X.append(src_sample)
            y.append(src_lang)
            
            # Применяем правила перевода для создания примера целевого языка
            tgt_sample = src_sample
            for old, new in rules.items():
                tgt_sample = tgt_sample.replace(old, new)
            
            X.append(tgt_sample)
            y.append(tgt_lang)
    
    def train(self, force=False):
        """Обучает модель нейронной сети"""
        if self.is_trained and not force:
            print("Модель уже обучена. Используйте force=True для переобучения.")
            return
        
        print("Генерация обучающих данных...")
        X, y = self.generate_training_data()
        
        # Разделяем данные на обучающую и тестовую выборки
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print(f"Обучение на {len(X_train)} примерах...")
        self.model.fit(X_train, y_train)
        
        # Оцениваем модель
        accuracy = self.model.score(X_test, y_test)
        print(f"Точность модели: {accuracy:.4f}")
        
        # Сохраняем модель
        pickle.dump(self.model, open(self.model_file, 'wb'))
        self.is_trained = True
        print("Модель обучена и сохранена")
        
        return accuracy
    
    def detect_language(self, code):
        """Определяет язык программирования в коде"""
        if not self.is_trained:
            self.train()
        
        if not code.strip():
            return "Не распознано"
        
        # Предварительная обработка кода
        code = self._preprocess_code(code)
        
        # Получаем вероятности для каждого языка
        try:
            # Получаем предсказание и вероятности
            predicted_lang = self.model.predict([code])[0]
            probabilities = self.model.predict_proba([code])[0]
            
            # Получаем индекс предсказанного языка и его вероятность
            lang_index = list(self.model.classes_).index(predicted_lang)
            confidence = probabilities[lang_index]
            
            # Если уверенность ниже порога, выполняем дополнительную проверку
            if confidence < 0.6:
                # Дополнительная проверка на основе ключевых слов
                fallback_lang = self._fallback_detection(code)
                if fallback_lang != "Не распознано":
                    return fallback_lang
            
            return predicted_lang
        except:
            # В случае ошибки предсказания используем запасной метод
            return self._fallback_detection(code)
    
    def _preprocess_code(self, code):
        """Предобработка кода перед распознаванием"""
        # Удаляем строки и комментарии, так как они могут содержать текст на любом языке
        code = re.sub(r'["\'](?:(?=(\\?))\1.)*?["\']', '', code)
        code = re.sub(r'\/\/.*?$', '', code, flags=re.MULTILINE)
        code = re.sub(r'\/\*[\s\S]*?\*\/', '', code)
        code = re.sub(r'#.*?$', '', code, flags=re.MULTILINE)
        return code
    
    def _fallback_detection(self, code):
        """Запасной метод определения языка на основе ключевых слов"""
        words = re.findall(r'[\w\.\!\:\#\<\>\$\(\)\[\]]+', code)
        matches = {}
        
        for language, keywords in language_keywords.items():
            matches[language] = sum(1 for word in words if word in keywords)
        
        # Применяем специфические правила
        if 'def' in words:
            if 'end' in words:
                matches['Ruby'] = matches.get('Ruby', 0) + 2
            if ':' in code:
                matches['Python'] = matches.get('Python', 0) + 2
        if 'echo' in words and '$' in code:
            matches['PHP'] = matches.get('PHP', 0) + 2
        if 'fn' in words and 'let' in words:
            matches['Rust'] = matches.get('Rust', 0) + 2
        if 'println!' in code:
            matches['Rust'] = matches.get('Rust', 0) + 1
        if 'print' in words and 'func' in code:
            matches['Swift'] = matches.get('Swift', 0) + 2
        if 'System.out.println' in code:
            matches['Java'] = matches.get('Java', 0) + 2
        if 'Console.WriteLine' in code:
            matches['C#'] = matches.get('C#', 0) + 2
        if 'writeln' in words or ':=' in code:
            matches['Pascal'] = matches.get('Pascal', 0) + 2
        if 'Сообщить' in words or 'Перем' in words:
            matches['1C'] = matches.get('1C', 0) + 2
        if 'console.log' in code:
            matches['Java Script'] = matches.get('Java Script', 0) + 2
        
        # Если нет совпадений, возвращаем "Не распознано"
        if not matches or max(matches.values(), default=0) == 0:
            return "Не распознано"
        
        # Возвращаем язык с наибольшим количеством совпадений
        return max(matches, key=matches.get)
    
    def feedback(self, code, correct_language, incorrect_language=None):
        """Обрабатывает обратную связь для улучшения модели"""
        # Если модель неправильно определила язык, добавляем этот пример в обучение
        if not self.is_trained:
            self.train()
        
        # Предварительно обрабатываем код
        processed_code = self._preprocess_code(code)
        
        # Создаем новые обучающие данные
        X = [processed_code]
        y = [correct_language]
        
        # Обновляем модель с новыми данными (инкрементное обучение)
        try:
            # Дообучаем модель на новом примере
            self.model.steps[1][1].partial_fit(
                self.model.steps[0][1].transform(X), 
                y,
                classes=list(language_keywords.keys())
            )
            
            # Сохраняем обновленную модель
            pickle.dump(self.model, open(self.model_file, 'wb'))
            print(f"Модель обновлена с учетом нового примера языка {correct_language}")
            return True
        except Exception as e:
            print(f"Ошибка при обновлении модели: {e}")
            return False
    
    def evaluate_translation(self, source_code, source_lang, target_lang, translated_code):
        """
        Оценивает качество перевода с одного языка на другой.
        Возвращает процент точности перевода.
        """
        if not self.is_trained:
            self.train()
        
        if not source_code.strip() or not translated_code.strip():
            return 0.0
        
        # Метрики для оценки качества перевода
        metrics = {}
        
        # 1. Проверка, распознается ли переведенный код как целевой язык
        detected_lang = self.detect_language(translated_code)
        language_match_score = 1.0 if detected_lang == target_lang else 0.5
        metrics["language_detection"] = language_match_score
        
        # 2. Проверка наличия ключевых слов целевого языка в переведенном коде
        target_keywords = set(language_keywords.get(target_lang, []))
        words_in_translated = set(re.findall(r'[\w\.\!\:\#\<\>\$\(\)\[\]]+', translated_code))
        
        keywords_found = target_keywords.intersection(words_in_translated)
        keywords_ratio = len(keywords_found) / max(1, min(len(target_keywords), 10))
        metrics["keywords_presence"] = min(1.0, keywords_ratio)
        
        # 3. Проверка структуры кода
        structure_score = 0.0
        if target_lang == "Python" and ":" in translated_code and not "{" in translated_code:
            structure_score = 1.0
        elif target_lang in ["C++", "Java", "C#", "Java Script"] and "{" in translated_code and "}" in translated_code:
            structure_score = 1.0
        elif target_lang == "Ruby" and "end" in translated_code:
            structure_score = 1.0
        elif target_lang == "1C" and "КонецПроцедуры" in translated_code:
            structure_score = 1.0
        elif target_lang == "Pascal" and "begin" in translated_code and "end" in translated_code:
            structure_score = 1.0
        else:
            structure_score = 0.5  # Базовая оценка, если не можем точно определить
        metrics["structure"] = structure_score
        
        # 4. Проверка применения правил перевода
        rules = translation_rules.get((source_lang, target_lang), {})
        rules_score = 0.0
        if rules:
            total_rules = len(rules)
            applied_rules = 0
            
            for old, new in rules.items():
                if old in source_code and new in translated_code:
                    applied_rules += 1
            
            rules_score = applied_rules / max(1, total_rules)
        metrics["rules_application"] = rules_score
        
        # 5. Синтаксическая проверка
        syntax_score = 0.7  # Базовая оценка, так как полную проверку синтаксиса сложно реализовать
        
        # 6. Проверка соответствия вложенности структур
        if source_lang == "Python" and target_lang != "Python":
            # Проверяем, что отступы в Python соответствуют скобкам в других языках
            python_indentation_levels = len(re.findall(r'^\s+', source_code, re.MULTILINE))
            target_braces = translated_code.count('{') if '{' in translated_code else 0
            nesting_score = min(1.0, max(0.5, 1.0 - abs(python_indentation_levels - target_braces) / max(1, python_indentation_levels)))
            metrics["nesting"] = nesting_score
        else:
            metrics["nesting"] = 0.8  # Базовая оценка
        
        # Вычисляем общую оценку с весами для разных метрик
        weights = {
            "language_detection": 0.35,
            "keywords_presence": 0.25,
            "structure": 0.20,
            "rules_application": 0.15,
            "nesting": 0.05
        }
        
        overall_score = sum(metrics[metric] * weights[metric] for metric in metrics) * 100
        
        # Выводим подробную информацию о метриках в консоль
        print(f"\n--- Оценка перевода {source_lang} -> {target_lang} ---")
        print(f"1. Распознавание языка: {metrics['language_detection']*100:.1f}%")
        print(f"2. Наличие ключевых слов: {metrics['keywords_presence']*100:.1f}%")
        print(f"3. Структура кода: {metrics['structure']*100:.1f}%")
        print(f"4. Применение правил: {metrics['rules_application']*100:.1f}%")
        print(f"5. Вложенность структур: {metrics['nesting']*100:.1f}%")
        print(f"Общая оценка качества перевода: {overall_score:.1f}%")
        
        return min(100, overall_score)  # Ограничиваем максимальной оценкой 100%
    
    def get_translation_examples(self, source_lang, target_lang, count=3):
        """
        Генерирует примеры перевода с исходного языка на целевой.
        Возвращает список пар (исходный код, переведенный код).
        """
        examples = []
        
        # Получаем ключевые слова исходного языка
        source_keywords = language_keywords.get(source_lang, [])
        if not source_keywords:
            return examples
        
        # Получаем правила перевода
        rules = translation_rules.get((source_lang, target_lang), {})
        if not rules:
            return examples
        
        # Генерируем примеры
        for _ in range(count):
            # Создаем простой пример кода на исходном языке
            if source_lang == "Python":
                source_code = f"def example_function():\n    print('Hello, World!')\n    return True"
            elif source_lang == "Java":
                source_code = f"public class Example {{\n    public void exampleMethod() {{\n        System.out.println(\"Hello, World!\");\n    }}\n}}"
            elif source_lang == "C++":
                source_code = f"#include <iostream>\nvoid exampleFunction() {{\n    std::cout << \"Hello, World!\" << std::endl;\n    return;\n}}"
            elif source_lang == "Ruby":
                source_code = f"def example_method\n    puts 'Hello, World!'\n    return true\nend"
            elif source_lang == "1C":
                source_code = f"Процедура ПримерМетода()\n    Сообщить(\"Привет, мир!\");\nКонецПроцедуры"
            else:
                # Генерируем базовый пример
                keywords = random.sample(source_keywords, min(5, len(source_keywords)))
                source_code = " ".join(keywords)
            
            # Переводим код
            translated_code = source_code
            for old, new in rules.items():
                translated_code = translated_code.replace(old, new)
            
            examples.append((source_code, translated_code))
        
        return examples

# Создаем глобальный экземпляр детектора
neural_detector = LanguageNeuralDetector()

def detect_language_neural(code):
    """Функция для интеграции с существующим кодом"""
    return neural_detector.detect_language(code)

def evaluate_translation_quality(source_code, source_lang, target_lang, translated_code):
    """Функция для оценки качества перевода кода"""
    return neural_detector.evaluate_translation(source_code, source_lang, target_lang, translated_code)

# Инициализация и предварительное обучение при импорте модуля
if __name__ == "__main__":
    print("Тестирование нейронного детектора языков программирования")
    neural_detector.train(force=True)
    
    # Тестовые примеры для разных языков
    test_samples = {
        "Python": "def hello():\n    print('Hello, World!')\n    return True",
        "Java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}",
        "C++": "#include <iostream>\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}",
        "Java Script": "function hello() {\n    console.log('Hello, World!');\n    return true;\n}",
        "1C": "Процедура ПриветМир()\n    Сообщить(\"Привет, мир!\");\nКонецПроцедуры",
        "Ruby": "def hello\n    puts 'Hello, World!'\n    return true\nend",
        "PHP": "<?php\necho \"Hello, World!\";\n$var = true;\nreturn $var;\n?>"
    }
    
    for lang, code in test_samples.items():
        detected = neural_detector.detect_language(code)
        print(f"Язык: {lang}, Распознано: {detected}, Правильно: {detected == lang}")