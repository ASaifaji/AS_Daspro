# Soal 1

def biner(n):
    if n>=1:
        return biner(n//2)+str(n%2)
    else:
        return str(n)

print(biner(10))
print(biner(8))