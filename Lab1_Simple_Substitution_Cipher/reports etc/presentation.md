---
# Front matter
title: "Лабораторная работа 1"
author: "Терентьев Егор Дмитриевич, НФИмд-01-23"

# Generic otions
lang: ru-RU
toc-title: "Содержание"

# Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

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

##### РОССИЙСКИЙ УНИВЕРСИТЕТ ДРУЖБЫ НАРОДОВ

##### Факультет физико-математических и естественных наук

##### ПРЕЗЕНТАЦИЯ ПО ЛАБОРАТОРНОЙ РАБОТЕ №1

дисциплина: Математические основы защиты информации и информационной безопасности

Преподователь: Кулябов Дмитрий Сергеевич

Cтудент: Терентьев Егор Дмитриевич

Группа: НФИмд-01-23

МОСКВА

2022 г.

# **Прагматика выполнения лабораторной работы**

Требуется реализовать:

1. Шифр Цезаря с произвольным ключом K.
2. Шифр Атбаш.

# **Цель работы**

Освоить на практике шифры простой замены.

# **Выполнение лабораторной работы**

# 1. Для реализации шифра цезаря создал функции: 
1. проверяющая правильность введенного ключа 
2. проверяющая введенное значения для пароля и слова для шифрования 
3. добавляющая только уникальные буквы из слова

![caesar_func_1](pics/pres_1.png "caesar func 1 part")

# 2. Также еще нужны функции создания шифр-алфавита и шифрования слова

![caesar_func_2](pics/pres_2.png "caesar func 2 part")

# 3. Основная фунция запуска где получаем входные значения и шифруем слово

![caesar_main_func](pics/5_main_func.png "main func")

# 4. Запуск программы

![output_caesar](pics/6_caesar_cipher_in_action.png "caesar output")

# 5. Для реализации шифра атбаш создал функции: 
1. для проверки что каждая буква входит в алфавит (для входных значений) 
2. разворот алфавита 
3. кодировка слова с помощью шифр-алфавита

![atbash_funcs](pics/7_atbash_funcs.png "atbash funcs")

# 6. Основная фунция запуска шифра Атбаш, где получаем входные значения и шифруем слово

![atbash_main_func](pics/8_atbash_main_func.png "atbash main func")

# 7. Запуск программы атбаш

![output_atbash](pics/9_atbash_output.png "atbash output")

# Выводы

В результате выполнения работы я освоил на практике применение шифров простой замены.
