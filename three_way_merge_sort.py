# import sys
# sys.setrecursionlimit(10000)

def three_way_merge_sort(A, low, high, B):
    if((high - low )< 2):
        return
    mid1 = low + (high-low)//3 
    mid2 = low + 2*((high-low)//3) + 1
    three_way_merge_sort(A, low, mid1, B)
    three_way_merge_sort(A,mid1, mid2, B)
    three_way_merge_sort(A, mid2, high, B)
    three_way_merge(A, low, mid1, mid2, high, B)

def three_way_merge(A, low, mid1, mid2, high, B):
    i = low
    j = mid1
    k = mid2
    l = low
    while(i<mid1 and j<mid2 and k<high):
        if (A[i] < A[j]):
            if (A[i] < A[k]):
                B[l] = A[i]
                i+=1
            else:
                B[l] = A[k]
                k+=1
        elif (A[j] < A[k]):
            B[l] = A[j]
            j+=1
        else:
            B[l] = A[k]
            k+=1
        l+=1
    
    while(i<mid1 and j<mid2):
        if (A[i] < A[j]):
            B[l] = A[i]
            l+=1; i+=1
        else:
            B[l] = A[j]
            l+=1; j+=1
    
    while(j<mid2 and k< high):
        if(A[j] < A[k]):
            B[l] = A[j]
            l+=1; j+=1
        else:
            B[l] = A[k]
            l+=1; k+=1
    
    while(i<mid1 and k<high):
        if(A[i] < A[k]):
            B[l] = A[i]
            l+=1; i+=1
        else:
            B[l] = A[k]
            l+=1; k+=1
    
    while(i < mid1):
        B[l] = A[i]
        l+=1; i+=1
    
    while(j < mid2):
        B[l] = A[j]
        l+=1; j+=1
    
    while(k < high):
        B[l] = A[k]
        l+=1; k+=1
    

data = [45, -2, -25, 78, 30, -42, 10, 19, 73, 93]
result = [0, 0, 0,0,0,0,0,0,0,0]
print(10//3)
three_way_merge_sort(data, 0, 10, result)
print(result)