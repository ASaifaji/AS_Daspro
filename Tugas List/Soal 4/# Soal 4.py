# Soal 4

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

def Body(S):
    return S[1:-1]

def HapusNilai(S, X):
    if IsEmpty(S)==True:
        return S
    else:
        if FirstElement(S)==X:
            return HapusNilai(Tail(S), X)
        else:
            return Konso(HapusNilai(Tail(S), X), FirstElement(S))

def CekPalindrom(S):
    if JumlahElement(list(S))<=1:
        return True
    else:
        return bool(FirstElement(list(S))==LastElement(list(S)) and CekPalindrom(Body(list(S))))

print(CekPalindrom("kodok") )
print(CekPalindrom("daspro") )