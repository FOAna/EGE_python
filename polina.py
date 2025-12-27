kol=0
for pos1 in 'дионсй':
    for pos2 in 'дионсй':
        for pos3 in 'дионсй':
            for pos4 in 'дионсй':
                for pos5 in 'дионсй':
                    for pos6 in 'дионсй':
                        s=pos1+pos2+pos3+pos4+pos5+pos6
                        if (not ('д' in s and 'н' in s)) and (not ('д' not in s and 'н' not in s)) and ('дд' not in s) and ('ии' not in s) and ('оо' not in s) and ('нн' not in s) and ('сс' not in s) and ('йй' not in s):
                            kol=kol+1
print(kol)

