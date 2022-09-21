arr = [3, 6, 7]
n = len(arr)

bit = [0] * n

def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end = ' ')
        print()
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)

f(0, n)

# 모든 부분집합 출력
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1, 1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()

def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

A = [1, 2, 3, 4, 5]
n = len(A)
r = 3
comb = [0] * r

nCr(n, r, 0)