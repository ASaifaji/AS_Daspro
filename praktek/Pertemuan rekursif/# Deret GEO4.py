# Deret GEO4

def geo4(n):
    if n==1:
        return 1
    else:
        return 4**(n-1) + geo4(n-1)

print(geo4(int(input())))