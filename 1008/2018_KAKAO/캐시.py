def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        answer = 5 * len(cities)
    
    else:
        for i in range(len(cities)):
            cities[i] = cities[i].lower()
        
        cache = []
        cache_num = []
        
        for i in range(len(cities)):
            if cities[i] in cache:
                cache_num[cache.index(cities[i])] = 0
                answer += 1
            else:
                if len(cache) != cacheSize:
                    cache.append(cities[i])
                    cache_num.append(0)
                else:
                    max_idx = cache_num.index(max(cache_num))
                    cache[max_idx] = cities[i]
                    cache_num[max_idx] = 0
                answer += 5
                    
            for k in range(len(cache_num)):
                cache_num[k] += 1
                    
    return answer