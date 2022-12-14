import sys
sys.stdin = open('input.txt')

dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4':4, '5': 5,
       '6': 6, '7': 7, '8': 8, '9': 9,
       'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def solution(num):
    result = ''
    while num:
        result = str(num % 2) + result
        num //= 2
    return result.zfill(4)

T = int(input())

for tc in range(T):
    a = input()
    tmp = ''
    for i in a:
        tmp += solution(dic[i])

    result = []

    N = len(tmp) // 7 + 1 if len(tmp) % 7 else len(tmp) // 7

    for i in range(N):
        total = 0
        cnt = 0
        for j in range(6, -1, -1):
            try:
                if tmp[(i * 7) + j] == '1':
                    total += 2 ** (6 - j - cnt)
            except:
                cnt += 1


        result.append(total)
    print(*result)