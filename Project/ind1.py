#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    s = 1

    for item in A:
        if item > 0:
            s *= item
    s1 = 0
    for i in A:
        if i == 1:
            s1 += 1

    if s == 1:
        if s1 == 0:
            print("0")
        else:
            print("1")
    else:
        print(s)
