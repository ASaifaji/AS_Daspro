# Soal 7

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
    S=flatten(S)
    if IsEmpty(S):
        return 0
    else:
        if FirstElement(S)%2==0:
            return 0 + NBOdds(Tail(S))
        else:
            return 1 + NBOdds(Tail(S))

print(NBOdds([3, [2, 4, 5], [6, 3], [6, 4, 1, 2], 7, [2]]))
print(NBOdds([3, [2, 4, 5], [6, 3], [6, 4, 1, 2], 7, [21]]))