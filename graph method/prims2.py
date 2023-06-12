# another version of prim's algorithm to get more practice in
from collections import defaultdict
import heapq

def prim(graph):
    # select the starting node
    start_node = list(graph.keys())[0] # node here is from the first key in the graph

    # other data structures needed
    visited = set() # empty set to avoid cycles
    minHeap = [(0, start_node)] # we use a minHeap 
    spanning_tree = defaultdict(set) # this just makes a dictionary with a set inside

    while minHeap:
        # extract minimum-weight edge
        weight, node = heapq.heappop(minHeap) 
        if node in visited:
            return 
        
        # mark the node as visited
        visited.add(node)

        if node != start_node:
            spanning_tree[node].add(weight)
            spanning_tree[weight].add(node)

        for neighbor, edge_weight in graph[node].items():
            heapq.heappush(minHeap, (edge_weight, neighbor))
    
    return spanning_tree

