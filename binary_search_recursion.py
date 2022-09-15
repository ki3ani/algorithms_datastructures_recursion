def binary_search(arr,left,right,x):

    if left < right:

        mid = (left + right)//2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr,left,mid-1,x)
        
        if arr[mid] < x:
            return binary_search(arr,mid+1,right,x)
        
    return -1

arr = [5,3,8,9,10,17,85,35,29]
x = 85
n = len(arr)
index = binary_search(arr,0,n-1,x)

print("We have",x, "at index", index)
