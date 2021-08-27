import sys
sys.stdin = open('input.txt')

V = int(input())
E = V - 1
edge = list(map(int, input().split()))
left = [0 for _ in range(V+1)]
right = [0 for _ in range(V+1)]
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c


def preorder(v):
    if v:
        print(v, end=' ')
        preorder(left[v])
        preorder(right[v])

def inorder(v):
    if v:
        inorder(left[v])
        print(v, end=' ')
        inorder(right[v])

def postorder(v):
    if v:
        postorder(left[v])
        postorder(right[v])
        print(v, end=' ')

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()