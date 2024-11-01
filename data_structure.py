from collections import defaultdict, deque




class Stack:
    def __init__(self) -> None:
        """Stack (FILO)
        """
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        try:
            return self.items.pop()
        except:
            return None

    def peek(self):
        try:
            return self.items[-1]
        except:
            return None

    def size(self):
        return len(self.items)
    




class Queue:
    def __init__(self):
        """Queue (FIFO)
        """
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        try:
            return self.items.pop()
        except:
            return None
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []





class Node(object):
    
    def __init__(self, nodeId):
        self._id = nodeId

    @property
    def id(self):
        return self._id

    def __str__(self):
        return str(self.id)


    
    
class Edge(object):

    def __init__(self, src:Node, dest:Node):
        self._src = src
        self._dest = dest

    @property
    def src(self):
        return self._src

    @property
    def dest(self):
        return self._dest

    def __str__(self):
        return '{}->{}'.format(self._src.id, self._dest.id)




class DiGraph():
    
    def __init__(self):
        """Directed graph
        """
        self.edges: dict[list] = {}
        
    def addNode(self, node:Node):
        if node in self.edges:
            raise ValueError("Duplicate node.")
        else:
            self.edges[node] = []
    
    def addEdge(self, edge:Edge):
        if edge.src not in self.edges:
            self.addNode(edge.src)
        if edge.dest not in self.edges:
            self.addNode(edge.dest)
        self.edges[edge.src].append(edge.dest)
    
    def childrenOf(self, node:Node):
        return self.edges[node]
    
    def hasNode(self, node:Node):
        return node in self.edges
    
    def getNode(self, nodeId:int):
        for node in self.edges:
            if node.id == nodeId:
                return node
        raise KeyError(nodeId)
    
    @property
    def nodes(self):
        nodes = []
        for src in self.edges:
            if src not in nodes:
                nodes.append(src)
            for dest in self.edges[src]:
                if dest not in nodes:
                    nodes.append(dest)
        return nodes
                

    
    def __str__(self):
        connections = ''
        for src in self.edges:
            for dest in self.edges[src]:
                connections += f"{str(src.id)} -> {str(dest.id)}\n"
        return connections[:-1] # omit final new line
        
        
        

class Graph(DiGraph):
    
    def addEdge(self, edge:Edge):
        DiGraph.addEdge(self, edge)
        revEdge = Edge(src=edge.dest, dest=edge.src)
        DiGraph.addEdge(self, revEdge)





def dfs(g:Graph, nodeId:int, visited)->list:
    """Depth First Search (DFS)

    Args:
        g (Graph): _description_
        nodeId (int): _description_
        visited (dict[Int:Bool]): "True" if node is visted before "False" otherwise

    Returns:
        list[Int]: List of visited nodeId in the path
    """
    src = [node for node in g.edges.keys() if node.id==nodeId][0]
    
    visit = [nodeId]
    visited[nodeId] = True

    for dest in g.edges[src]:
        if not visited[dest.id]:
            visit += dfs(g, dest.id, visited)

    return visit        



def dfs_1(edges:list[list], source:int)->list:
    """Depth First Search (DFS)

    Args:
        edges (list[list]): list of edges with sources and destinations, ex. [[0,1],[0,2]]
        source (int): the starting node of the search
    Returns:
        list: returns the list of the nodes in the path in order visited by the algorithm
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited= set()
    stack  = deque([source])
    path= []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            path.append(node)
            visited.add(node)
            
            for nbr in graph[node]:
                if nbr not in visited:
                    stack.append(nbr)
    return path

        

def bfs(edges:list[list[int]], source:int)    :
    """Breadth First Search (BFS)

    Args:
        edges (list[list]): list of edges with sources and destinations, ex. [[0,1],[0,2]]
        source (int): the starting node of the search
    Returns:
        list: returns the list of the nodes in the path in order visited by the algorithm
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited= set()
    queue  = deque([source])
    path = []
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            path.append(node)
            visited.add(node)
                        
            for nbr in graph[node]:
                if nbr not in visited:
                    queue.append(nbr)
    return path
            
            
    

def main():
    pass
    
    
    
    
if __name__=='__main__':
    main()
