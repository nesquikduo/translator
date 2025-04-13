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
        'input': 'std::cin >> ',
        'self': 'this',
        ':': '{',
        'lambda': '[]()',
        '#': '//'},
    ('Python', 'Java'): {
        'def ': 'public void ',
        'print': 'System.out.println',
        'self': 'this',
        'lambda': '->',
        '#': '//'},
    ('Python', 'Ruby'): {
        'def ': 'def ',
        'print': 'puts',
        'self': 'self',
        ':': '',
        '#': '#'},
    ('Python', 'PHP'): {
        'def ': 'function ',
        'print': 'echo ',
        'self': '$this',
        '#': '//'},
    ('Python', 'Java Script'): {
        'def ': 'function ',
        'print': 'console.log',
        'self': 'this',
        '#': '//'},
    ('Python', 'Swift'): {
        'def ': 'func ',
        'print': 'print',
        'self': 'self',
        '#': '//'},
    ('Python', 'Rust'): {
        'def ': 'fn ',
        'print': 'println!',
        'self': 'self',
        '#': '//'},
    ('Python', 'Scala'): {
        'def ': 'def ',
        'print': 'println',
        'self': 'this',
        '#': '//'},
    ('Python', 'Pascal'): {
        'def ': 'procedure ',
        'print': 'writeln',
        'self': '',
        '#': '//'},
    ('Python', '1C'): {
        'def ': 'Процедура ',
        'print': 'Сообщить',
        'self': 'ЭтотОбъект',
        '#': '//'},
    ('Python', 'HTML'): {
        'print': '<p>',
        '#': '<!--'},
    ('Python', 'CSS'): {
        'print': '',
        '#': '/*'},

    # C++
    ('C++', 'Python'): {
        '#include': 'import',
        'std::cout << ': 'print',
        'std::cin >> ': 'input',
        '//': '#',
        '{': ':',
        '}': '',
    },
    ('C++', 'Java'): {
        '#include': 'import',
        'std::cout << ': 'System.out.println',
        'std::cin >> ': 'System.in.read',
        '->': '->',
        'std::': ''
    },
    ('C++', 'Ruby'): {
        '#include': '',
        'std::cout << ': 'puts',
        'std::cin >> ': '',
        '//': '#',
        '{': '',
        '}': 'end'
    },

    # Java
    ('Java', 'Python'): {
        'public void ': 'def ',
        'System.out.println': 'print',
        'this': 'self',
        '//': '#',
        '{': ':',
        '}': ''
    },
    ('Java', 'C++'): {
        'public void ': 'void ',
        'System.out.println': 'std::cout << ',
        'this': 'this',
        '//': '//',
        '{': '{',
        '}': '}'
    },

}

