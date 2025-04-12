languages_colors = {
    'C++': 'lightpink',
    'C#': 'lightblue',
    'Java': 'brown',
    'Ruby': 'red',
    'Pascal': 'lightpink',
    'Java Script': 'lightgreen',
    'Swift': 'lightyellow',
    '1C': 'purple',
    'Rust': 'pink',
    'PHP': 'blue',
    'Scala': 'red',
    'CSS': 'yellow',
    'Python': 'green',
    'HTML': 'purple',
    'Не распознано': 'white'
}

language_keywords = {
    'C++': ['#include', 'std::', 'cout', 'cin', '->', '::'],
    'C#': ['using', 'namespace', 'class', 'void', 'public', 'static'],
    'Java': ['public', 'class', 'void', 'import', 'System.out'],
    'Ruby': ['def', 'end', 'puts', 'class', 'module', 'begin'],
    'Pascal': ['begin', 'end', 'writeln', 'program', 'var', ':='],
    'Java Script': ['function', 'console.log', 'let', 'var', 'const'],
    'Swift': ['func', 'let', 'var', 'class', 'import', 'print'],
    '1C': ['Процедура', 'Функция', 'КонецПроцедуры', 'Перем', 'Если', 'Тогда'],
    'Rust': ['fn', 'let', 'mut', 'println!', 'impl', 'use'],
    'PHP': ['<?php', 'echo', '$', 'function', 'namespace', 'use'],
    'Scala': ['object', 'def', 'val', 'var', 'println', 'class'],
    'CSS': ['{', '}', ':', ';', 'color', 'background'],
    'Python': ['def', 'print', 'import', 'class', 'self', 'lambda'],
    'HTML': ['<html>', '<head>', '<body>', '<div>', '</html>', '<script>']
}

translation_rules = {
    ('Python', 'C++'): {
        'def ': 'void ',
        'print': 'std::cout << ',

    },
    # потом другие правила......
}