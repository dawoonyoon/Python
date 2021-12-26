import collections 
def solution(bridge_length, weight, truck_weights):
    deq = collections.deque([0]*bridge_length)
    t = 0
    pointer = 0  # 시간초과로 인한 포인터 추가
    while pointer < len(truck_weights):
        deq.pop()
        t +=1
        deq_sum = sum(deq) # 시간초과로 인한 변수 설정
        
        if deq_sum > weight:
            deq.appendleft(0)
            # print(deq)
            continue
        else:
            if deq_sum + truck_weights[pointer] > weight:
                deq.appendleft(0)
                # print(deq)
                continue
            else:
                deq.appendleft(truck_weights[pointer])
                # del truck_weights[0]
                pointer += 1
                # print(deq)
                continue
    print(t+bridge_length)
        
        
    return t + bridge_length