kol=0
for pos1 in '246':
    for pos2 in '0123456':
        for pos3 in '0123456':
            for pos4 in '0123456':
                for pos5 in '3456':
                    s=pos1+pos2+pos3+pos4+pos5
                    if s.count('4')<=1:
                        kol=kol+1
