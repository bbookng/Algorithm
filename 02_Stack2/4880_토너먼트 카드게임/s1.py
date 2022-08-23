import sys
sys.stdin = open('4880.txt')
sys.setrecursionlimit(10000)

def game(a, b):
    if arr[a] == arr[b]:
        return arr[a]
    elif arr[a]-arr[b] == 1 or arr[b]-arr[a] == 2:
        return arr[a]
    else:
        return arr[b]

def action(S, E):
    if len(arr) == 1:
        return N
    tmp = len(arr) // 2
    first = arr[:tmp+1]
    second = arr[tmp+1:]
    first = action(first)
    second = action(second)
    return game(first[0], second[0])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(action(arr))



