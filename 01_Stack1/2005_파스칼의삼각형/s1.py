import sys
sys.stdin = open('2005.txt')

def sol(i, arr):
    if i > N:                               # N번째 줄까지 출력했으며
        return                              # return
    if i == 1:                              # i가 1일때
        print("1")
        sol(i+1, [1])                       # i가 2일때를 위해 실행
    else:                                   # cf ) i번째 줄에는 숫자가 i개 들어감
        result = [0] * (i - 2)              # 밑에서 양 끝에 1을 추가함으로 i-2개의 result를 만들어줌
        for k in range(0, len(arr)-1):      # 윗줄 list 탐색
            result[k] = arr[k] + arr[k+1]   # k를 기준으로 k, k+1을 더해서 새로운 result에 추가
        result = [1] + result + [1]         # 더해진 result에 양 끝으로 1을 추가
        print(*result)                      # i 줄 출력
        sol(i+1, result)                    # N줄 출력될때까지 i+1 해서 재귀

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    sol(1, [])


