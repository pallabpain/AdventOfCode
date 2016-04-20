from collections import defaultdict
from itertools import permutations

def get_route(r, g, op):
    return op([sum(map(lambda a, b: g[a][b], x[:-1], x[1:])) for x in r])

data = [line.strip('\n') for line in open("input.txt").readlines()]

graph = defaultdict(dict)
for datum in data:
    a, _, b, _, distance = datum.split()
    graph[a][b] = graph[b][a] = int(distance)

print "Shortest distance =", get_route(permutations(graph), graph, min)
print "Longest distance =", get_route(permutations(graph), graph, max)