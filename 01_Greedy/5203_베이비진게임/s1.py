import sys
sys.stdin = open('input.txt')

def babygin(player):
    check = [0] * 13
    for i in player:
        check[i] += 1

    for i in range(11):
        if check[i] >= 3:
            return True
        elif check[i] and check[i+1] and check[i+2]:
            return True

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1 = []
    player2 = []
    result = 0

    for i in range(12):
        if i % 2:
            player2.append(arr[i])
        else:
            player1.append(arr[i])

        if len(player1) >= 3 and len(player2) >= 3:
            if babygin(player1):
                result = 1
                break
            elif babygin(player2):
                result = 2
                break
    print(f'#{tc} {result}')



