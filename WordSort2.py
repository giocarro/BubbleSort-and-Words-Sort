#!/env/bin/python

def bubbleSort(data):
    n=0
    m=0
    l=len(data)
    r1=range(l)
    s=l-1
    r2=range(s)
    for i in r2:
        for j in r2:
            if j==s: break
            elif data[j]>data[j+1]:
                a=data[j]
                data[j]=data[j+1]
                data[j+1]=a
                n+=1
            m+=1
        m+=1
        s-=1
    
    for i in r1:
        print(data[i])

    print 'Inside If: ',n,'\nIterations: ',m
    pass

if __name__=='__main__':
    File=open("words.txt","r")
    data=File.readlines()
    bubbleSort(data)
