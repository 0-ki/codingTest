def solution(participant, completion):
    # dict.get(x, '디폴트 값')
    # dict.items() key:value 쌍 튜플을 얻는다.
    
    # completion에 없는 participant 1명을 구하라
    d = {}
    # 이름을 key로, value는 0으로 들어갈 것임. 이미 있는 동명이인인 경우 +1 이 된다.
    for x in participant:
        d[x] = d.get(x,0) +1
    for x in completion:
        d[x] = d.get(x) - 1
    
    result = [k for k,v in d.items() if v > 0]
    return result[0]

print(sorted(['987','1000', '123', '99','0']))