cnt = 0
for pos1 in 'виня':
    for pos2 in 'вишня':
        for pos3 in 'вишня':
            for pos4 in 'вишня':
                for pos5 in 'вишня':
                    for pos6 in 'вшн':
                        s = pos1 + pos2 + pos3 + pos4 + pos5 + pos6
                        if s.count('в') <= 1:
                            cnt += 1
print(cnt)
