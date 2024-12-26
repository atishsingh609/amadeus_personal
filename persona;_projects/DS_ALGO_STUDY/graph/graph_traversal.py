#=======================DFS==============================
from collections import deque

graph = {"a" : ["b", "c"],
         "b" : ["d", "e"],
         "c" : ["f", "g"],
         "d" : [],
         "e" : [],
         "f" : [],
         "g" : []}

def traverse(graph, edge):

    stack = [edge]
    while stack:
        cur_edge = stack.pop()
        print(cur_edge, end = " ")
        for next_edge in graph[cur_edge]:
            stack.append(next_edge)

print(traverse(graph, "a"))


def recursive_traverse(graph, edge):
    print(edge, end = " ")
    for cur_edge in graph[edge]:
        recursive_traverse(graph, cur_edge)

recursive_traverse(graph, "a")



#========================BFS==================================================

def bfs_traverse(graph, edge):

    queue = deque([edge])
    while queue:
        cur_edge = queue.popleft()
        print(cur_edge, end = " ")
        for next_edge in graph[cur_edge]:
            queue.append(next_edge)
bfs_traverse(graph, "a")