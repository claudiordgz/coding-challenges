from fixture import get_testcase,read_raw

import fileinput


def shortest_search(n_queries, queries):
    previous_elements = 0
    for query in range(n_queries):
        graph = dict()
        start_of_data = queries[previous_elements: ]
        n_m = [int(el) for el in start_of_data[0].split()]
        n_nodes, n_edges = int(n_m[0]), int(n_m[1])
        for node in range(1, n_nodes + 1):
            graph[node] = set()
        for e in start_of_data[1:n_edges+1]:
            edge = [int(n) for n in e.split()]
            if edge[0] not in graph:
                graph[edge[0]] = set()
            if edge[1] not in graph:
                graph[edge[1]] = set()
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        s = int(start_of_data[n_edges + 1])
        calculate_costs(graph, s)
        previous_elements += 2 + n_edges


def calculate_costs(g, s):
    costs = bfs(g, s)
    for k in g:
        if k not in costs and k != s:
            costs[k] = -1
    print(' '.join(map(str, costs.values())))


def bfs(graph, start):
    visited, queue, idx, costs, children = set(), [start], 0, dict(), 0
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            new_queue = graph[vertex] - visited
            queue.extend(new_queue)
            current_children = len(queue)
            if children == 0:
                children = current_children
                idx += 1
                for q in list(queue):
                    if q not in costs:
                        costs[q] = 6 * idx
        children -= 1
    return costs


def solution(data):
    #data =[line.rstrip('\n').rstrip('\r') for line in fileinput.input()]
    n_queries = int(data[0])
    shortest_search(n_queries, data[1:])



for t in '012345':
    i, o = get_testcase(t, read_as=read_raw)
    print(solution(i) == o[0])
