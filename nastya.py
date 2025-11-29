from itertools import*
count = 0
x = permutations('0123456789', r = 6)
# чо касаемо permutations)))
for i in x:
    r = ''.join(i)
    if r[0] != '0' and int(r) % 5 == 0 :
        r = r.replace('1', '*')
        r = r.replace('3', '*')
        r = r.replace('5', '*')
        r = r.replace('7', '*')
        r = r.replace('9', '*')
        r = r.replace('2', '!')
        r = r.replace('4', '!')
        r = r.replace('0', '!')
        r = r.replace('6', '!')
        r = r.replace('8', '!')
        if '**' not in r and '!!' not in r:
            count += 1
print(count)

count_1 = 0
for a1 in '123456789':
    for a2 in '0123456789':
        for a3 in '0123456789':
            for a4 in '0123456789':
                for a5 in '0123456789':
                    for a6 in '05':
                        r = a1 + a2 + a3 + a4 + a5 + a6
                        if len(set(r)) == 6:
                            r = r.replace('1', '*')
                            r = r.replace('3', '*')
                            r = r.replace('5', '*')
                            r = r.replace('7', '*')
                            r = r.replace('9', '*')
                            r = r.replace('2', '!')
                            r = r.replace('4', '!')
                            r = r.replace('0', '!')
                            r = r.replace('6', '!')
                            r = r.replace('8', '!')
                            if '**' not in r and '!!' not in r:
                                count_1 += 1
print(count_1)