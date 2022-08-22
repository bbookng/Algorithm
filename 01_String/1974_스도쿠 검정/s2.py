import sys
sys.stdin = open('1974.txt')

def sol(arr):
    for i in range(9):
        check = []
        for j in range(9):
            if arr[i].count(arr[i][j]) >= 2:
                return 0
            if arr[j][i] in check:
                return 0
            else:
                check.append(arr[j][i])


    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = []
            for k in range(3):
                for l in range(3):
                    if arr[i+k][j+l] in check:
                        return 0
                    else:
                        check.append(arr[i][j])

    return 1




T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {sol(arr)}')