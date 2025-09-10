
# Adjancy List representation of a graph
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E','C', 'A']
graph['C'] = ['A', 'B', 'E','F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)

print("Graph:", graph)
print("Matrix Elements:", matrix_elements)
print("Rows:", rows)
print("Cols:", cols)

adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
print("Adjacency Matrix:", adjacency_matrix)
edges_list = []

for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key, neighbor))

print("Edges List:", edges_list)

for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1


print(adjacency_matrix)

