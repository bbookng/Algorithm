import sys
sys.stdin = open('4873.txt')

def sol(N):
    check = []
    for i in N:
        if len(check) != 0 and i == check[-1]:  # i와 check의 마지막 요소가 같으면
            check.pop()                         # 반복문자 이므로 빼준다
        else:
            check.append(i)                     # 그렇지 않으면 check에 추가
    return len(check)

T = int(input())

for tc in range(1, T+1):
    N = input()
    print(f'#{tc} {sol(N)}')