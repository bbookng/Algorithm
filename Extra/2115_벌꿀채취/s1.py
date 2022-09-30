import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split()))]