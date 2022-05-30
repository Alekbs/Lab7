#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))

    # Сумма положительных
    sum = 0
    for item in A:
        if item > 0:
            sum += item

    # Поиск минимального и максимального по модулю
    min_A = abs(A[1])
    max_A = abs(A[1])
    Min, Max = 0, 0
    for i, item in enumerate(A):
        if abs(item) < min_A:
            min_A = abs(item)
            Min = i
        if abs(item) > max_A:
            max_A = abs(item)
            Max = i

    # Поиск произведения
    if Min > Max:
        Min, Max = Max, Min
    s = 1
    for i in range(Min + 1, Max):
        s *= A[i]
    if Max - Min == 1:
        s = 0

    print(
        "Sum =", sum, "\nProduct =", s, "\nSorted list:", sorted(A, reverse=True)
    )
