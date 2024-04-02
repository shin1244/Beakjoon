from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    bridge = deque(bridge)
    truck_weights = deque(truck_weights)
    result = 0
    now_weight = 0
    while truck_weights:
        result += 1
        now_weight -= bridge.pop()
        if weight-now_weight >= truck_weights[0]:
            truck = truck_weights.popleft()
            bridge.appendleft(truck)
            now_weight+=truck
        else:
            bridge.appendleft(0)
    
    return result+bridge_length