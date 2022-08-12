import sys
sys.stdin = open('1221.txt')

def sol(n, length, arr):
    check = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in range(int(length)):
        arr[i] = check.index(arr[i])
    arr.sort()
    for i in range(int(length)):
        arr[i] = check[arr[i]]
    return ' '.join(arr)


T = int(input())
for tc in range(1, T+1):
    n, length = input().split()
    arr = list(input().split())
    print(f'#{tc}')
    print(f'{sol(n, length, arr)}')