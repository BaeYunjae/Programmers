# 첫번째 풀이
from collections import deque

def solution(priorities, location):
    que = deque()
    for l, p in enumerate(priorities):  # (인덱스, 우선순위)라서 
        que.append((l, p))              # (l, p)여야 함

    cnt = 0
    while True:
        MAX = max(que, key = lambda x: x[1])
        if que[0] == MAX:
            if que[0][0] == location:
                cnt += 1
                break
            que.popleft()
            cnt += 1
        else:
            que.rotate(-1)
            
    return cnt
  
----------------------------------------------------------------
# 더 효율적
from collections import deque

def solution(priorities, location):
    que = deque((p, l) for l, p in enumerate(priorities))
    print(que)
    
    cnt = 0
    while True:
        item = que.popleft()
        if que and max(que)[0] > item[0]:
            que.append(item)
        else:
            cnt += 1
            if item[1] == location:
                break
                
    return cnt
  
-----------------------------------------------------------------
# 두번째 풀이
def solution(priorities, location):
    que = [(l, p) for l, p in enumerate(priorities)]
    cnt = 0
    while True:
        item = que.pop(0)
        if any(item[1] < q[1] for q in que):
            que.append(item)
        else:
            cnt += 1
            if item[0] == location:
                return cnt
              
