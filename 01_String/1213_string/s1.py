import sys
sys.stdin = open('1213.txt', 'rt', encoding='UTF8')

def sol(target, sentence):
    cnt = sentence.count(target)
    return cnt

T = 10
for tc in range(1, T+1):
    n = int(input())
    target = input()
    sentence = input()
    print(f'#{tc} {sol(target, sentence)}')