# penjumlahan prima

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

def isprima(n, i=2):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % i == 0:
        return False
    elif i * i > n:
        return True
    else:
        return isprima(n, i + 1)

def NBPrime(S):
    X=flatten(S)
    if IsEmpty(X):
        return 0
    else:
        if isprima(FirstElement(X)):
            return int(FirstElement(X)) + NBPrime(Tail(X))
        else:
            return 0 + NBPrime(Tail(X))

print(NBPrime([1,[5,2,3],10,9,[7],[3,3]]))