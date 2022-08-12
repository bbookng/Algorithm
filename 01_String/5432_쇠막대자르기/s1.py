import sys
sys.stdin = open('5432.txt')

def sol(arr):
    cnt = 0
    total = cnt
    flag = False
    for i in arr:
        if i == '(':
            cnt += 1
            flag = True
        else:
            if flag == True:
                cnt -= 1
                total += cnt
                flag = False
            else:
                cnt -= 1
                total += 1

    return total


T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    print(f'#{tc} {sol(arr)}')