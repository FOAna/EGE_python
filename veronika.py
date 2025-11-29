s = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if ((a == 2) and (b != 2) and (c != 2)) or ((b == 2) and (a != 2) and (c != 2)) or ((c == 2) and (a != 2) and (b != 2)):
                s = s + 1
print(s)

