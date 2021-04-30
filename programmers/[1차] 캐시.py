def solution(cacheSize, cities):
    up = []
    for i in cities :
        up.append(i.upper())
    cities = up
    cache = []
    running_time = 0
    if cacheSize == 0 :
        return len(cities) * 5
    while cities :
        a = cities.pop(0)
        if len(cache) < cacheSize :
            if a in cache :
                cache.append(a)
                running_time += 1
            else :
                cache.append(a)
                running_time += 5
        else :
            if a in cache :
                cache.remove(a)
                cache.append(a)
                running_time += 1
            else :
                cache.pop(0)
                cache.append(a)
                running_time += 5
    print(running_time)

solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])