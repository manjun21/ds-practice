import collections
def diagonalSort(A):
        n, m = len(A), len(A[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                print(i-j)
                d[i - j].append(A[i][j])
                print(d)
        for k in d:
            d[k].sort(reverse=False)
        for i in range(n):
            for j in range(m):
                A[i][j] = d[i - j].pop()
        return A


mat = [ [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
print(diagonalSort(mat))

#2,2->-2