def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    
    # 터지면서 그래프가 새로 생성되서 While문 사용
    while True:
        visited = [[0 for _ in range(n-1)] for _ in range(m-1)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == 0: # 0은 같은 모양이어서 터졌을 때 0으로 값 변경
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    visited[i][j] = 1

        # 아무 것도 터지지 않아서 변경이 없으면 break
        if visited == [[0 for _ in range(n-1)] for _ in range(m-1)]:
            break

        answer = 0
        
        for i in range(m-1):
            for j in range(n-1):
                if visited[i][j] == 1:
                    board[i][j], board[i+1][j], board[i][j+1], board[i+1][j+1] = 0, 0, 0, 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    answer += 1

        # 0이면 빈자리가 생기니까 떨어지는 과정            
        while True:
            V = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] == 0:
                        continue
                    if board[i+1][j] == 0:
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        V = 1
            if V == 0:
                break
    return answer