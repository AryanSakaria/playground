import networkx as nx 
import matplotlib.pyplot as plt 

import random
from collections import deque

class Node:
	def __init__(self, val = 0, color="white"):
		self.val = val
		self.color = color
		self.d = 0 
		self.pi = 0 #predecessor



class graph:
	def __init__(self):
		self.adj_list = {}
		self.V = {}
		self.edge_list = []
		self.G_v = nx.Graph()
		self.max_d = 0 

	def bfs(self, s):
		for v_node in self.V:
			self.V[v_node].color = "white"
			self.V[v_node].d = float("infinity")
			self.V[v_node].pi = None
		self.V[s].color = "gray"
		self.V[s].d = 0 
		self.V[s].pi = None 
		q = deque()
		q.append(s)
		while len(q):
			# u = q[0]
			u = q.popleft()
			for v in self.adj_list.get(u, []):
				if self.V[v].color == "white":
					self.V[v].color = "grey"
					self.V[v].d = self.V[u].d + 1
					self.max_d = max(self.max_d, self.V[v].d)
					self.V[v].pi = u 
					q.append(v)
			self.V[u].color = "black"

		print("printing BFS")
		for i_ in range(self.max_d+1):
			current_str = ""
			for node_p in self.V:
				if self.V[node_p].d == i_:
					current_str += str(node_p) + ' '
			print(current_str)
		print("BFS print complete")

	def dfs(self):
		for vertex in self.V:
			self.V[vertex].color = "white"
			self.V[vertex].pi = None 
		self.time = 0
		print("Starting DFS path")
		for vertex in self.V:
			if self.V[vertex].color == "white":
				# print(f"starting dfs visit for {vertex}")
				self.dfs_visit(vertex)
				# print(f'Color of {vertex} is {self.V[vertex].color}')

		print("DFS path completed")


	def dfs_visit(self, vertex):
		# print(vertex)
		self.time += 1 
		self.V[vertex].d = self.time
		self.V[vertex].color = "grey"
		# print(f'List of children of vertex {vertex} is {self.adj_list.get(vertex,[])}')
		for each_v in self.adj_list.get(vertex, []):
			# print(f'Color of {each_v} is {self.V[each_v].color}')
			if self.V[each_v].color == "white":
				# print(f"going to child {each_v}")
				print(f'Reached {each_v} from {vertex}')
				self.V[each_v].pi = vertex
				self.dfs_visit(each_v)
		self.time += 1
		self.V[vertex].time = self.time
		self.V[vertex].color = "black"


	def add_node(self,node):
		self.V[node.val] = node 
		return 

	def add_edge(self, edge):
		if not edge[0] in self.adj_list:
			self.adj_list[edge[0]] = []
		if not edge[1] in self.adj_list:
			self.adj_list[edge[1]] = []
		self.adj_list[edge[0]].append(edge[1])
		self.adj_list[edge[1]].append(edge[0])

		self.edge_list.append(edge)
		pass

	def visualise_graph(self):
		self.G_v.add_edges_from(self.edge_list)
		nx.draw_networkx(self.G_v)
		plt.show()

if __name__ == '__main__':
	G = graph()
	num_nodes = 10 
	num_edges = random.randint(num_nodes,num_nodes*(num_nodes-1)/2)
	for i in range(num_nodes):
		G.add_node(Node(i))

	edge_list = []
	for i in range(num_nodes):
		for j in range(i + 1, num_nodes):
			edge_list.append((i,j))
	edges = random.sample(edge_list, num_edges)
	for edge in edges:
		G.add_edge(edge)
	G.bfs(0)
	G.dfs()
	G.visualise_graph()



