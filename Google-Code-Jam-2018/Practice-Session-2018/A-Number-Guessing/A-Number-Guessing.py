# Problem A: Number Guessing
# URL: https://codejam.withgoogle.com/2018/challenges/0000000000000130/dashboard

import math


def GuessNumber(a, b, n):
    for i in range(n):
        if a >= b:
            return
        guess = math.ceil((a + b) / 2)
        print(guess)
        judge = input()
        if judge == "CORRECT":
            return
        elif judge == "TOO_SMALL":
            a = guess
        elif judge == "TOO_BIG":
            b = guess - 1


t = int(input())
for i in range(1, t + 1):
    (a, b) = (int(s) for s in input().split(" "))
    n = int(input())
    GuessNumber(a, b, n)
