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
    'Python': 'green',
    'Не распознано': 'white'
}

language_keywords = {
    'C++': ['#include', 'std', '::', 'cout', 'cin', '->', 'void', 'int', 'return', 'if', 'else'],
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

    'Python': ['def', 'print', 'input', 'import', 'class', 'self',
                'lambda', 'if', 'else', 'elif', 'for', 'while',
                'return', 'try', 'except', 'with', 'as', 'from', '#'
]
}

translation_rules = {

    ('Python', 'C++'): {
        'def': 'void',
        'print': 'std::cout <<',
        'input': 'std::cin >>',
        'self': 'this',
        'lambda': '[]()',
        '#': '//',
        ':': '{',
        'return': 'return',
        'True': 'true',
        'False': 'false'},

    ('Python', 'Java'): {
        'def': 'public void',
        'print': 'System.out.println',
        'input': 'Scanner.nextLine()',
        'self': 'this',
        'lambda': '->',
        '#': '//',
        'return': 'return',
        'True': 'true',
        'False': 'false'},

    ('Python', 'Java Script'): {
        'def': 'function',
        'print': 'console.log',
        'input': 'prompt',
        'self': 'this',
        'lambda': '()=>',
        '#': '//',
        'return': 'return'},

    ('Python', 'C#'): {
        'def': 'void',
        'print': 'Console.WriteLine',
        'input': 'Console.ReadLine()',
        'self': 'this',
        'lambda': '=>',
        '#': '//',
        'return': 'return'},

    ('Python', 'Ruby'): {
        'def': 'def',
        'print': 'puts',
        'input': 'gets',
        'self': 'self',
        'lambda': '->',
        '#': '#',
        ':': '',
        'return': 'return'},

    ('Python', 'Swift'): {
        'def': 'func',
        'print': 'print',
        'input': 'readLine()',
        'self': 'self',
        'lambda': 'in',
        '#': '//',
        'return': 'return'},

    ('Python', 'Rust'): {
        'def': 'fn',
        'print': 'println!',
        'input': 'stdin',
        'self': 'self',
        'lambda': '|x|',
        '#': '//',
        'return': 'return'},

    ('Python', 'Scala'): {
        'def': 'def',
        'print': 'println',
        'input': 'scala.io.StdIn.readLine()',
        'self': 'this',
        'lambda': '=>',
        '#': '//',
        'return': 'return'},

    ('Python', 'Pascal'): {
        'def': 'procedure',
        'print': 'writeln',
        'input': 'readln',
        'self': '',
        '#': '//',
        'return': 'exit'},

    ('Python', '1C'): {
        'def': 'Процедура',
        'print': 'Сообщить',
        'input': '',
        'self': 'ЭтотОбъект',
        '#': '//',
        'return': ''},

    ('Python', 'PHP'): {
        'def': 'function',
        'print': 'echo',
        'input': 'readline',
        'self': '$this',
        'lambda': 'function',
        '#': '//',
        'True': 'true',
        'False': 'false',
        'None': 'null',
        'return': 'return'},

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

