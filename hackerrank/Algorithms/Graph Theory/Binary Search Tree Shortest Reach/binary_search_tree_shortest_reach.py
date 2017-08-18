from collections import deque
import gc
def breadth_first_collect_distances(nodes, start_node_index):
	distances = [-1 for node in nodes]
	previously_traversed = set()
	previously_traversed.add(start_node_index)
	nodes_to_check = deque()
	nodes_to_check.append(start_node_index)
	current_distance = 0
	while len(nodes_to_check) > 0:
		original_queue_length = len(nodes_to_check)
		for _ in range(original_queue_length):
			traversed_index = nodes_to_check.popleft()
			distances[traversed_index] = current_distance
			for edge_node_index in nodes[traversed_index]:
				if edge_node_index not in previously_traversed:
					previously_traversed.add(edge_node_index)
					nodes_to_check.append(edge_node_index)
		current_distance += 6
	return distances

cases = int(input())
for _ in range(cases):
	count_inputs = input().split()
	node_count = int(count_inputs[0])
	edge_count = int(count_inputs[1])
	nodes = [deque() for _ in range(node_count)]
	for _ in range(edge_count):
		edge_inputs = input().split()
		node_index_1 = int(edge_inputs[0]) - 1
		node_index_2 = int(edge_inputs[1]) - 1
		nodes[node_index_1].append(node_index_2)
		nodes[node_index_2].append(node_index_1)
	start_index = int(input()) - 1
	distances = breadth_first_collect_distances(nodes, start_index)
	print(" ".join(str(distances[node_index]) for node_index in range(node_count) if node_index != start_index))
