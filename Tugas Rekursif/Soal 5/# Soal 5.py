# Soal 5

# Konstruktor
def date(d,m,y):
    return [d,m,y]

# Selektor
def d(D):
    return D[0]
def m(D):
    return D[1]
def y(D):
    return D[2]

# predikat
def iskabisat(D):
    if (y(D)%4)==0:
        return True
    else:
        return False

# Operasi

def NextNDay(D,n):
    if iskabisat(D)==True:
        if m(D)==1:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==2:
            if (d(D)+n)>29:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-29)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==3:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==4:
            if (d(D)+n)>30:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-30)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==5:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==6:
            if (d(D)+n)>30:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-30)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==7:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==8:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==9:
            if (d(D)+n)>30:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-30)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==10:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==11:
            if (d(D)+n)>30:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-30)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==12:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        

    else:
        if m(D)==1:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==2:
            if (d(D)+n)>28:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-28)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==3:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==4:
            if (d(D)+n)>30:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-30)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==5:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==6:
            if (d(D)+n)>30:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-30)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==7:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==8:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==9:
            if (d(D)+n)>30:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-30)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==10:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==11:
            if (d(D)+n)>30:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-30)
            else:
                return date(d(D)+n,m(D),y(D))
        elif m(D)==12:
            if (d(D)+n)>31:
                return NextNDay(date(0,m(D)+1,y(D)),d(D)+n-31)
            else:
                return date(d(D)+n,m(D),y(D))

print(NextNDay(date(2,11,2023),4))
print(NextNDay(date(17,8,2023),15))
print(NextNDay(date(11,6,2023),25))