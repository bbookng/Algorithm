import sys
sys.stdin = open('5097.txt')

def sol(M, arr):
    stack = []
    for i in range(M):
        stack.append(arr.pop(0))
        arr.append(stack.pop())
    return arr[0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {sol(M, arr)}')