""" if input array=[123], it takes the consecutive sub-arrays and if they are
    prime we will print the finl sum """

n=int(input())
list=[]
sublist=[]
l1=[]
l2=[]
for i in range(0,len(str(n))):
    a=int(n%10)
    n=int(n/10)
    list.append(a)
list.reverse()
#print(list)
for i in range(len(list) + 1):
    for j in range(i + 1, len(list) + 1):
        sub = list[i:j] 
        sublist.append(sub)
#print(sublist)
for i in sublist:
    total=0
    k=len(i)
    for j in range(0, len(i)):
        total = total + (i[j]*(10**(k-1)))
        k-=1
    l1.append(total)
for num in l1:
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           l2.append(num)
sum=0
for i in l2:
    sum+=i
print(sum)
