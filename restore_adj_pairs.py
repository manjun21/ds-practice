import collections
def restoreArray(adjacentPairs: list[list[int]]) -> list[int]:
        nb = collections.defaultdict(list)
        for u, v in adjacentPairs:
            nb[u].append(v)
            nb[v].append(u)

        for key, nb_num in nb.items():
            if len(nb_num) == 1:
                start = key
                break
        res = [start]
        pre = start
        cur = nb[start][0]
        while True:
            res.append(cur)
            if len(nb[cur]) > 1:
                #pre,cur = cur,nb[cur][0] if nb[cur][0] != pre else nb[cur][1]
                pre,cur =  cur,nb[cur][1] if nb[cur][0] == pre else nb[cur][0]
            else:
                break

        return res

adjacentPairs = [[2,1],[3,4],[3,2]]
print(restoreArray(adjacentPairs))