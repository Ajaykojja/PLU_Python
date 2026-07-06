graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

u = 'A'
v = 'B'

if v in graph[u]:
    print("Edge Exists")
else:
    print("Edge Does Not Exist")