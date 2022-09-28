import sys
sys.stdin = open('input.txt')

def QuickSort(arr, s, e):
    if s >= e:
        return
    p = s
    left, right = s+1, e

    while left <= right:
        while left <= e and arr[left] <= arr[p]:
            left += 1
        while right > s and arr[right] >= arr[p]:
            right -= 1
        if left > right:
            arr[right], arr[p] = arr[p], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]
        QuickSort(arr, s, right-1)
        QuickSort(arr, right+1, e)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    QuickSort(arr, 0, len(arr)-1)
    print(*arr)
