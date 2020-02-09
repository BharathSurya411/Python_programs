list=[]
l2=[]
m=[]
l3=[]
def Remove(l2): 
    final_list = [] 
    for num in l2: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

n=int(input())
for i in range(0,n):
    l=[]
    list.append(l)
for i in range(0,n):
    for j in range(0,2):
        a=input()
        list[i].append(a)
for i in list:
        l2.append(i[1])
l2.sort()
k=Remove(l2)[1]
for i in list:
    for j in i:
        m.append(j)
for i in m:
    if(i==k):
        l3.append(m)
    m=i
l3.sort()
for i in l3:
    print(i)
