# a = ["baa", "abcd", "abca", "cab", "cad"]
# a = ["wrt","wrf","er","ett","rftt"]
a = ["zy","zx"]
def alienOrder(words):
    # build the adjacency list
    graph = {}

    for word in words:
        for c in word:
            if c not in graph.keys():
                graph[c] = []


    for i in range (len(words) - 1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                break


    print(graph)

    # build the indegree map

    inDegree = {u : 0 for u in graph}

    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    print("Indegree: {}".format(inDegree))
    q = []

    for v in inDegree:
        if inDegree[v] == 0:
            q.append(v)

    print("initial q: {}".format(q))

    top_sort = []

    while q:
        node = q.pop(0)

        top_sort.append(node)

        for des in graph[node]:
            inDegree[des] -= 1
            if inDegree[des] == 0:
                q.append(des)

    print(top_sort)

alienOrder(a)
