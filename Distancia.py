graph = {
  'El rosario' : ['Tacuba','Instituto del petróleo'],
  'Instituto del petróleo' : ['El rosario', 'La Raza'],
  'La Raza' : ['Instituto del petróleo', 'Consulado'],
  'Tacuba' : ['El rosario', 'Hidalgo', 'Tacubaya'],
  'Consulado' : ['La raza', 'Martin Carrera', 'Oceanía'],
  'Guerrero' : ['Hidalgo', 'La raza', 'Garibaldi'],
  'Hidalgo': ['Tacuba', 'Bellas Artes', 'Guerrero', 'Balderas' ]
}

visited = [] 
queue = []  

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


bfs(visited, graph, 'El rosario')
