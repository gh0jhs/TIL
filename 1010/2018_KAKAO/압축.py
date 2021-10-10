def solution(msg):
    answer = []
    dict = {}
    # 아스키코드
    for i in range(65, 91):
        dict[chr(i)] = i - 64
        
    k = 27
    visited = [0] * len(msg)
    last = False
    
    for i in range(len(msg)):
        if visited[i] == 1:
            continue
        for j in range(i+1, len(msg)):
            w = msg[i:j+1]
            visited[j-1] = 1
            
            if dict.get(w) == None:
                dict[w] = k
                k += 1
                answer.append(dict[msg[i:j]])
                break
                
            if j == len(msg) -1:
                answer.append(dict[msg[i:]])
                last = True
                
    if last == False:
        answer.append(dict[msg[-1]])
    return answer