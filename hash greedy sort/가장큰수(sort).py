def solution_mine(numbers):
    # 문자열로 만들어서 담는다.
    numbers = [str(x) for x in numbers]
    # 1 > 2 > 12 순으로 정렬될 것임. ASCII 사전순으로.
    # 문자열의 최대 자릿수가 4 이하이므로, *4를 한 값을 기준으로 비교하며 내림차순 정렬.
    # lambda 식으로 key가 되는 비교 로직을 작성한다. 4를 곱한 후 4자리까지만 자른 것을 key 기준으로 잡았다.
    numbers.sort(key=lambda x: (x*4)[:4] , reverse=True)
    
    # 가장 앞이 0일 때는 0만 들어있는 배열이 인자로 들어온 것이므로.. [0,0,0,0]
    print(numbers[0])
    if numbers[0] == '0':
        return '0'
    else:
        return ''.join(numbers)

