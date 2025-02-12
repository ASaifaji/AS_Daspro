# Soal 3

def IsEmpty(S):
    return S == []

def FirstElement(S):
    if (not IsEmpty(S)):
        return S[0]

def Tail(S):
    return S[1:]

def NBElmtX(x,y):
    if IsEmpty(list(y)):
        return 0
    else:
        if x==FirstElement(list(y)):
            return 1 + NBElmtX(x,Tail(list(y)))
        else:
            return 0 + NBElmtX(x,Tail(list(y)))

print(NBElmtX("a", "alamat"))
print(NBElmtX("o", "ilmu komputer dan informatika"))