import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 2)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    while N:
        if tree[N//2] == 0:
            tree[N//2] = tree[N // 2 * 2] + tree[N // 2 * 2 + 1]
        N -= 1
    print(f'#{tc} {tree[L]}')