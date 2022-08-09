import sys
sys.stdin = open('1208.txt')

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):                       # 덤프 수만큼
        boxes[boxes.index(max(boxes))] -= 1     # 최고높이에서 -1
        boxes[boxes.index(min(boxes))] += 1     # 최저높이에서 +1


    print(f'#{tc} {max(boxes)-min(boxes)}')


