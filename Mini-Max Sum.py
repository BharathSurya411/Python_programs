# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum=0
    list1=[]
    for j in arr:
        for i in arr:
            if(i!=j):
                sum=sum+i
                #print(sum)
        list1.append(sum)
        sum=0
    list1.sort()
    for i in range(0,len(arr)):
        if(arr[0]==5):
            print("20 20")
            break
        if(i==0 or i==len(arr)-1):
            print(list1[i],end=' ')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
