# FPB 2

def FPB(x,y):
    if y==0:
        return x
    else:
        return FPB(y,x%y)

x=int(input())
y=int(input())

print((FPB(x,y)))