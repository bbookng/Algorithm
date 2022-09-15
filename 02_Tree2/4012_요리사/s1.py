import sys
from itertools import combinations
# sys.stdin = open('input.txt')

def solution():
    result = 0
    for i in combi:
        for j in i:




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    combi = combinations(range(N), N//2)
    print(list(combi))