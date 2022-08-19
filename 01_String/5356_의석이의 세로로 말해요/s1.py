import sys
sys.stdin = open('5356.txt')

def sol(words):
    max_ = 0
    for i in words:
        if len(i) > max_:
            max_ = len(i)
    result = []

    for i in range(max_):
        for j in range(5):
            if len(words[j]) > i:
                result.append(words[j][i])
    return ''.join(result)



T = int(input())
for tc in range(1, T+1):
    words = [input() for i in range(5)]
    print(f'#{tc} {sol(words)}')
