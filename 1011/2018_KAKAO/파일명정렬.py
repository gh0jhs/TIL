def solution(files):
    answer = []
    HEAD = []
    NUMBER = []
    ANS = []
    for i in range(len(files)):
        visit = False 
        cnt = 0
        for j in range(len(files[i])):
            if files[i][j] in '1234567890' and visit == False: # num_start 값 구하기
                num_start = j
                visit = True # num_start 값을 구하면 True
            if files[i][j] in '1234567890' and j == len(files[i])-1 and visit == True: # TAIL없이 숫자로 끝날 경우
                num_end = j
                break
            if files[i][j] not in '1234567890' and visit == True: # 숫자가 아닌 다른 문자가 오면 num_end 값
                num_end = j-1
                break
            if files[i][j] in '1234567890': # 숫자 5개 이상
                cnt += 1
                if cnt == 5:
                    num_end = j
                    break
            
        HEAD.append(files[i][:num_start].lower())
        NUMBER.append(int(files[i][num_start:num_end+1]))
        ANS.append([HEAD[i], NUMBER[i], i])
    # print(ANS)
    ANS.sort()

    for i in range(len(files)):
        answer.append(files[ANS[i][2]])
    return answer