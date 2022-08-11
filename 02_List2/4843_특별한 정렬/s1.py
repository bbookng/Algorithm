import sys
sys.stdin = open('4843.txt')

# def sol(N, arr):
#     result = []
#     arr.sort()
#     for i in range(N//2):
#         result.append(arr[-1 + -i])
#         result.append(arr[i])
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     ans = sol(N, arr)
#     print(f'#{tc}', end=' ')
#     print(*ans[0:10])
#


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []

    arr.sort()

    for i in range(N // 2):         # 1회에 앞뒤로 넣을거기 때문에 절반만큼 반복
        result.append(arr[-1 + -i]) # 뒤 출력
        result.append(arr[i])       # 앞 출력

    print(f'#{tc}', end=' ')
    print(*result[0:10])        # 10개까지 출력