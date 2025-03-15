from collections import deque

def bfs(graph, start_node):
    """Perform BFS on a graph from the start_node."""
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph.get(node, []))
    
    return visited
