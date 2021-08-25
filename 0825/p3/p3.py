# bfs 연습

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
#
#
# def bfs(G, v):
#     visited = [0]*n
#     queue = []
#     queue.append(v)
#
#     while queue:
#         t = queue.pop(0)
#         if not visited[t]:
#             visited[t] = True
#             visit(t)
#             for i in G[t]:
#                 if not visited[i]:
#                     queue.append(i)



# arr = list(map(int, input().split()))
# data = [[0 for _ in range(8)] for _ in range(8)]
# for i in range(0, len(arr), 2):
#     data[arr[i]][arr[i+1]] = data[arr[i+1]][arr[i]] = 1
# visited = [0 for _ in range(8)]
# queue = []
# front = -1
# rear = -1
#
# s = 1
# queue.append(s)
# rear += 1
# visited[s] = 1
#
# while rear != len(data) - 2:
#     for j in range(len(data)):
#         if data[s][j] == 1 and visited[j] == 0:
#             queue.append(j)
#             visited[j] = 1
#             rear += 1
#     s += 1
#
# while front != rear:
#     print(queue.pop(0))
#     front += 1



# def bfs(data, start):
#     global visited
#     visited[start] = 1
#     queue = []
#     queue.append(start)
#
#     while queue:
#         t = queue.pop(0)
#         start = t
#         print(t, end=' ')
#
#         for i in range(8):
#             if data[start][i] == 1 and visited[i] == 0:
#                 queue.append(i)
#                 visited[i] = 1
#
#
#
# arr = list(map(int, input().split()))
# data = [[0 for _ in range(8)] for _ in range(8)]
# for i in range(0, len(arr), 2):
#     data[arr[i]][arr[i+1]] = data[arr[i+1]][arr[i]] = 1
# visited = [0 for _ in range(8)]
# bfs(data, 1)

# from collections import deque
# def bfs(data, start):
#     global visited
#     visited[start] = 1
#     queue = deque([start])
#
#     while queue:
#         t = queue.popleft()
#         start = t
#         print(t, end=' ')
#
#         for i in range(8):
#             if data[start][i] == 1 and visited[i] == 0:
#                 queue.append(i)
#                 visited[i] = 1
#
#
#
# arr = list(map(int, input().split()))
# data = [[0 for _ in range(8)] for _ in range(8)]
# for i in range(0, len(arr), 2):
#     data[arr[i]][arr[i+1]] = data[arr[i+1]][arr[i]] = 1
# visited = [0 for _ in range(8)]
# bfs(data, 1)
