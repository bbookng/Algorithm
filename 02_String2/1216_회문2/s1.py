import sys
sys.stdin = open('12161.txt')

def sol(arr):
    for k in range(100, -1, -1): # 팰린드롬 범위
        for i in range(100):    # 행
            for j in range(100-k+1):  # 열
                # arr[i] 행 j부터 j+k까지 똑같으면
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    return k        # k 반환

T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [input() for i in range(100)] # 가로
    arr2 = list(zip(*arr))  # 세로
    # 가로, 세로 중 max 반환
    print(f'#{tc} {max(sol(arr),sol(arr2))}')

