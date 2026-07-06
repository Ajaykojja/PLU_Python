graph={
    "A":["B","C"],
    "B":["D"],
    "C":["D"],
    "D":[]
}
vist=set()
queue=[]
queue.append("A")
while queue:
    node=queue.pop(0)
    if node not in vist:
        print(node)
        vist.add(node)
        for i in graph[node]:
            queue.append(i)
            