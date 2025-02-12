# Soal 2

def IsEmpty(S):
    return S == []	    
		    
def FirstElement(S):
    if (not IsEmpty(S)):
        return S[0]

def IsOneElmt(S):
    return not IsEmpty(S) and (IsEmpty(Head(S)))

def Head(S):
    return S[:-1]

def Tail(S):
    return S[1:]

def KaliList(A, B):
    if IsOneElmt(A) or IsOneElmt(B):
        return [FirstElement(A) * FirstElement(B)]
    else:
        return [FirstElement(A) * FirstElement(B)] + KaliList(Tail(A), Tail(B))

print(KaliList([2, 4, 6], [1, 2, 3]) )
print(KaliList([1, 2, 3, 4], [1, 2, 3, 4]) )