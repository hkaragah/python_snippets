"""
GRAPH:

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.

"""


from collections import defaultdict, deque

def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    """ 
        Approach: Breadth First Search (BFS)
    """
    
    # Step 1: Build the adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 2: Use BFS to check if there is a path from source to destination
    visited = set()  # To track visited nodes
    queue = deque([source])
    visited.add(source)
    
    while queue:
        node = queue.popleft()
        
        # Check if we reached the destination
        if node == destination:
            return True
        
        # Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # If we've exhausted all possible paths without finding destination
    return False




def validPath_1(n:int, edges: list[list[int]], source:int, destination:int)->bool:
    """
        Approahc: Depth First Search (DFS)
    """
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)


    visited = set()
    visited.add(source)
    stack = deque([source])
    
    while stack:
        
        node = stack.pop()
        
        if node == destination:
            return True
        
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                stack.append(nbr)
                
    return False















def main():
    print(validPath(
        n=3,
        edges=[[0,1],[1,2],[2,0]],
        source=0,
        destination=2
    ))
    
    print(validPath(
        n=6,
        edges=[[0,1],[0,2],[3,5],[5,4],[4,3]],
        source=0,
        destination=5
    ))
    
    print(validPath_1(
        n=3,
        edges=[[0,1],[1,2],[2,0]],
        source=0,
        destination=2
    ))
    
    print(validPath_1(
        n=6,
        edges=[[0,1],[0,2],[3,5],[5,4],[4,3]],
        source=0,
        destination=5
    ))
    
    print(validPath_1(
        n=6,
        edges=[[0,1],[0,2],[2,3],[3,5],[5,4],[4,3]],
        source=0,
        destination=5
    ))
    
    print(validPath_1(
        n=6,
        edges=[[0,1],[0,2],[2,3],[3,5],[5,4],[4,3]],
        source=0,
        destination=1
    ))

import os
if __name__ == "__main__":
    os.system('cls')
    main()