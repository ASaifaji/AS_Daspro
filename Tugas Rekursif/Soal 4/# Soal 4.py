# Soal 4

def CountDigit(n):
    if n < 10:
        return 1
    else:
        return 1 + CountDigit(n // 10)

print(CountDigit(0))
print(CountDigit(1234))
print(CountDigit(222))