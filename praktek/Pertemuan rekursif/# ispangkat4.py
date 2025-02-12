# ispangkat4

def IsPangkat4(n):
    if n==1:
        return True
    elif n==4:
        return True
    elif n>=4:
        return IsPangkat4(n/4)
    else:
        return False

print(IsPangkat4(int(input())))