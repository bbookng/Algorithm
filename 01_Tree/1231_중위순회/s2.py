import sys
sys.stdin = open('input.txt')

def inorder(now):
    if len(childs[now]) > 0:
        inorder(childs[now][0])
    print(values[now], end='')
    if len(childs[now]) > 1:
        inorder(childs[now][1])


T = 10
for tc in range(T):
    N = int(input())
    childs = [[] for _ in range(N+1)]
    values = [[-1] for _ in range(N+1)]
    for i in range(N):
        idx, value, *child = input().split()
        values[int(idx)] = value
        childs[int(idx)] = list(map(int, child))

    inorder(1)
    print()

