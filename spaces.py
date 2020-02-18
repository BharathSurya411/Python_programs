                          
l=[]
new=[]
n=input()
space_size1=0
word_size1=0
space_size2=0
word_size2=0
for i in range(0,len(n)):
    if(n[i]==" "):space_size1+=1
for i in range(0,len(n)):
    if(n[i]==" "):l.append(n[i])
k=n.split()
if len(k)==1:print("Please Enter more than One Word..")
else:
    for pop in range(0,len(k)-1):l.pop()
    word_size1=len(k)
    for i in k:
        new.append(i)
        if(i!=k[len(k)-1]):
            new.append(" ")
            for j in l:
                new.append(j)
                l.pop()
                break
        else:
            while(len(l)):
                for m in range(0,len(new)):
                    if (new[m]!=" " and new[m]!=new[len(new)-1]):
                        for j in l:
                            new.insert((m+1),j)
                            l.pop()
                            break
    for j in range(0,len(new)):
        if(new[j]==" "):space_size2+=1
        else:word_size2+=1
    for i in new:print(i,end="")
    print()
    print("The given sentence has",word_size1,"words and",space_size1,"spaces..")
    print("The given sentence has",word_size2,"words and",space_size2,"spaces..")
