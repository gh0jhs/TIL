lst = list(map(int, input().split(', ')))
arr = [[0 for _ in range(max(lst))] for _ in range(max(lst))]
for i in range(0,len(lst),2):
    a = lst[i] - 1
    b = lst[i+1] - 1
    arr[a][b] = arr[b][a] = 1

stack = []
visited =[False for _ in range(max(lst))]

i = 0
stack.append(1)
visited[0] = True
top = -1
while top != -2:
    for j in range(len(arr)):
        if arr[i][j] == 1 and visited[j] == False:
            stack.append(j+1)
            visited[j] = True
            i = j
            top += 1
            break
    else:
        top -= 1
        i = top
print(stack)