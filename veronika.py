k=0
for a in "дионсй":
    for b in "дионсй":
        for c in "дионсй":
            for d in "дионсй":
                for e in "дионсй":
                    for f in "дионсй":
                        s=a+b+c+d+e+f
                        if (not (s.count("д")>=1 and s.count("н")>=1)) and (s.count("д")>=1 or s.count("н")>=1) and (a!=b) and (b!=c) and (c!=d) and (d!=e) and (e!=f):
                            k=k+1
print(k)
