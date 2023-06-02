# prim's algorithm 
# used for minimum spanning trees
# finding the least-weighted path that connects all vertices with no cycle 

import heapq
from typing import List


def prims(adj: List[List[int]]) -> int:
    res = 0
    visited = set()
    minH = [[0, 0]]

    while len(visited) > 0:
        cost, i = heapq.heappop(minH)
        if i in visited:
            continue
        res += cost
        visited.add(i)
        for neighborCost, neighbor in adj[i]:
            if neighbor not in visited:
                heapq.heappush(minH, [neighborCost, neighbor])
    return res
