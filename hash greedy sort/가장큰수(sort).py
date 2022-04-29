def sol(numbers):
    # list comprehension으로 각 수를 문자열로 다시 대입
    numbers = [str(x) for x in numbers]
    # 최대 1000의 길이인 수를 앞에 부터 비교하기 위해 1의 자리도 4자리(1000)과 맞추어 대조하도록 4를 곱한다.
    # sort( key=기준 [, reverse=True내림차순])
    numbers.sort( key=lambda x: (x*4)[:4], reverse=True)
    
    # 정렬했을 때 가장 앞이 0이라면, 0보다 큰 수를 인자로 받지 않았다는 뜻이므로.
    if numbers[0] == '0':
        return '0'
    else:
        answer = ''.join(numbers)
    return answer


def solution_mine(numbers):
    nums=list(map(lambda a: str(a), numbers))
    print(nums)

    # 2시간 고민 끝에 *3으로 해결하는 힌트를 확인함.
    comp_n = [num*3 for num in nums]
    
    print(comp_n)
    
    dic = {}
    for i in range(len(nums)):
        dic[comp_n[i]] = nums[i]
        
    k = list(dic.keys())
    k.sort()
    print(k)
    ans=[]
    for i in range(len(k)):
        ans.append(dic.get(k[i]))
    print(ans)
    
    res = ""
    for i in range(len(ans)):
        res += ans.pop()
    return res

