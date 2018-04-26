import heapq

def dijkstra(graph, initial_node):
    distances = [float('Inf') for _ in range(len(graph.nodes))]
    distances[initial_node] = 0
    pq = [(0, initial_node)]
    while pq:
        top = heapq.heappop(pq)
        top_weight = top[0]
        top_index = top[1]
        for neighbor in graph.nodes[top_index]:
            new_weight = top_weight + 6
            if new_weight < distances[neighbor]:
                distances[neighbor] = new_weight
                heapq.heappush(pq, (new_weight, neighbor))
    return distances


class Graph:
    
    def __init__(self, n):
        self.nodes = {i: [] for i in range(n)}
        
    def connect(self, from_node, to_node):
        self.nodes[from_node].append(to_node)
        self.nodes[to_node].append(from_node)

        
    def find_all_distances(self, initial_node):
        distances = dijkstra(self, initial_node)
        res = []
        for distance in distances:
            if distance == float('Inf'):
                res.append(-1)
            elif distance == 0:
                continue
            else:
                res.append(distance)
        return res

'''
2
4 2
1 2
1 3
1
3 1
2 3
2
'''
g = Graph(4)
for x,y in [(1,2), (1,3)]:
    g.connect(x-1, y-1)
s = 1
a = g.find_all_distances(s-1)
print(*a, sep=" ")