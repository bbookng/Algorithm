import sys
sys.stdin = open('4865.txt')

def sol(str1, str2):
    max_ = 0
    for i in str1:
        if str2.count(i) > max_:
            max_ = str2.count(i)
    return max_


T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    print(f'#{tc} {sol(str1, str2)}')
