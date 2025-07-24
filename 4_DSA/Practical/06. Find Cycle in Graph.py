# Python Program To Implement Graph Insertion Operation | Add Node | Adjacency Matrix | Data Structure

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
        
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end = " ")
        print()
        
nodes = []        
graph = []
node_count = 0

print("Before Adding Nodes")
print(nodes)
print(graph)
print("After Adding Nodes")
add_node("A")
add_node("B")
add_node("C")
print(nodes)
print(graph)

print_graph()

