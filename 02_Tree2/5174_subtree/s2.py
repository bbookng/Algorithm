import sys
sys.stdin = open('input.txt')

def preorder(now):
    global cnt
    cnt += 1
    for child in childs[now]:
        preorder(child)


T = int(input())

for _ in range(T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    childs = [[] for _ in range(E+2)]
    for i in range(0, len(arr), 2):
        childs[arr[i]].append(arr[i+1])

    cnt = 0
    preorder(N)
    print(cnt)