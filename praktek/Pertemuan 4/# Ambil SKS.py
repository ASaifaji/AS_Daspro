# Ambil SKS

def ambil_sks(a):
    if 0<=a<2.0:
        return "18 SKS"
    elif 2.0<=a<=2.49:
        return "20 SKS"
    elif 2.5<=a<=2.99:
        return "22 SKS"
    elif a>3.0:
        return "24 SKS"

IPK = float(input())
x = ambil_sks(IPK)
print(x)