import bisect
 
N, M = input().split()
list1 = (int(input()) for _ in range(int(N)))
list2 = (int(input()) for _ in range(int(M)))
 
for x in list2:
    i = bisect.bisect_left(list1, x)
    if list1[i] == x:
        print(i + 1, bisect.bisect(list1, x, i))
    else:
        print(0)