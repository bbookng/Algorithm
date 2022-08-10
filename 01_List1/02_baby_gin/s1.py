n = int(input())

for tc in range(1, n+1):
    arr = list(map(int, input()))
    check = [0] * 10                    # 0부터 9까지 숫자가 몇개 들어있는지 check_list
    triple = 0                          # triplit check
    run = 0                             # run check

    # arr의 각 숫자를 check list의 일치하는 idx에 +1
    for i in arr:
        for j in range(10):
            if i == j:
                check[j] += 1

    # triplit 을 count 하는 반복문
    for i in range(len(check)):
        while True:                     # triplit이 같은 수로 2개일 수 있으므로 while문 사용
            if check[i] >= 3:           # check[i] 가 3 이상이면 tripit
                triple += 1             # triplit 에 1 추가
                check[i] -= 3
                continue
            else:
                break

    # run 을 count 하는 반복문
    for x in range(0, 8):
        while True:
            if check[x] and check[x+1] and check[x+2]:      # check list에서 연속 3개가 True (1이상) 이면
                run += 1                                    # run + 1
                check[x] -= 1
                check[x+1] -= 1
                check[x+2] -= 1
                continue
            else:
                break

    if triple + run == 2:           # triplit과 run의 합이 2이면 baby-gin
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

