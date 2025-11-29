k=0
for a1 in sorted("БАТЫР"):
    for a2 in sorted("БАТЫР"):
        for a3 in sorted("БАТЫР"):
            for a4 in sorted("БАТЫР"):
                for a5 in sorted("БАТЫР"):
                    s=a1+a2+a3+a4+a5
                    k+=1
                    if "Ы" not in s and "АА" not in s:
                        print(k)
                        exit()