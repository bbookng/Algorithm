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
    cnt = 0
    p = [i for i in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    for i in range(1, N+1):
        if i == p[i]:
            cnt += 1

    print(f'#{tc} {cnt}')


