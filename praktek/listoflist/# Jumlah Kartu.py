# Jumlah Kartu

def IsEmpty(S):
    return bool(S == [])	    
		    
def FirstElement(S):
    if (not IsEmpty(S)):
        return S[0]
  
def Head(S):
    return S[:-1]

def Tail(S):
    return S[1:]

def flatten(S):
    if IsEmpty(S)==True:
        return[]
    elif type(FirstElement(S))==list:
        return FirstElement(S) + flatten(Tail(S))
    else:
        return [FirstElement(S)] + flatten(Tail(S))

def jumlahkartu(S):
    X=flatten(S)
    if X==[]:
        return 0
    else:
        return 1 + jumlahkartu(Tail(X))

print(jumlahkartu([1,[2,3],[4,[5,6,7]]]))