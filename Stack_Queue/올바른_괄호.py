# 첫번째 풀이 (정확성: 69.5, 효율성: 30.5)
def solution(s):
    s = list(s)
    cnt = 0
    
    while s:
        if s[-1] == ')':
            cnt += 1
            s.pop()
        elif s[-1] == '(':
            if cnt == 0:
                return False
            else:
                cnt -= 1
                s.pop()
    
    if cnt:
        return False
    else:
        return True

----------------------------------------
# 두번째 풀이
def solution(s):
    pair = 0
    
    for x in s:
        if x == '(':
            pair += 1
        elif x == ')':
            pair -= 1
        if pair < 0:
            return False
        
    return pair == 0
        
    
            
                
        
        
    
    
