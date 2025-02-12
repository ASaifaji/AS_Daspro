# UTBK EZ

def syaratlolos(a,b,c,d):
    if 0<=a<=100 and 0<=b<=100 and 0<=c<=100 and 0<=d<=100:
        if ((a+b+c+d)/4 > 75) and (a>85) and (b>=70) and (c==95) and (d==100):
            return "lolos"
        else:
            return "tidak lolos"
    else:
        return "input salah"

mtk = int(input())
tps = int(input())
bing = int(input())
bind = int(input())

print(syaratlolos(mtk,tps,bing,bind))