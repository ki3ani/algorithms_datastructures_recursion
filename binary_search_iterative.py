def binary_search(arr,x):
    left = 0
    right = len(arr)-1
    mid = 0 

    while(left <= right):

        mid = (left + right)//2

        if(arr[mid] > x):
            right = mid -1

        elif(arr[mid] < x):
            left = mid + 1
        
        else:
            return mid

    return -1


arr =  [34,57,68,92,105]

x = 92
ind = binary_search(arr,x)
print(x,"is at the index:", ind)

#Time complexity is at the order of 0(logn)
#The space is at 0(1)
#note to do a binary search, the items should be sorted first



