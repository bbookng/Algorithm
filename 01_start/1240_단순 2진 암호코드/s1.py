import sys
sys.stdin = open('input.txt')

dic = {0: '0001101', 1: '0011001', 2: '0010011',
       3: '0111101', 4: '0100011', 5: '0110001',
       6: '0101111', 7: '0111011', 8: '0110111',
       9: '0001011'}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    tmp = ''
    for i in arr:
        if sum(i) == 0:
            continue
        else:
            i = ''.join(map(str, list(i)))
            for j in range(M-1, -1, -1):
                if i[j] == '1':
                    tmp = i[j-55:j+1]
                    break


    result = []
    cnt = 0

    for i in range(56):
        for j in range(10):
            if tmp[cnt:cnt+7] == dic[j]:
                cnt += 7
                result.append(j)
                break
        else:
            cnt += 1

    odd = 0
    even = 0

    for i in range(8):
        if i % 2:
            even += result[i]
        else:
            odd += result[i]

    ans = 0 if (odd * 3 + even) % 10 else odd + even

    print(f'#{tc} {ans}')