def solution(str1, str2):
    str1 = list(str1)
    str2 = list(str2)

    # 아스키코드 이용해서 소문자로 변경 / 숫자나 공백 특수문자 들어가면 *로 변경
    for i in range(len(str1)):
        if 65 <= ord(str1[i]) <= 90:
            str1[i] = chr(ord(str1[i])+32)
        elif 97 <= ord(str1[i]) <= 122:
            continue
        elif str1[i] in '1234567890 ':
            str1[i] = '*'
        else:
            str1[i] = '*'
            
    for i in range(len(str2)):
        if 65 <= ord(str2[i]) <= 90:
            str2[i] = chr(ord(str2[i])+32)
        elif 97 <= ord(str2[i]) <= 122:
            continue
        elif str2[i] in '1234567890 ':
            str2[i] = '*'
        else:
            str2[i] = '*'

    list1 = []
    list2 = []
    
    # *이 들어갈 때를 제외하고 2글자씩 리스트에 추가
    for i in range(len(str1)-1):
        x = str1[i] + str1[i+1]
        if '*' not in x:
            list1.append(x)
    for i in range(len(str2)-1):
        x = str2[i] + str2[i+1]
        if '*' not in x:
            list2.append(x)
            
    if list1 == [] and list2 == []:
        ans = 1

    # 교집합 원소 수 구하기
    else:
        visited = [0 for _ in range(1000000)]
        a = 0 # 교집합
        b = 0 # 합집합
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j] and visited[j] == 0:
                    visited[j] = 1
                    a += 1
                    break
        b = len(list1) + len(list2) - a # 합집합 = A + B - 교집합
        ans = a/b

    answer = int(65536 * ans)
    return answer