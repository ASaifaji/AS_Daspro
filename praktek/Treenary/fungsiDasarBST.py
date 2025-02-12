def MakePB(A, L, R):
    return [A, L, R]

def Akar(P):
    return P[0]

def Left(P):
    return P[1]

def Right(P):
    return P[2]

def IsEmpty(S):
    return bool(S == [])

def FirstElement(S):
    if (not IsEmpty(S)):
        return S[0]

def IsTreeEmpty(P):
    if P == []:
        return True
    else:
        return False
    
def IsOneElement(P):
    if not (IsTreeEmpty(P)) and IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
        return True
    else:
        return False

def IsUnerLeft(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
        return True
    else: 
        return False

def IsUnerRight(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P)):
        return True
    else:
        return False
    
def IsBiner(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P)):
        return True
    else:
        return False

def NBElement(P):
    if IsOneElement(P):
        return 1
    else:
        if (IsBiner(P)):
            return NBElement(Left(P)) + 1 + NBElement(Right(P))
        elif (IsUnerLeft(P)):
            return NBElement(Left(P)) + 1
        elif (IsUnerRight(P)):
            return 1 + NBElement(Right(P))
        
def NBDaun(P):
    if IsOneElement(P):
        return 1
    else:
        if (IsBiner(P)):
            return NBDaun(Left(P)) + NBDaun(Right(P))
        elif (IsUnerLeft(P)):
            return NBDaun(Left(P))
        elif (IsUnerRight(P)):
            return NBDaun(Right(P))

def Tail(S):
    return S[1:]

def flatten(S):
    if IsEmpty(S)==True:
        return[]
    elif type(FirstElement(S))==list:
        return flatten(FirstElement(S)) + flatten(Tail(S))
    else:
        return [FirstElement(S)] + flatten(Tail(S))

def taruhpalingkanan(P1,P2):
    if IsEmpty(Right(P1)):
        return [Akar(P1),Left(P1),P2]
    else:
        return [Akar(P1),Left(P1),taruhpalingkanan(Right(P1),P2)]

def Camouflage(P,X):
    if [X]<=Left(P):
        return [X,[],taruhpalingkanan(Left(P),Right(P))]
    elif [X]>=Left(P):
        return [X,taruhpalingkanan(Left(P),Right(P)),[]]


print(Camouflage(MakePB(17, MakePB(13, MakePB(6, [], []), MakePB(15, [], [])), MakePB(21, MakePB(19, [], []), MakePB(24, [], []))),1))