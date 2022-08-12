import sys
sys.stdin = open('p1.txt')

def sol1(word):
    return word[::-1]

def sol2(word):
    word = list(word)
    word.reverse()
    word = ''.join(word)
    return word

def sol3(word):
    word = list(word)
    for i in range(len(word)//2):
        word[i], word[-1-i] = word[-1-i], word[i]
    return ''.join(word)

def sol4(word):
    word = list(word)
    result = []
    for i in range(len(word)):
        result.append(word[-1])
        word.pop()
    return ''.join(result)

T = int(input())
for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {sol1(word)}')
    print(f'#{tc} {sol2(word)}')
    print(f'#{tc} {sol3(word)}')
    print(f'#{tc} {sol4(word)}')


