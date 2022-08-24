import sys
sys.stdin = open('1225.txt')

def sol(arr):
    tmp = arr.pop(0)                # tmp는 제일 앞 순서 숫자
    while tmp > 0:                  # tmp가 양수일 동안 반복
        for i in range(1, 6):       # 1부터 5까지 한 싸이클 반복
            tmp -= i                # 빼기 빼기 빼기 빼기 빼기
            if tmp > 0:             # tmp가 양수이면
                arr.append(tmp)     # 맨 뒤에 추가
            else:                   # 양수 아니면
                arr.append(0)       # 맨 뒤에 0 넣고
                return              # return
            tmp = arr.pop(0)        # tmp는 다시 맨 앞 숫자


T = 10
for tc in range(1, T+1):
    n = input()
    arr = list(map(int, input().split()))
    sol(arr)
    print(f'#{tc}', *arr)