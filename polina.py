kol=0
for pervi in '1234':
    for vtoroi in '1234':
        for treti in '1234':
            # if not(pervi==vtoroi==2 or pervi==treti==2 or vtoroi==treti==2 or):
            shifr = pervi + vtoroi + treti
            if shifr.count('2') == 1:
                kol=kol+1
                kol=kol+1
print(kol)

