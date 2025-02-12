# Hapus Nilai

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
  
def HapusNilai(user_input, X):
    if IsEmpty(user_input)==True:
        return user_input
    else:
        if FirstElement(user_input)==X:
            return HapusNilai(Tail(user_input), X)
        else:
            return Konso(HapusNilai(Tail(user_input), X), FirstElement(user_input))
    
  
  
user_input = [int(x) for x in input().split()]
X = int(input())

print(HapusNilai(user_input, X))