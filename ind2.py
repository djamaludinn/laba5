#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input('Введите слова: ')
    a = s.find('жи')
    b = s.find('жы')
    if a > -1:
        print('жи написанно правильно')
    if b > -1:
        print('жи написанно неправильно')
    c = s.find('ши')
    d = s.find('шы')
    if c > -1:
        print('ши написанно правильно')
    if d > -1:
        print('ши написанно неправильно')
    s = s.replace('жы', 'жи').replace('шы', 'ши')
    print(s)