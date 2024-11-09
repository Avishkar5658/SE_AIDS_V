
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []  # List for visited nodes
queue = []  # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)  # Mark the node as visited
    queue.append(node)  # Add the node to the queue
    while queue:  # Loop to visit each node
        m = queue.pop(0)  # Dequeue a node
        print(m, end=" ")  # Print the visited node
        for neighbour in graph[m]:  # Visit the unvisited neighbors
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver code
print("Following is the Breadth-First Search:")
bfs(visited, graph, '5')  # Start BFS from node '5'
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()  # Set to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:  # If the node is not visited
        print(node)  # Print the node
        visited.add(node)  # Mark the node as visited
        for neighbour in graph[node]:  # Visit each unvisited neighbor
            dfs(visited, graph, neighbour)

# Driver code
print("Following is the Depth-First Search:")
dfs(visited, graph, '5')  # Start DFS from node '5'