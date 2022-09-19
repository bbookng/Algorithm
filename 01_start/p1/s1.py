import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(T):
    arr = list(input())
    result = []
    for i in range(len(arr)//7):
        tmp = 0
        for j in range(6, -1, -1):
            if arr[(i*7)+j] == '1':
                tmp += 2**(6-j)
        result.append(tmp)
    print(*result)
