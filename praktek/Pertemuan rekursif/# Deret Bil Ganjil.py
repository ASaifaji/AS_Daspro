# Deret Bil Ganjil

def gnjl(n):
    if n==1:
        return 1
    else:
        return ((2*n)-1) + gnjl(n-1)

print(gnjl(int(input())))