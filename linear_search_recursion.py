#Calling out the Recursion
def recursive_search(arr,l,r,x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return recursive_search(arr,l+1,r-1,x)

arr = [2,4,10,17,19,8,7]
x = 8
n = len(arr)

index = recursive_search(arr,0,n-1,x)

print(x,"is at index {i}".format(i = index))

