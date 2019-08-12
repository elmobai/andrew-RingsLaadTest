import re
with open('C:\Users\Emlyn Farrell\Desktop\andrew ps test\test1') as myfile:
    content = myfile.read()

text = re.search(r'N10\n.*?FINISH PASS', content, re.DOTALL).group()
with open('C:\Users\Emlyn Farrell\Desktop\andrew ps test\test1output', "w") as myfile2: myfile2.write(text)