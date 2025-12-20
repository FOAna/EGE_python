k=0
for a in "виня":
    for b in "вишня":
        for c in "вишня":
            for d in "вшн":
                s=a+b+c+d
                if s.count("в") >= 1:
                    k = k+1
print(k)

