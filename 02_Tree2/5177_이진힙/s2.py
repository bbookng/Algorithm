import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    tree = [0]
    arr = list(map(int, input().split()))

    for char in arr:
        tree.append(char)
        now = len(tree)-1
        while now > 1 and tree[now] < tree[now//2]:
            tree[now], tree[now//2] = tree[now//2], tree[now]
            now //= 2

    answer = 0
    now = N//2
    while now > 0:
        answer += tree[now]
        now //= 2


    print(answer)