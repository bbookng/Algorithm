import sys
sys.stdin = open('input.txt')
import math

def dfs(idx, total):
    global _max, _min
    if idx == N-1:
        _max = max(_max, total)
        _min = min(_min, total)
        return
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                tmp = total + numbers[idx+1]
            if i == 1:
                tmp = total - numbers[idx+1]
            if i == 2:
                tmp = total * numbers[idx+1]
            if i == 3:
                tmp = math.trunc(total / numbers[idx+1])
            dfs(idx+1, tmp)
            operator[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    _max = -float('inf')
    _min = float('inf')
    dfs(0, numbers[0])
    print(f'#{tc} {_max - _min}')


