# Soal 2

def isprima(n,i=None):
    if i == None:
        i=n-1
    if n < 2:
        False
    elif n == (2 or 3):
        True
    elif i == 1:
        return True
    elif n % i == 0:
        return False
    else:
        return isprima(n,i-1)

print(isprima(13))
print(isprima(10))