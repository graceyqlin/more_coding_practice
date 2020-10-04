import graph_find_route_between_nodes as graphs

tree_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['G'],
  'F' : [],
  'G' : []
}


print('bfs tree_graph')
print(graphs.find_route_bfs(tree_graph, 'A', 'F'))

print('dfs tree_graph')
print(graphs.find_route_dfs(tree_graph, 'A', 'F'))


back_edge_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['G', 'B'],
  'F' : [],
  'G' : []
}

print('bfs back_edge_graph')
print(graphs.find_route_bfs(back_edge_graph, 'A', 'F'))

print('dfs back_edge_graph')
print(graphs.find_route_dfs(back_edge_graph, 'A', 'F'))


muptiple_path_graph = {
  'A' : ['B','C', 'G'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['G', 'B'],
  'F' : [],
  'G' : []
}

print('bfs muptiple_path__graph')
print(graphs.find_route_bfs(muptiple_path_graph, 'A', 'F'))

print('dfs muptiple_path__graph')
print(graphs.find_route_dfs(muptiple_path_graph, 'A', 'F'))


cross_edge_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'C'],
  'C' : ['F'],
  'D' : [],
  'E' : ['G', 'B'],
  'F' : [],
  'G' : []
}

print('bfs cross_edge_graph')
print(graphs.find_route_bfs(cross_edge_graph, 'A', 'F'))

print('dfs cross_edge_graph')
print(graphs.find_route_dfs(cross_edge_graph, 'A', 'F'))




