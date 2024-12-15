def selection_sort(arr):
    n=len(arr)
    for i in range (n-1):
        min=i
        for j in range (i+1,n):
            if arr[j]<arr[min]:
                min=j
        if(min!=i):
            arr[i],arr[min]=arr[min],arr[i]
arr=list(map(int,input("enter array").split()))
print("original array",arr)
selection_sort(arr)
print("sorted array",arr)