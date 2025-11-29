bilet=0

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        summa1 = a+b+c
                        summa2 = d+e+f
                        if summa1==summa2 and a == 9:
                            bilet=bilet+1
                            if bilet <= 5:
                                print(a, b, c, d, e, f)
                        if bilet >= 5:
                            break
                    if bilet >= 5:
                        break
                if bilet >= 5:
                    break
            if bilet >= 5:
                break
        if bilet >= 5:
            break
    if bilet >= 5:
        break

