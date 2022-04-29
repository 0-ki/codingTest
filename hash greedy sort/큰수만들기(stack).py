def solution(number, k):
    collected = [] # Stack
    
    for i, num in enumerate(number):
        # 비어있으면 통과 후 넣기 / 가장 마지막 들어있는 것과 지금 넣는것 비교 / k번 만큼만 가능
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k-=1
        # k가 모두 소진되었으면, 중단하고 남은 수를 전부 넣고 끝내서 효율성
        if k == 0:
            collected += list(number[i:])
            break
        # 결국 더 작은 수를 빼내고 지금 것을 넣는다
        collected.append(num)
    # 999 인 경우처럼 작지 않아서 빼지 않은 경우 뒤에서부터 자르면 됨
    collected = collected[:-k] if k > 0 else collected
    return ''.join(collected)


def solution_mine(num, k):
    ans = [] # Stack
    
    for i in num:
        # 비어있으면,
        if not ans:
            ans.append(i)
            continue
        if k > 0:
            # 들어올 수보다 더 작은 수들은 빼낸다
            while ans[-1] < i:
                ans.pop()
                k-=1
                # ans가 비었거나, k가 모두 소모되면 끝낸다
                if not ans or k == 0:
                    break
        # ans가 비었거나, 더 큰수가 오면 담는다 
        ans.append(i)
    # "999" k=2 인 경우, k를 소모하지 않고 9 9 9 담기니까, ans[:-2]만큼.
    # [True] if 조건문 else [False]
    ans = ans[:-k] if k>0 else ans
    return ''.join(ans)

num1 = '157532998234'
print(solution(num1, 2))