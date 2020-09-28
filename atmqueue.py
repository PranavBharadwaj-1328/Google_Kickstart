import numpy as np

def getoutqueue(N,X,A):
    Q = list(np.arange(1,N+1,1))
    O = []
    while(len(Q) != 0):
        i = Q[0]
        A[i-1] = A[i-1] - X
        if(A[i-1] <= 0):
            Q.remove(i)
            O.append(i)
            continue
        else:
            Q.remove(i)
            Q.append(i)
            continue
    print(' '.join(map(str, O)))

def atmqueue():
    T = int(input())
    N = []
    X = []
    A = []
    for i in range(T):
        x,y = input().split()
        N.append(int(x))
        X.append(int(y))
        A.append(list(map(int,input().strip().split()))[:N[i]])
    for i in range(T):
        getoutqueue(N[i],X[i],A[i])

atmqueue()
