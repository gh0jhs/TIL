import sys
sys.stdin = open('input.txt')
#
tc = int(input())
result = []
for _ in range(tc):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    x = 0
    while True:
        for i in range(k, 0, -1):

