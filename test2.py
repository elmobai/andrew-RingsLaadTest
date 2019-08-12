with open('C:\Users\Emlyn Farrell\Desktop\andrew ps test\test1') as infile, open('C:\Users\Emlyn Farrell\Desktop\andrew ps test\test1output', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == "N10":
            copy = True
            continue
        elif line.strip() == "FINISH PASS":
            copy = False
            continue
        elif copy:
            outfile.write(line)

            