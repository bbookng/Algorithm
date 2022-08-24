# import sys
# sys.stdin = open('4880.txt')
# sys.setrecursionlimit(10000)
#
def game(a, b):
    if arr[a][1] == arr[b][1]:
        return arr[a]
    elif arr[a][1]-arr[b][1] == 1 or arr[b][1]-arr[a][1] == 2:
        return arr[a]
    else:
        return arr[b]
#
# def action(S, E):
#     if len(arr) == 1:
#         return N
#     tmp = len(arr) // 2
#     first = arr[:tmp+1]
#     second = arr[tmp+1:]
#     first = action(first)
#     second = action(second)
#     return game(first[0], second[0])
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print(action(arr))
#



def solution(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    p1 = solution(arr[:mid])
    p2 = solution(arr[mid:])

    return game(p1[0], p2[0])





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(enumerate(map(int,input().split())))
    print(solution(arr)[0]+1)

