"""
6 Şubat 2018, Salı, Ankara, Türkiye
Sayısal Loto; klasikleşmiş bir "ROM Hello World" uygulaması ;)
www.madran.net
"""
from random import randint
i = 0
secilenler = [0,0,0,0,0,0]
for rastgele in secilenler:
    while i < len(secilenler):
        secilen = randint(1, 49)
        if secilen not in secilenler:
            secilenler[i] = secilen
            i+=1
    print(sorted(secilenler))
    i=0
