import sys
sys.stdin = open('input.txt')

password = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

def getResult(passwords):
    temp = 0
    for p in passwords:

        even = 0
        odd = 0
        for pi in range(8):
            if pi % 2:
                even += int(p[pi])
            else:
                odd += int(p[pi])

        if (odd * 3 + even) % 10 == 0:
            temp += (odd + even)

    return temp


def findI(b_line):
    i = 1
    while True:
        for j in range(7):
            if b_line[len(b_line) - 7 * (j + 1) * i:len(b_line) - 7 * j * i:i] not in password:
                i += 1
                break

        if j == 6:
            return i


def findPassword(tmp):
    pw = ''
    while tmp:
        now = tmp[:7]
        tmp = tmp[7:]
        if now in password:
            pw += str(password[now])
        else:
            break

    return pw


T = int(input())

for tc in range(1, T+1):
    results = []
    passwords = set()
    N, M = map(int, input().split())
    arr = list(set(input().strip().strip('0') for _ in range(N)))

    for line in arr:
        if line: # 0만 있는 곳이 아닐 때,
            b_line = ''
            for k in range(len(line)):
                b_line += bin(int(line[k], base=16)).replace('0b', '').zfill(4)

            b_line = b_line.zfill(4 * M).rstrip('0')

            while b_line:
                i = findI(b_line)
                tmp = b_line[len(b_line) - 56 * i:len(b_line):i]
                b_line = b_line[:len(b_line) - 56 * i]

                pw = findPassword(tmp)

                if len(pw) == 8:
                    passwords.add(pw)

                b_line = b_line.rstrip('0')

    result = getResult(passwords)

    print(f'#{tc} {result}')






