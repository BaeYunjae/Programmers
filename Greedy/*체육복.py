def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:                                 # lost = [2, 4], reserve = [3] 이면 3이 하나(2)만 없애고 반복문이 종료됨
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

'''
n	 lost	   reserve	return
5	[2, 4]	[1, 3, 5]	  5
5	[2, 4]	[3]	        4
3	[3]	    [1]	        2
'''
