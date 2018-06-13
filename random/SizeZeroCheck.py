import re
str2='''02/15/2016              10:49 PM               962                       switchfinal.py
02/15/2016              10:49 PM               943                       switchfinal.py.bak
01/27/2016              11:46 AM                15                        t.py
03/31/2016              12:39 PM               840                       t1.py
01/25/2016              10:34 AM             2,407                      tc1.py
02/14/2017              09:13 AM                 0                         teat.py
03/15/2016              05:52 PM                 5                         tes.py'''


'''
class LineReader(str2):
    for line in str2:
        print(line)
'''

timeRe=re.compile(r"[0-9]{2}:[0-9]{2} [A|P]M")
DateRe=re.compile(r"[0-9]{2}/[0-9]{2}/[0-9]{4}")
FileNre=re.compile(r"[a-zA-Z0-9.]+")



str3=str2.split("\n")
for line in str3:
    print( line)
    t=timeRe.findall(line)
    print(t)
    d=DateRe.findall(line)
    print(d)
    #print(str(t[0])+"   "+str(d[0]))
    line=line.strip(str(d[0])+" ")
    #strip funx=ctio strips all the chars from suppied input hence 9 is getting stripped
    print(line)
    line=line.strip(" ")
    print line
    line=line.strip(t[0])
    print (line)
    #print(k)
    f=FileNre.findall(line)
    print(f)
#print(str3)
