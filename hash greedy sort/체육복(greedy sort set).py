def solution(n, lost, reserve):
    # 양쪽 중복을 제거한 다음 고려한다.
    lset = set(lost)
    rset = set(reserve)
    lost = (lset-rset)
    reserve = (rset-lset)

    # 아래처럼 더 깔끔하게도 가능하겠다.
    # s = set(lost) & set(reserve)
    # l = lost - s
    # r = reserve - s

    # sorted는 list로 return한다.
    for i in sorted(reserve):
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    return n - len(lost)