import sys
sys.stdin = open('input.txt')

def binary_search(arr, value):
    first, last = 0, len(arr)

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            last = mid - 1
        else:
            first = mid + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_N = list(map(int, input().split()))
    arr_M = list(map(int, input().split()))

    visited = [0, 0]
    for i in arr_N:
        binary_search()