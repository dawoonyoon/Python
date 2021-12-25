from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights) # 대기트럭(truck_weights)을 담은 deque 생성
    bridge = deque([0 for i in range(bridge_length)]) # 다리길이만큼 0을 채워서 변수 생성
    time = 0 # 경과 시간
    bridge_weight = 0 # 다리를 건너고 있는 트럭의 무게
    # bridge의 크기가 0이 될때까지 반복
    while len(bridge) != 0:
        out = bridge.popleft() # 다리를 건너는 첫번째 트럭(bridge[0])을 pop해줌
        bridge_weight -= out # 다리 무게에서 다리를 건넌 트럭의 무게를 빼줌
        time += 1 # 시간을 더해줌
        
        if truck_weights: # deque에 요소가 남아있으면 True
        
        	# 현재 다리를 건너는 트럭의 무게와 다리에 오를 트럭의 무게의 합이
            if bridge_weight + truck_weights[0] <= weight:
            	# 다리가 견딜 수 있는 무게 이하일때
                left = truck_weights.popleft() # 대기트럭 deque에서 다음 트럭을 pop하고
                bridge_weight += left # 다리를 건너고 있는 트럭 무게에 더하고
                bridge.append(left) # 건너는 트럭 리스트에 넣어준다.
            else:
            	# 다리가 견딜 수 있는 무게 초과일때
                bridge.append(0) # 다음 트럭이 못지나 가므로 0을 채워준다.
    return time
