def bubble_sort(arr):
    n=len(arr)
    for i in range (n-1):
        flag=False 
        for j in range (n-i-1):
            if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
               flag=True
        if(flag==False):
            break
arr=list(map(int,input("enter array").split()))
print("original array",arr)
bubble_sort(arr)
print("sorted array",arr)