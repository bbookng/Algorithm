import sys
sys.stdin = open('input.txt')

def find(x):
    if x != p[x]:
        return find(p[x])
    return x

def union(a, b):
    p[find(b)] = find(a)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    p = [i for i in range(N+1)]

    for i in range(0, M*2, 2):
        a, b = arr[i], arr[i+1]
        union(a, b)

    for i in range(1, N+1):
        if i == p[i]:
            cnt += 1

    print(f'#{tc} {cnt}')
