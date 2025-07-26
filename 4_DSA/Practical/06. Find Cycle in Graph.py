"""# Python Program To Implement Graph Insertion Operation | Add Node | Adjacency Matrix | Data Structure

# It will work for every type of graph like undirected unweighted etc

def add_node(v):
    global node_count 
    if v in nodes:
        print("V is already present in the graph")
    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

# Python Program To Implement Graph Insertion Operation | Add Edge | Adjacency Matrix | Data Structure

# unweighted undirected graph

def add_edge_1(v1, v2):
    if v1 not in nodes:
        print(v1, "Not present in the graph")
    elif v2 not in nodes:
        print(v2, "Not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1
        
# unweighted directed graph

def add_edge_2(v1, v2):
    if v1 not in nodes:
        print(v1, "Not present in the graph")
    elif v2 not in nodes:
        print(v2, "Not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        
# weighted undirected graph

def add_edge_3(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "Not present in the graph")
    elif v2 not in nodes:
        print(v2, "Not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost
        
# weighted directed graph

def add_edge_4(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "Not present in the graph")
    elif v2 not in nodes:
        print(v2, "Not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        
# Python Program For Graph Deletion Operation | Delete Node | Adjacency Matrix | Data Structure

# It will work for every type of graph like undirected unweighted etc

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, "is not present in the graph")
    else:
        index = nodes.index(v)
        nodes.remove(v)
        node_count -= 1
        graph.pop(index)
        for n in graph:
            n.pop(index)

# Python Program For Graph Deletion Operation | Delete Edge | Adjacency Matrix | Data Structure

# unweighted undirected graph, weighted undirected graph

def delete_edge_1(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0
        
# unweighted directed graph, weighted directed graph

def delete_edge_2(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end = " ")
        print()
        
nodes = []        
graph = []
node_count = 0

add_node("A")
add_node("B")
add_node("C")

print_graph()"""










# Python Program To Implement Graph Insertion Operation | Add Node | Adjacency List | Data Structure

def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []
        
# Python Program To Implement Graph Insertion Operation | Add Edge | Adjacency List | Data Structure

# unweighted undirected graph

def add_edge_1(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 not in graph[v1]:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
# unweighted directed graph

def add_edge_2(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 not in graph[v1]:
            graph[v1].append(v2)

# weighted undirected graph

def add_edge_3(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if [v2, cost] not in graph[v1]:
            graph[v1].append([v2, cost])
            graph[v2].append([v1, cost])

# weighted directed graph

def add_edge_4(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if [v2, cost] not in graph[v1]:
            graph[v1].append([v2, cost])

# Python Program For Graph Deletion Operation | Delete Node | Adjacency List | Data Structure

# directed unweighted graph, undirected unweighted

def delete_node_1(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

# undirected weighted graph, directed weighted

def delete_node_2(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for edge in list1[:]:
                if v == edge[0]:
                    list1.remove(edge)

# Python Program For Graph Deletion Operation | Delete Edge | Adjacency List | Data Structure

# unweighted undirected graph

def delete_edge_1(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
            
# unweighted directed graph

def delete_edge_2(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            
# weighted undirected graph

def delete_edge_3(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        temp1 = [v1, cost]
        temp2 = [v2, cost]
        if temp2 in graph[v1]:
            graph[v1].remove(temp2)
            graph[v2].remove(temp1)
            
# weighted directed graph

def delete_edge_4(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        temp = [v2, cost]
        if temp in graph[v1]:
            graph[v1].remove(temp)

# Python Program To Implement DFS Using Recursion | Data Structure

# unweighted undirected graph

def DFS_1(node, visited, graph):
    if node not in graph:
        print("Node is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS_1(i, visited, graph)
            
# weighted graph

def DFS_2(node, visited, graph):
    if node not in graph:
        print("Node is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS_2(i[0], visited, graph)

def print_graph():
    for n in graph:
        print(n, "-->" , graph[n])


graph = {}
visited = set()
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge_1("A", "B")
add_edge_1("B", "E")
add_edge_1("A", "C")
add_edge_1("A", "D")
add_edge_1("B", "D")
add_edge_1("C", "D")
add_edge_1("E", "D")
print_graph()







