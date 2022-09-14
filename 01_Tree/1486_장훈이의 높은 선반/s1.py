import sys
sys.stdin = open('input.txt')

def solution(idx):
    global result, tmp
    if tmp >= B and tmp - B < result:
        result = tmp - B
    if idx < N:
        tmp += arr[idx]
        solution(idx + 1)
        tmp -= arr[idx]
        solution(idx + 1)




T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    result, tmp = float('inf'), 0
    solution(0)

    print(f'#{tc} {result}')