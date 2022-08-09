import sys
sys.stdin = open('4831.txt')

T = int(input())

def sol(n, k, arr):
    location = 0                    # 현재 위치
    count = 0                       # 충전 횟수
    while True:
        if location + k >= n:       # 현재 위치 + k가 종점보다 크거나 같으면
            return count            # 도착했다는 의미로 count값 반환
        # 앞의 set는 현재 갈 수 있는 범위, 뒤의 set는 충전소 list 교집합으로 갈 수 있는 충전소 찾기
        charge = set(range(location+k, location, -1)) & set(arr)
        if charge:          # charge 값이 0 이 아니면 (있으면)
            location = max(charge)  # 현재 위치를 현재 갈 수 있는 충전소 중 가장 먼 곳으로
            count += 1              # 충전 완료
            continue

        return 0


for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {sol(n, k, arr)}')


















