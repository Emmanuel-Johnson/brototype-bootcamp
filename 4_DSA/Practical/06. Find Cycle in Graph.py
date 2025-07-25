# Python Program To Implement Graph Insertion Operation | Add Node | Adjacency Matrix | Data Structure

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

# undirected unweighted graph

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
        
# undirected weighted graph

def add_edge_2(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "Not present in the graph")
    elif v2 not in nodes:
        print(v2, "Not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost
        
# directed unweighted graph

def add_edge_3(v1, v2):
    if v1 not in nodes:
        print(v1, "Not present in the graph")
    elif v2 not in nodes:
        print(v2, "Not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        
# directed weighted graph

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
print(nodes)
print(graph)

add_edge_1("A", "B")
add_edge_1("A", "C")

print_graph()

print()

delete_node("A")
print_graph()








"""# Python Program To Implement Graph Insertion Operation | Add Node | Adjacency List | Data Structure

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
        graph[v1].append(v2)
        graph[v2].append(v1)

# weighted undirected graph

def add_edge_2(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append((v2, cost))
        graph[v2].append((v1, cost))

# unweighted directed graph

def add_edge_3(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)

# weighted directed graph

def add_edge_4(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append((v2, cost))


graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_edge_4("A", "B", 10)
add_edge_4("A", "C", 5)
add_edge_4("C", "D", 20)
print(graph)"""










