def Shell(A):
    t = int(len(A)/2)
    while t > 0:
        for i in range(len(A)-t):
            j = i
            while j >= 0 and A[j] > A[j+t]:
                A[j], A[j+t] = A[j+t], A[j]
                j -= 1
        t = int(t/2)