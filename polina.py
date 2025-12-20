kol=0
# for pos1 in 'ш':
for pos2 in 'вишня':
    for pos3 in 'вишня':
        for pos4 in 'вшн':
            s='ш'+pos2+pos3+pos4
            # if s.count('в')>=1 and s.count('и')>=1:
            if 'в' in s and 'и' in s:
                kol=kol+1
print(kol)
