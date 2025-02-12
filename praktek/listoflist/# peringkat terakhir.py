# peringkat terakhir

def isoneelemt(S):
    return not(S==[]) and (head(S)==[])

def lastelmt(S):
    return S[-1]

def firstelmt(S):
    if (not S==[]):
        return S[0]

def head(S):
    return S[:-1]

def tail(S):
    return S[1:]

def nama(N):
    return N[0]

def nilai(N):
    return N[1]

def konso(S,L):
    if S==[]:
        return [L]
    else :
        return [L]+S

def HapusNilai(S, X):
    if S==[]:
        return S
    else:
        if firstelmt(S)==X:
            return HapusNilai(tail(S), X)
        else:
            return konso(HapusNilai(tail(S), X), firstelmt(S))

def namafungsi(S):
    if isoneelemt(S):
        return nama(lastelmt(S))
    else:
        if nilai(lastelmt(S)) >= nilai(lastelmt(head(S))):
            return (namafungsi(head(S)))
        elif nilai(lastelmt(S)) <= nilai(lastelmt(head(S))):
            return (namafungsi(HapusNilai(S,lastelmt(head(S)))))
        elif nilai(lastelmt(S)) == nilai(lastelmt(head(S))):
            return (namafungsi(head(S)))

# APLIKASI
import ast
LoL = ast.literal_eval(input())

print(namafungsi(LoL))

