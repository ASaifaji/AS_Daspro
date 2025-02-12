# Soal 8

def IsEmpty(S):
    return bool(S == [])

def IsOneElmt(S):
    return not IsEmpty(S) and (IsEmpty(Head(S)))
		    
def FirstElement(S):
    if (not IsEmpty(S)):
        return S[0]
  
def Head(S):
    return S[:-1]

def Tail(S):
    return S[1:]

def sum(S):
    if IsEmpty(S)==True:
        return 0
    else:
        return FirstElement(S) + sum(Tail(S))

def MakeListAtom(S):
    if IsEmpty(S)==True:
        return []
    elif type(FirstElement(S))==list:
        return [sum(FirstElement(S))] + MakeListAtom(Tail(S))
    else:
        return [FirstElement(S)] + MakeListAtom(Tail(S))

print(MakeListAtom([3, [2, 4, 5], [1, 3], [6, 4, 1, 2], 7, [2]]))