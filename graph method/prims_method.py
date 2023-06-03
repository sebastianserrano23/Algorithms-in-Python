# prim's algorithm 
# used for minimum spanning trees
# finding the least-weighted path that connects all vertices with no cycle 

import heapq
from typing import List


def prims(graph: List[List[int]]) -> int:
    res = 0
    visited = set()
    minH = [[0, 0]]

    while len(visited) > 0:
        cost, i = heapq.heappop(minH) # [0, 0] is what got popped, so cost = 0 and i = 0 intially 
        if i in visited: # node i is in visited
            continue # we continue with our program and ignore this node
        res += cost # add cost to res
        visited.add(i) # add i to the visisted set
        for neighborCost, neighbor in graph[i]: # 
            if neighbor not in visited:
                heapq.heappush(minH, [neighborCost, neighbor])
    return res
