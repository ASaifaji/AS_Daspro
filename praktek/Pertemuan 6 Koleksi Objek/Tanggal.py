# Konstruktor
def make_date(d,m,y):
    return [d,m,y]


# Selektor
def day(D):
    return D[0]

def month(D):
    return D[1]

def year(D):
    return D[2]

# predikat
def iskabisat(D):
    if (D[2]%4)==0:
        return True
    else:
        return False

# Operasi
def jum_hr(D):
    if iskabisat(D)==True:
        if D[1]==1:
            return (0)+D[0]
        if D[1]==2:
            return (31)+D[0]
        if D[1]==3:
            return (31+29)+D[0]
        if D[1]==4:
            return (31+29+31)+D[0]
        if D[1]==5:
            return (31+29+31+30)+D[0]
        if D[1]==6:
            return (31+29+31+30+31)+D[0]
        if D[1]==7:
            return (31+29+31+30+31+30)+D[0]
        if D[1]==8:
            return (31+29+31+30+31+30+31)+D[0]
        if D[1]==9:
            return (31+29+31+30+31+30+31+31)+D[0]
        if D[1]==10:
            return (31+29+31+30+31+30+31+31+30)+D[0]
        if D[1]==11:
            return (31+29+31+30+31+30+31+31+30+31)+D[0]
        if D[1]==12:
            return (31+29+31+30+31+30+31+31+30+31+30)+D[0]
    else:
        if D[1]==1:
            return (0)+D[0]
        if D[1]==2:
            return (31)+D[0]
        if D[1]==3:
            return (31+28)+D[0]
        if D[1]==4:
            return (31+28+31)+D[0]
        if D[1]==5:
            return (31+28+31+30)+D[0]
        if D[1]==6:
            return (31+28+31+30+31)+D[0]
        if D[1]==7:
            return (31+28+31+30+31+30)+D[0]
        if D[1]==8:
            return (31+28+31+30+31+30+31)+D[0]
        if D[1]==9:
            return (31+28+31+30+31+30+31+31)+D[0]
        if D[1]==10:
            return (31+28+31+30+31+30+31+31+30)+D[0]
        if D[1]==11:
            return (31+28+31+30+31+30+31+31+30+31)+D[0]
        if D[1]==12:
            return (31+28+31+30+31+30+31+31+30+31+30)+D[0]

print(jum_hr(make_date(6,10,19)))

