import heapq

def solution(scoville, K):
    n = 0

    # scoville list를 heap으로.
    heapq.heapify(scoville)
    # 기본 min-heap 
    while scoville[0] < K:
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)
        n += 1
        # 모두 섞고 1개만 남았는데 그 수가 K보다 작은 경우는 더이상 불가능
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return n
    
# 데크를 사용하여 구현하려다가 막힘
# from collections import deque

# def solution(scoville, K):
#     if K == 0:
#         return 0
#     if 0 in scoville:
#         return -1
    
#     n = 0
#     deq = deque()
#     scoville.sort()
#     deq.extend(scoville)

#     while deq[0] < K and len(deq) > 1:
#         one = deq[0]
#         two = deq[1]
#         if one < K:
#             n+=1
#             new = one + (two*2)
#             deq.popleft()
#             deq.popleft()
#             print(one, two, new)
#             for i in range(len(deq)):
#                 if deq[i] > new:
#                     deq.insert(i, new)
#                     break
#         else:
#             break
                    
#     return n