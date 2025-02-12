# Nomor 1

def IsEmpty(S):
    return S == []	    
		    
def FirstElement(S):
    if (not IsEmpty(S)):
        return S[0]
        
def Konso(S,L):
    if IsEmpty(S):
        return [L]
    else :
        return [L]+S

def IsOneElmt(S):
    return not IsEmpty(S) and (IsEmpty(Head(S)))

def Head(S):
    return S[:-1]

def Tail(S):
    return S[1:]

def max(a,b):
    if a>=b:
        return a
    else:
        return b

def HapusNilai(Li, X):
    if IsEmpty(Li)==True:
        return Li
    else:
        if FirstElement(Li)==X:
            return HapusNilai(Tail(Li), X)
        else:
            return Konso(HapusNilai(Tail(Li), X), FirstElement(Li))

def maxlist(Li):
    if IsOneElmt(Li):
        return FirstElement(Li)
    else:
        max(FirstElement(Li),maxlist(Tail(Li)))

def MaxList2(Li):
    return maxlist(HapusNilai(Li, maxlist(Li)))

print(MaxList2([2, 6, 10, 99, 100, 20]) )
print(MaxList2([70, 67, 13, 98, 10, 20]) )