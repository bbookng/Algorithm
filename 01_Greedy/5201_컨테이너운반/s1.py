import sys
sys.stdin = open('input.txt')

def solution():
    result = 0
    while limit and weight:
        if max(weight) > max(limit):
            weight.pop()
        else:
            tmp = weight.pop()
            result += tmp
            limit.pop()
    return result


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    limit = list(map(int, input().split()))
    weight.sort()
    limit.sort()

    print(f'#{tc} {solution()}')