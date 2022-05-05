
class Node:
    def __init__(self,d,p=None,n=None):
        self.d = d
        self.p = p
        self.n = n
    

def solution(n, k, cmd):
    rows = []
    for i in range(n):
        rows.append(Node(i))
        if i != 0:
            rows[i].p = rows[i-1]
            rows[i-1].n = rows[i]
    answer = ['O']*n
    stack = []
    k = rows[k]
            
    for c in cmd:
        cs = c.split()
        
        if cs[0] == 'U':
            X = int(cs[1])
            
            for i in range(X):
                k = k.p
                
        elif cs[0] == 'D':
            X = int(cs[1])
            
            for i in range(X):
                k = k.n
            
        elif cs[0] == 'C':
            stack.append(k.d)
            
            prev_n = k.p
            next_n = k.n
            answer[k.d] = 'X'
            if k.n is None: k=k.p
            else: k=k.n
            
            if prev_n is not None:
                prev_n.n = next_n
            if next_n is not None:
                next_n.p = prev_n
            
        elif cs[0] == 'Z':
            X = stack.pop()
            z = rows[X]
            answer[X] = 'O'
            
            prev_z = z.p
            next_z = z.n
            
            if prev_z is not None:
                prev_z.n = z
            if next_z is not None:
                next_z.p = z
            
    
    return "".join(answer)

print("OOOOXOOO"==solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))