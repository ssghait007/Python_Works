file1=open("input.txt","r")
file2=open("output.txt","w")
i=0
lines=[]
for line in file1:
    line=line.rstrip(" ")
    line=line.lstrip(" ")
    words=0
    letters=0
    i+=1
    print line
    for letter in line:
        if(letter!=" "):
            letters+=1
        if(letter==" "):
            words+=1
    file2.write("line ="+str(i)+"   Words= "+str(words+1)+"   letters= "+str(letters)+"\n")

file1.close()
file2.close()
