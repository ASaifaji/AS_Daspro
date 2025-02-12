# Permen Manis

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

def jum_transaksi(budi,anto):
    if IsEmpty(budi) or IsEmpty(anto):
        return 0
    else:
        if FirstElement(budi)<FirstElement(anto):
            return 1 + jum_transaksi(Tail(budi),Tail(anto))
        else:
            return 0 + jum_transaksi(Tail(budi),Tail(anto))


X = int(input())
input1 = [int(x) for x in input().split()]
input2 = [int(x) for x in input().split()]

print(jum_transaksi(input1,input2))