# 4.Dependent_Projects.py

# 4. You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the first project is dependent on the second project).

#    All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built.

#    Example Input:
#     projects: a, b, c, d, e, f
#     dependencies: (d, a), (b, f), (d, b), (a, f), (c, d)

#    Example Output: f, e, a, b, d, c

#projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#dependencies = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd'), ('g', 'h')]

projects = ['a', 'b', 'c', 'd', 'e']
dependencies = [('e', 'a'), ('e', 'c'), ('e', 'd'), ('c', 'b'), ('d', 'b')]

# def get_project_order_bfs(projects, dependencies):
# 	import collections
# 	graph = collections.defaultdict(list)
# 	for item in dependencies:
# 		late_project = item[0]
# 		prior_project = item[1]
# 		graph[prior_project].append(late_project)

# 	prior_list = set([item[1] for item in dependencies])
# 	late_list = set([item[0] for item in dependencies])

# 	root_list = list(prior_list - late_list)

# 	visited = []

# 	while root_list:

# 		queue = [root_list.pop(0)]

# 		while queue:
# 			current = queue.pop(0)	
# 			if current not in visited:
# 				visited.append(current)

# 			next_list = graph[current]
# 			for next in next_list:
# 				if next not in visited:
# 					visited.append(next)
# 					queue.append(next)

# 	for project in projects:
# 		if project not in prior_list and project not in late_list:
# 			visited.append(project)

# 	return visited

# print('using bfs to get order')
# print(get_project_order_bfs(projects, dependencies))



# def get_project_order_dfs(projects, dependencies):
# 	import collections
# 	graph = collections.defaultdict(list)

# 	for item in dependencies:
# 		late_project = item[0]
# 		prior_project = item[1]
# 		graph[prior_project].append(late_project)

# 	prior_list = set([item[1] for item in dependencies])
# 	late_list = set([item[0] for item in dependencies])

# 	root_list = list(prior_list - late_list)

	
# 	stack = []
# 	visited = []

# 	def get_val_dfs(current, visited):
# 		if not current:
# 			return
# 		if current not in visited:
# 			visited.append(current)
# 		next_list = graph[current]
# 		if next_list:
# 			for next_val in next_list:
# 				get_val_dfs(next_val, visited)

# 		# return visited

# 	while root_list:
# 		root = root_list.pop()
# 		get_val_dfs(root, visited)

# 	for project in projects:
# 		if project not in prior_list and project not in late_list:
# 			visited.append(project)

# 	return visited

# print(get_project_order_dfs(projects, dependencies))


def get_dependancy_order(projects, dependencies):
	import collections
	graph = collections.defaultdict(list)

	for item in dependencies:
		late_project = item[0]
		prior_project = item[1]
		graph[prior_project].append(late_project)
	
	prior_list = set([item[1] for item in dependencies])
	late_list = set([item[0] for item in dependencies])

	root_list = list(prior_list - late_list)

	
	stack = []
	visited = []

	def get_val_dfs(current, visited):
		if not current:
			return
		if current not in visited:
			visited.append(current)
		next_list = graph[current]
		if next_list:
			for next_val in next_list:
				get_val_dfs(next_val, visited)

		# return visited

	while root_list:
		root = root_list.pop()
		get_val_dfs(root, visited)

	visited = visited[::-1]

	for project in projects:
		if project not in prior_list and project not in late_list:
			visited.append(project)

	return visited


print(get_dependancy_order(projects, dependencies))




