# Soal 5

def makepoint(x,y):
    return[x,y]

def absis(P):
    return P[0]

def oordinat(P):
    return P[1]

def IsEmpty(S):
    return S == []	    
		    
def FirstElement(S):
    if (not IsEmpty(S)):
        return S[0]

def LastElement(S):
    if not (IsEmpty(S)):
        return S[-1]
    
def JumlahElement(S):
    if IsEmpty(S):
        return 0
    else :
        return 1 + JumlahElement(Tail(S))
        
def Konso(S,L):
    if IsEmpty(S):
        return [L]
    else :
        return [L]+S

def Konsi(L,S):
    if IsEmpty(S):
        return [L]
    else:
        return S+[L]

def IsOneElmt(S):
    return not IsEmpty(S) and (IsEmpty(Head(S)))
  
def Head(S):
    return S[:-1]

def Tail(S):
    return S[1:]

def HapusNilai(S, X):
    if IsEmpty(S)==True:
        return S
    else:
        if FirstElement(S)==X:
            return HapusNilai(Tail(S), X)
        else:
            return Konso(HapusNilai(Tail(S), X), FirstElement(S))

def jarak(A,B):
    return (((absis(B)-absis(A))**2)+((oordinat(B)-oordinat(A))**2))**0.5

def NearestPoint(A,B):
    if IsOneElmt(B):
        return B
    else:
        if jarak(A,FirstElement(B))<=jarak(A,FirstElement(Tail(B))):
            return NearestPoint(A, HapusNilai(B,FirstElement(Tail(B))))
        else:
            return NearestPoint(A, HapusNilai(B,FirstElement(B)))


print( NearestPoint([1,2], [[0,0], [3,4], [6,7], [1,1], [2,1]]) )