---
# Front matter
title: "Математические основы защиты информации и информационной безопасности. Отчет по лабораторной работе №1"
subtitle: "Шифры простой замены"
author: "Терентьев Егор Дмитриевич 1132236902"
group: "НФИмд-01-23"
institute: RUDN University, Moscow, Russian Federation

# Generic otions
lang: ru-RU
toc-title: "Содержание"

# Bibliography
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

# Pdf output format
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
### Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Misc options
indent: true
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Освоить на практике шифры простой замены.

# Выполнение лабораторной работы

Требуется реализовать:

1. Шифр Цезаря с произвольным ключом K.
2. Шифр Атбаш.

## Шифр цезаря

Шифр Цезаря (также он является шифром простой замены) — это моноалфавитная подстановка, т.е. 
каждой букве открытого текста ставится в соответствие одна буква шифртекста. 
На практике при создании шифра простойзамены в качестве шифроалфавита берется исходный алфавит, но с нарушеннымпорядком букв (алфавитная перестановка). 
Для запоминания нового порядкабукв перемешивание алфавита осуществляется с помощью пароля. 
В качествепароля могут выступать слово или несколько слов с неповторяющимися буквами.
Шифровальная таблица состоит из двух строк: в первой записывается стандартный алфавит открытого текста, 
во второй — начиная с некоторой позицииразмещается пароль (пробелы опускаются), 
а далее идут в алфавитном порядке оставшиеся буквы, не вошедшие в пароль. 
В случае несовпадения начала пароля с началом строки процесс после ее завершения циклически продолжается с первой позиции. 
Ключом шифра служит пароль вместе с числом, указывающим положение начальной буквы пароля.

Чтобы реализовать программу был написал след. код на python:

Функция проверяющая правильность введенного ключа: это значение int и если оно больше значения алфавита, то получаем остаток [@fig:1].

![is_key](pics/1_is_key.png){#fig:1 width=100%}

Функция проверяющая введенное значения для пароля и слова для шифрования: нужно чтобы каждая буква входила в алфавит [@fig:2].

![correct_input_word](pics/2_correct_input_word.png){#fig:2 width=100%}

Функция добавляющая только уникальные буквы из слова (нужно для пароля) и функция создающая шифр-алфавит [@fig:3].

![unique_let_and_cipher_alphabet](pics/3_unique_let_and_create_code_alphabet.png){#fig:3 width=100%}

Функция шифрующая слово по шифр алфавиту [@fig:4]

![word_to_code](pics/4_word_to_code.png){#fig:4 width=100%}

Основная фунция запуска где получаем входные значения и шифруем слово [@fig:5]

![main_func_caesar](pics/5_main_func.png){#fig:5 width=100%}

Пример работы шифра как было показано в материалах к лабораторной работе [@fig:6]

![output_caesar](pics/6_caesar_cipher_in_action.png){#fig:6 width=100%}

## Шифр атбаш

Данный шифр является шифром сдвига на всю длину алфавита, состоящего из русских букв и пробела.

Чтобы реализовать программу был написал след. код на python:

Здесь реализована функция для проверки что каждая буква входит в алфавит (для входных значений), разворот алфавита, и кодировка слова с помощью шифр-алфавита [@fig:7]

![atbash_func](pics/7_atbash_funcs.png){#fig:7 width=100%}

Основная фунция запуска где получаем входные значения и шифруем слово [@fig:8]

![mainFunc_atbash](pics/8_atbash_main_func.png){#fig:8 width=100%}

Пример работы шифра [@fig:9]

![output_atbash](pics/9_atbash_output.png){#fig:9 width=100%}

# Выводы

В результате выполнения работы я освоил на практике применение шифров простой замены.

# Список литературы

1. Методические материалы курса
