graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

visited = set()

def dfs(node):
    if node in visited:
        return
    print(node, end=" ")
    visited.add(node)
    for i in graph[node]:
        dfs(i)

dfs('A')