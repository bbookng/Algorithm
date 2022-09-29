import sys
sys.stdin = open('input.txt')
from itertools import permutations
import math

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    operator = []
    numbers = list(map(int, input().split()))
    for i in range(4):
        if i == 0:
            for j in range(arr[i]):
                operator.append('+')
        elif i == 1:
            for j in range(arr[i]):
                operator.append('-')
        elif i == 2:
            for j in range(arr[i]):
                operator.append('*')
        elif i == 3:
            for j in range(arr[i]):
                operator.append('/')

    data = list(set(permutations(operator, len(operator))))

    _max = 0
    _min = 0
    for i in data:
        tmp = numbers[0]
        for j in range(len(i)):
            if i[j] == '+':
                tmp += numbers[j+1]
            elif i[j] == '-':
                tmp -= numbers[j+1]
            elif i[j] == '*':
                tmp *= numbers[j+1]
            elif i[j] == '/':
                tmp /= numbers[j+1]
                tmp = math.trunc(tmp)
        _max = max(_max, tmp)
        _min = min(_min, tmp)

    print(f'#{tc} {_max - _min}')


