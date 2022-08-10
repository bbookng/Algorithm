tc = int(input())                           # 입력받을 test case의 갯수

for i in range(tc):                         # test case 만큼 반복
    num = int(input())                      # 칸 길이 (?)
    arr = list(map(int, input().split()))   # 각 칸에 상자가 몇개 쌓여 있는지
    max_ = 0                                # 가장 큰 낙차 값

    for j in range(num):                    # 칸의 처음부터 끝까지 반복
        cnt = 0                             # 같은 높이의 상자 끼리의 거리 count
        for k in range(j, num):             # j번째 요소를 기준으로 num의 크기만큼 반복해서 비교
            if arr[j] > arr[k]:             # arr의 j번째 요소가 k번째 요소보다 크면
                cnt += 1                    # count + 1
        if cnt > max_:                      # 거리 (count)의 수가 max_보다 크면
            max_ = cnt                      # 최댓값 갱신

    print(f'#{i+1} {max_}')                 # tc 마다 출력

