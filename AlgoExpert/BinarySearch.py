# Recursive solution for binary search algorithms
# Time complexity -  O(logN)
# Space complexity - O(logN) for call stack during recursive call

def BinarySearch(ar,target):
    return BinarySearchHelper(ar,target,0,len(ar)-1)

def BinarySearchHelper(ar,target,l,r):
    if l>r:
        return -1
    Mid = (l+r)//2
    curr = ar[Mid]
    if curr == target:
        return Mid
    elif curr>target:
        return BinarySearchHelper(arr,target,Mid+1,r)
    else:
        return BinarySearchHelper(ar,targer,l,Mid-1)
