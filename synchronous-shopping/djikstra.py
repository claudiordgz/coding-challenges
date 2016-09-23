import math


g = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}


def djikstra(graph, start):
    unvisited = {node: math.inf for node in graph.keys()} #using None as +inf
    visited = {}
    current = start
    current_distance = 0
    unvisited[start] = current_distance

    while unvisited:
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key=lambda x: x[1])[0]
        for neighbour, distance in graph[current].items():
            if neighbour not in unvisited: continue
            new_distance = current_distance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
        visited[current] = current_distance
        del unvisited[current]


    return visited



shortest_path = djikstra(g, 'B')
print(shortest_path)
'''
{'E': 2, 'F': 4, 'C': 3, 'A': 4, 'B': 0, 'D': 1, 'G': 2}
{'A': 4, 'D': 1, 'F': 4, 'C': 3, 'G': 2, 'E': 2, 'B': 0}
{'F': 4, 'E': 2, 'C': 3, 'D': 1, 'A': 4, 'G': 2, 'B': 0}
'''