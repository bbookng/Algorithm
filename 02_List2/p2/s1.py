T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 0                      # result 기본값은 0
    for i in range(1 << 10):        # 부분집합의 갯수는 2**n이니까 2**10만큼 반복
        tmp = []                    # 부분집합을 저장할 임시 리스트
        for j in range(10):         # 원소의 수만큼 비트를 비교
            if i & (1<<j):          # i의 j번 비트가 1인 경우
                tmp.append(arr[j])  # tmp에 추가
            if len(tmp) != 0 and sum(tmp) == 0: # tmp가 공집합이 아니고 tmp의 합이 0이면
                result = 1          # result = 1
                break               # 확인완료. 더 이상 반복안해도 됨
    print(f'#{tc} {result}')






