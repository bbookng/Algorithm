import sys
sys.stdin = open('3143.txt')

def sol(A, B):
    cnt = 0
    idx = 0
    while idx < len(A):
        if A[idx] == B[0]:
            if A[idx:idx+len(B)] == B:
                cnt += 1
                idx = idx+len(B)
            else:
                cnt += 1
                idx += 1
        else:
            cnt += 1
            idx += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    print(f'#{tc} {sol(A, B)}')