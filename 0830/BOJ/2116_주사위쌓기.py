n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt_list = []
for first_top in range(1,7):
    cnt = 0
    top = first_top
    for i in range(len(arr)):
        bottom = top
        bot_idx = arr[i].index(bottom)
        if bot_idx == 0:
            top = arr[i][5]
        elif bot_idx == 1:
            top = arr[i][3]
        elif bot_idx == 2:
            top = arr[i][4]
        elif bot_idx == 3:
            top = arr[i][1]
        elif bot_idx == 4:
            top = arr[i][2]
        elif bot_idx == 5:
            top = arr[i][0]
        if top == 6:
            cnt += 1
            if bottom == 5:
                cnt += 1
        elif bottom == 6:
            cnt += 1
            if top == 5:
                cnt += 1
    cnt_list.append(cnt)
print(6*n - min(cnt_list))