# Soal 1
# Pecahan Campuran

# tipe bentukan
def pecahan(a,b,c):
    return(a,b,c)

# Selektor Pecahan Campuran
def bil(P):
    return P[0]

def pem(P):
    return P[1]

def pen(P):
    return P[2]

#Selektor Pecahan Biasa
def pemb(P):
    return P[0]

def peny(P):
    return P[1]

# Operator
def konversipecahan(P):
    if P[0]>=0:
        return [(P[0]*P[2])+P[1],P[2]]
    else:
        return [(P[0]*P[2])-P[1],P[2]]

def konversireal(P):
    if P[0]>=0:
        return round(((P[0]*P[2])+P[1])/P[2],3)
    else:
        return round(((P[0]*P[2])-P[1])/P[2],3)

def konversicampuran(P):
    if P[0]>=0:
        return [P[0]//P[1],P[0]%P[1],P[1]]
    else:
        return [(-(P[0]//P[1])),P[0]%P[1],P[1]]

def addp(P1,P2):
    return (pemb(konversipecahan(P1))*peny(konversipecahan(P2))+pemb(konversipecahan(P2))*peny(konversipecahan(P1)),
                            peny(konversipecahan(P1))*peny(konversipecahan(P2)))

def subp(P1,P2):
    return (pemb(konversipecahan(P1))*peny(konversipecahan(P2))-pemb(konversipecahan(P2))*peny(konversipecahan(P1)),
                            peny(konversipecahan(P1))*peny(konversipecahan(P2)))

def mulp(P1,P2):
    return (pemb(konversipecahan(P1))*pemb(konversipecahan(P2)),peny(konversipecahan(P1))*peny(konversipecahan(P2)))

def divp(P1,P2):
    return (pemb(konversipecahan(P1))*peny(konversipecahan(P2)),peny(konversipecahan(P1))*pemb(konversipecahan(P2)))

#Predikat
def IsEqP(P1,P2):
    if konversireal(P1)==konversireal(P2):
        return True
    else:
        return False

def IsLtP(P1,P2):
    if konversireal(P1)<=konversireal(P2):
        return True
    else:
        return False

def IsGtP(P1,P2):
    if konversireal(P1)>=konversireal(P2):
        return True
    else:
        return False

# Aplikasi

P1=(5,2,1)
P2=(-2,1,9)
P3=(5,4,5)
P4=(-4,2,7)

print(konversipecahan(P1))
print(konversireal(P2))
print(konversicampuran(addp(P1,P3)))
print(konversicampuran(subp(P1,P3)))
print(konversicampuran(mulp(P3,P4)))
print(konversicampuran(divp(P1,P2)))
print(IsEqP(P2,P4))
print(IsLtP(P2,P3))
print(IsGtP(P3,P4))
