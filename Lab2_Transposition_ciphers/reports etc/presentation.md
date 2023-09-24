---
# Front matter
title: "Лабораторная работа 2"
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

##### ПРЕЗЕНТАЦИЯ ПО ЛАБОРАТОРНОЙ РАБОТЕ №2

дисциплина: Математические основы защиты информации и информационной безопасности

Преподователь: Кулябов Дмитрий Сергеевич

Cтудент: Терентьев Егор Дмитриевич

Группа: НФИмд-01-23

МОСКВА

2023 г.

# **Прагматика выполнения лабораторной работы**

Требуется реализовать:

1. Маршрутное шифрование.
2. Шифрование с помощью решеток.
3. Табоица Виженера

# **Цель работы**

Освоить на практике шифры перестановки.

# **Выполнение лабораторной работы**

# 1. Для реализации маршрутного шифрования: 
1. Функции проверки правильности пароля, значения k
2. Функция берущая столбцы матрицы в виде ключа буквы пароля в алфавитном порядке (был использован словарь для удобства)

![route_funcs](pics/1_route_funcs.png "route funcs")

# 2. Основная фунция запуска где получаем входные значения и шифруем слово

![route_main_func](pics/2_route_main_func.png "route main func")

# 3. Запуск программы маршрутного шифрования

![route_output](pics/3_route_output.png "route output")

# 4. Для реализации шифрования с помощью решеток:
1. Функция генерирующая сетку (матрицу) (использована библиотека numpy Для удобства) и ее заполнение
2. Функция заполняющая сетку значениями букв из текста и переворачивающая матрицу
3. Функция выбираюшая столбцы в алфавитном порядке пароля
4. Функция объединяющая все вышепоказанные функции и проверки правильности введенных данных

![grid_funcs](pics/4_grid_funcs.png "grid funcs")

# 5. Основная фунция запуска функции шифрования с помощью решеток

![grid_main_func](pics/5_grid_main_func.png "grid main func")

# 6. Запуск программы атбаш

![grid_output](pics/6_grid_output.png "grid output")

# 7. Для реализации Таблицы Виженера:
1. Функция шифрования (построение таблицы Вижинера)
2. Функция дешифровки

![vigenere_funcs](pics/7_vigenere_funcs.png "vigenere funcs")

# 8. Основная фунция запуска функции Таблицы Виженера

![vigenere_main_func](pics/8_vigenere_main_func.png "vigenere main func")

# 9. Запуск программы Таблицы Виженера

![vigenere_output](pics/9_vigenere_output.png "vigenere output")

# Выводы

В результате выполнения работы я освоил на практике применение шифров перестановки.
