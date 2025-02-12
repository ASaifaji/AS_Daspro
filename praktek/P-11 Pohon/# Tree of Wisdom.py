       # Tree of Wisdom

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

def ismember(p,x):
    if x==Akar(p):
        return True
    elif IsTreeEmpty(p) or IsOneElement(p):
        return False
    else:
        if x>=Akar(p):
            return ismember(Right(p),x)
        else:
            return ismember(Left(p),x)

def findX(p,x):
    if Akar(p)==x:
        return 1
    elif not ismember(p,x):
        return -1
    elif x>= Akar(p):
        return findX(Right(p),x)+1
    elif x<Akar(p):
        return findX(Left(p),x)+1