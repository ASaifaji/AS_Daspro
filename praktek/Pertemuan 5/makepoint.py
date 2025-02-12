#KOORDINAT

def make_point(a,b):
    return [a,b]

def absis(p):
    return p[0]

def ordinat(p):
    return p[1]

P1 = make_point(3,6)
print(absis(P1))
print(ordinat(P1))


#PECAHAN

def make_sub(a,b):
    return [a,b]
def pembilang(s):
    return s[0]
def penyebut(s):
    return s[1]
def pecahan(s):
    return f"{s[0]}/{s[1]}"
def addp (s1,s2):
    return make_sub(pembilang(s1)*penyebut(s2)+pembilang(s2)*penyebut(s1),penyebut(s1)*penyebut(s2))
def subp (s1,s2):
    return make_sub(pembilang(s1)*penyebut(s2)-pembilang(s2)*penyebut(s1),penyebut(s1)*penyebut(s2))
def mulp (s1,s2):
    return make_sub(pembilang(s1)*pembilang(s2),penyebut(s1)*penyebut(s2))
def divp (s1,s2):
    return make_sub(pembilang(s1)*penyebut(s2),penyebut(s1)*penyebut(s2))
def realp (s):
    return s[0]/s[1]
def iseqp (s1,s2):
    return bool(realp(s1)==realp(s2))
def isltp (s1,s2):
    return bool(realp(s1)<=realp(s2))
def isgtp (s1,s2):
    return bool(realp(s1)>=realp(s2))

S1 = make_sub(2,3)
S2 = make_sub(2,6)

print(S1)
print(pembilang(S1))
print(penyebut(S1))
print(pecahan(S1))
print(addp(S1,S2))
print(subp(S1,S2))
print(mulp(S1,S2))
print(divp(S1,S2))
print(realp(S1))
print(iseqp(S1,S2))
print(isltp(S1,S2))
print(isgtp(S1,S2))