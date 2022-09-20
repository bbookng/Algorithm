import sys
sys.stdin = open('input.txt')

dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4':4, '5': 5,
       '6': 6, '7': 7, '8': 8, '9': 9,
       'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

pattern = {0: '001101', 1: '010011', 2: '111011',
           3: '110001', 4: '100011', 5: '110111',
           6: '001011', 7: '111101', 8: '011001',
           9: '101111'}

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
    cnt = 0

    for i in range(len(tmp)):
        for j in range(10):
            if tmp[cnt:cnt+6] == pattern[j]:
                result.append(j)
                cnt += 6
                break
        else:
            cnt += 1

    print(*result)





