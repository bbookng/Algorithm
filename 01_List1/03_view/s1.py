# tc = 10
# for i in range(1, tc+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     result = 0
#     for j in range(2, len(arr)):
#         high = 0
#         if arr[j] - arr[j-2] >= 1 and arr[j] - arr[j-1] >= 1 and arr[j] - arr[j+1] >= 1 and arr[j] - arr[j+2] >= 1:
#             arr2 = [arr[j-2], arr[j-1], arr[j+1], arr[j+2]]
#             result += (arr[j] - max(arr2))
#
#     print(f'#{i} {result}')
# #
#
# def check(array, N):
#
#
# for tc in range(1, 11):
#     N = int(input())
#     array = list(map(int, input().split()))
#     total = 0
#     for i in range(2, N - 2):
#         around_max = max(array[i - 2], array[i - 1], array[i + 2], array[i + 1])
#         if array[i] > around_max:
#             total += (array[i] - around_max)
#
#     print(f'#{tc} {total)}')
def custommax(*args):               # 내장함수 max 만들기
    max_ = 0
    for e in args:
        if e > max_:
            max_ = e
    return max_

def check(arr, N):
    total = 0                       # 조망권 확보된 총 세대 수
    for i in range(2, N-2):         # 맨앞,뒤 2칸 제외 반복
        _max = custommax(arr[i-2],arr[i-1],arr[i+2],arr[i+1])   # i 기준 전후 2건물 씩 4건물 중 젤 높은층
        if arr[i] > _max:           # i 건물이 _max 보다 크다면 (조망권이 확보됐다면)
            total += (arr[i] - _max)    # i 층 - max층 = 조망권 확보된 세대 수

    return total


for tc in range(1, 11):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {check(arr,N)}')