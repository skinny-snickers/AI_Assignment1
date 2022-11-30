# A Node class for Greedy Best First Search Pathfinding
def draw():
    # Best First Search "graphics"
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.DiGraph()

    edges = [('0', '1', 2), ('0', '2', 1), ('0', '3', 10), ('1', '4', 3),
             ('1', '5', 2), ('2', '6', 9), ('3', '7', 5), ('3', '8', 2), ('7', '9', 5)]

    G.add_weighted_edges_from(edges)

    labels = nx.get_edge_attributes(G, 'weight')

    val_map = {
        '0': "tab:blue",
        '1': "tab:grey",
        '2': "tab:brown",
        '3': "tab:orange",
        '4': "tab:olive",
        '5': "tab:green",
        '6': "tab:cyan",
        '7': "tab:pink",
        '8': "tab:blue",
        '9': "tab:brown",
    }

    values = [val_map.get(nodes, 0.50) for nodes in G.nodes()]

    pos = nx.shell_layout(G, scale=2)

    # Controlling nodes
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color=values)
    # controlling edges "arrows between nodes"
    nx.draw_networkx_edges(G, pos, width=2, edgelist=G.edges(), edge_color='purple', arrowsize=20, arrowstyle='->')
    # for the edges lables obv
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.25)
    # labelzzz
    nx.draw_networkx_labels(G, pos)

    plt.show()


class Node:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight


# pathNode class will help to store
# the path from src to destination.
class pathNode:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent


# Function to add edge in the graph.
def addEdge(u, v, weight):
    # Add edge u -> v with weight weight.
    adj[u].append(Node(v, weight))


# Declaring the adjacency list
adj = []


# Greedy best first search algorithm function
def GBFS(h, V, src, dest):
    """
    This function returns a list of
    integers that denote the shortest
    path found using the GBFS algorithm.
    If no path exists from src to dest, we will return an empty list.
    """
    # Initializing openList and closeList.
    openList = []
    closeList = []

    # Inserting src in openList.
    openList.append(pathNode(src, None))

    # Iterating while the openList
    # is not empty.
    while (openList):

        currentNode = openList[0]
        currentIndex = 0
        # Finding the node with the least 'h' value
        for i in range(len(openList)):
            if (h[openList[i].node] < h[currentNode.node]):
                currentNode = openList[i]
                currentIndex = i

        # Removing the currentNode from
        # the openList and adding it in
        # the closeList.
        openList.pop(currentIndex)
        closeList.append(currentNode)

        # If we have reached the destination node.
        if (currentNode.node == dest):
            # Initializing the 'path' list.
            path = []
            cur = currentNode

            # Adding all the nodes in the
            # path list through which we have
            # reached to dest.
            while (cur != None):
                path.append(cur.node)
                cur = cur.parent

            # Reversing the path, because
            # currently it denotes path
            # from dest to src.
            path.reverse()
            return path

        # Iterating over adjacents of 'currentNode'
        # and adding them to openList if
        # they are neither in openList or closeList.
        for node in adj[currentNode.node]:
            for x in openList:
                if (x.node == node.v):
                    continue

            for x in closeList:
                if (x.node == node.v):
                    continue

            openList.append(pathNode(node.v, currentNode))

    return []



# The total number of vertices.
V = 10
## Initializing the adjacency list
for i in range(V):
    adj.append([])

addEdge(0, 1, 2)
addEdge(0, 2, 1)
addEdge(0, 3, 10)
addEdge(1, 4, 3)
addEdge(1, 5, 2)
addEdge(2, 6, 9)
addEdge(3, 7, 5)
addEdge(3, 8, 2)
addEdge(7, 9, 5)

# Defining the heuristic values for each node.
h = [20, 22, 21, 10, 25, 24, 30, 5, 12, 0]
path = GBFS(h, V, 0, 5)
for i in range(len(path) - 1):
    print(path[i], end=" -> ")

print(path[(len(path) - 1)])
draw()
