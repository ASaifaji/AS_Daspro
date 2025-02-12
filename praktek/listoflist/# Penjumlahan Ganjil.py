# Penjumlahan Ganjil

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

def NBOdds(S):
    X=flatten(S)
    if IsEmpty(X):
        return 0
    else:
        if FirstElement(X)%2==0:
            return 0 + NBOdds(Tail(X))
        else:
            return int(FirstElement(X)) + NBOdds(Tail(X))

print(NBOdds([1,[5,2,3],10,9,[7],[3,3]]))