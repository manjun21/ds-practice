
import heapq
from collections import defaultdict
m = [[1,4,-2],
[-2,3,4],
[3,1,3]]

hasht = defaultdict(int)

# count occurences of each num in matrix
for row in range(len(m)):
    for col in range(len(m[0])):
        hasht[m[row][col]] += 1

# push onto heap first by # occurs, then by desc digit
heap = []
for key, val in hasht.items():
    heapq.heappush(heap, (-val,key))

# traverse matrix's diags towards bottom left
# the start of each diag traversal is the top row, then last col
for diag_head in (m+m-1):
    row= 0 if diag_head < m else diag_head - m + 1
    col = diag_head if diag_head < m else m-1
    occurs, dig = heapq.heappop()[1]
    for _ in range(occurs):
        m[row][col] = dig

