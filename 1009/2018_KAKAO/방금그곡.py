def solution(m, musicinfos):
    answer = ''
    data = []
    for i in range(len(musicinfos)):
        data.append(musicinfos[i].split(','))
        
    music_time = []
    for i in range(len(data)):
        time = 0
        time += (int(data[i][1][:2]) * 60 + int(data[i][1][3:])) - (int(data[i][0][:2]) * 60 + int(data[i][0][3:]))
        music_time.append(time)
        
    # C# : Q, D# : W, F# : E, G# : R, A# : T
    for i in range(len(m)):
        m = m.replace('C#', 'Q')
        m = m.replace('D#', 'W')
        m = m.replace('F#', 'E')
        m = m.replace('G#', 'R')
        m = m.replace('A#', 'T')
    
    for i in range(len(data)):
        data[i][3] = data[i][3].replace('C#', 'Q')
        data[i][3] = data[i][3].replace('D#', 'W')
        data[i][3] = data[i][3].replace('F#', 'E')
        data[i][3] = data[i][3].replace('G#', 'R')
        data[i][3] = data[i][3].replace('A#', 'T')
        
    music_string = ''
    for i in range(len(music_time)):
        cnt = 0
        j = 0
        while cnt != music_time[i]:
            music_string += data[i][3][j]
            cnt += 1
            j += 1
            if j == len(data[i][3]):
                j = 0
    print(music_string)
    if m not in music_string:
        answer = '(None)'
        
    else:
        ans_idx = []
        temp = 0
        while True:
            ms = music_string.find(m, temp)
            ans_idx.append(ms)
            if music_string.find(m, ms + len(m)) == -1:
                break
            temp = ms + len(m)
        
        visited = [0] * len(data)
        ts = te = 0
        for i in range(len(music_time)):
            ts = te
            te = ts + music_time[i]
            for j in range(len(ans_idx)):
                if ts <= ans_idx[j] < te:
                    visited[i] = 1
                    break

        max_temp = 0
        idx = 0
        for i in range(len(music_time)):
            if visited[i] == 1 and music_time[i] > max_temp:
                idx = i
                max_temp = music_time[i]

        answer = data[idx][2]
        
    return answer