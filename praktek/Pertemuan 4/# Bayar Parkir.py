# Bayar Parkir

def parkir(j):
    if j==1:
        return 5000
    elif j>1:
        if j<=4:
            return 5000 + ((j-1)*4000)
        else:
            return 17000 + ((j-4)*3000)
    else:
        return 0

jam = int(input())
print(parkir(jam))