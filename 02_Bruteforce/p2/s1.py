# import sys
# sys.stdin = open('input.txt')

def Babygin(A, s):
    n = len(A)
    if s == n-1:
        return
    min = s
    for i in range(s, n):
        if A[min] > A[i]:
            min = i
    A[s], A[min] = A[min], A[s]

    Babygin(A, s+1)


T = int(input())

for tc in range(T):
    S = list(map(int, input()))
    cnt = 0

    Babygin(S, 0)

    if S[0] == S[1] - 1 == S[2] - 2 or S[0] == S[1] == S[2]:
        cnt += 1
    if S[3] == S[4] == S[5] or S[3] == S[4] - 1 == S[5] - 2:
        cnt += 1

    if cnt == 2:
        print(True)
    else:
        print(False)

