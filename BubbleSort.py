#!/env/bin/python

import random

n=20

def bubbleSort(arr):
    a=0
    print 'Initial array:\t',arr
    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]: 
                a=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a

    print 'Final array:\t',arr
    pass

if __name__=='__main__':
    arr=[]
    for i in range(n):
        v=random.randint(100,9999)
        arr.append(v)
    bubbleSort(arr)

