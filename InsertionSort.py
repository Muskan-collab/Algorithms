
def insertion_sort(arr):
   n=len(arr)
   for i in range (1,n):
       temp=arr[i]
       j=i-1
       while j>=0 and arr[j]>temp:
          arr[j+1]=arr[j]
          j-=1
       arr[j+1]=temp
arr=list(map(int,input().split()))
print("array",arr)
insertion_sort(arr)
print("sorted array",arr)
    