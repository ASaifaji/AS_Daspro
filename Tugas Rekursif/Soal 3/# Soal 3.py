# Soal 3

def FPB(x,y):
    if y==0:
        return x
    else:
        return FPB(y,x%y)

print(FPB(60,10))
print(FPB(11,1))