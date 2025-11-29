k=0
for a1 in "123456789ABCDEF":
    for a2 in "0123456789ABCDEF":
        for a3 in "0123456789ABCDEF":
            for a4 in "0123456789ABCDEF":
                s=a1+a2+a3+a4
                if len(s)==len(set(s)):
                    s = s.replace("0", "*")
                    s = s.replace("2", "*")
                    s = s.replace("4", "*")
                    s = s.replace("6", "*")
                    s = s.replace("8", "*")
                    s = s.replace("A", "*")
                    s = s.replace("C", "*")
                    s = s.replace("E", "*")
                    s = s.replace("1", "!")
                    s = s.replace("3", "!")
                    s = s.replace("5", "!")
                    s = s.replace("7", "!")
                    s = s.replace("9", "!")
                    s = s.replace("B", "!")
                    s = s.replace("D", "!")
                    s = s.replace("F", "!")
                    if "**" not in s and "!!" not in s:
                        k+=1
print(k)



