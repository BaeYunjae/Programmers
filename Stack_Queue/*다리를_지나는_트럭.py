from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)                  # 리스트보다 덱이 빠름
    truck_weights = deque(truck_weights)
    sum_weight = 0
    
    while bridge: 
        arrive = bridge.popleft()                        # 시작은 0 이지만, 이후를 위해 편의상 arrive로 정의
        if arrive > 0:                                   # 다리 끝에 도착하면 bridge 덱에서 빼주면서 
            sum_weight -= arrive                         # 다리 위 무게 합에서도 빼준다
        answer += 1
        
        if truck_weights:                                 
            if sum_weight + truck_weights[0] <= weight:  # 다리 위 무게 합 + 첫번째 대기 트럭 <= 최대 무게
                land = truck_weights.popleft()           # 첫번째 대기 트럭을 
                bridge.append(land)                      # 다리 위에 올리고
                sum_weight += land                       # 다리 위 무게 합에 더한다
            else:                                                     
                bridge.append(0)                         # 최대 무게보다 크면 뒤에 0 추가
        
    return answer

-----------------------------------------------------------------------------------
# 테스트케이스 5번 시간초과
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    
    while bridge:
        bridge.pop(0)                                     # 다리 맨 앞의 자리 빼기
        answer += 1
        
        if truck_weights:                                 # 대기 트럭이 있을 때 
            if sum(bridge) + truck_weights[0] <= weight:  # 다리 위 무게 + 첫번째 대기 트럭 무게 <= 최대 무게
                bridge.append(truck_weights.pop(0))       # 다리에 첫번째 대기 트럭 추가
            else:                                         # 최대 무게보다 크면                 
                bridge.append(0)                          # 다리에 0 추가
        
    return answer
