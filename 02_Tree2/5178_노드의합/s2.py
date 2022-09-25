import sys
sys.stdin = open('input.txt')

def postorder(now):
    if tree[now]:
        return tree[now]
    left, right = 0, 0
    if now*2 <= N:
        left = postorder(now*2)

    if now*2 + 1 <= N:
        right = postorder(now*2 + 1)

    tree[now] = left + right
    return tree[now]

T = int(input())
for _ in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        idx, number = map(int, input().split())
        tree[idx] = number
    print(tree)
    postorder(1)
    print(tree[L])


