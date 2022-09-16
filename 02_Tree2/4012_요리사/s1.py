import sys
from itertools import combinations
sys.stdin = open('input.txt')

def synergy(arr, com):
    result = 0
    for i in com:
        for j in com:
            result += arr[i][j]
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    combi = list(combinations(range(N), N//2))
    ans = float('inf')

    for i in combi:
        opp = list(set(range(N)) - set(i))
        synergy1 = synergy(arr, i)
        synergy2 = synergy(arr, opp)
        if ans > abs(synergy2-synergy1):
            ans = abs(synergy2-synergy1)

    print(f'#{tc} {ans}')


