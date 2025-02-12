# deret

def deret3(x,y):
    if x==y:
        return x
    else:
        return x + deret3(x+2,y)

print(deret3(1,7))


# 9
# 1+3+9+27
def deret(x,y):
    if x==y:
        return x
    else:
        return x+deret(x*3,y)

print(deret(1,27))


# 10
# 1+4+9+16+...
def deret(x,y,z):
    if x==y:
        return x
    else:
        return x + deret(x+z,y,z+2)

print(deret(1,16,3))