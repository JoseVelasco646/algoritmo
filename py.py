import numpy as np
from collections import deque

# Definimos la matriz
matriz = np.array([[-3,-3,2,-3,3,-2,-2,1,2,0,2,0,1],
                   [2,3,'I',-1,-1,3,2,0,-3,-3,2,2,1],
                   [1,-3,-3,2,3,1,3,3,2,1,-2,-2,3],
                   [0,0,3,0,3,-3,-2,-3,0,2,2,1,1],
                   [2,-1,-1,-3,3,3,0,-3,1,-2,2,0,1],
                   [0,3,-1,1,-1,-2,2,-2,2,-1,-2,-3,0],
                   [0,3,2,0,1,1,2,3,-1,-3,0,0,-2],
                   [3,3,-3,-2,3,-3,-1,-3,3,-2,2,-2,-1],
                   [-2,-2,1,0,-1,0,3,0,0,-2,2,-3,-1],
                   [-3,3,0,-1,-3,1,2,-3,2,-3,0,2,-2],
                   [-3,-3,-3,3,-2,0,-2,-3,1,0,1,-1,-2],
                   [-1,0,1,2,1,0,'F',0,-3,3,3,-2,-1],
                   [1,-3,1,0,1,2,3,1,-2,3,3,0,3]])

# Encuentra las posiciones de 'I' y 'F'
start = tuple(np.argwhere(matriz == 'I')[0])
end = tuple(np.argwhere(matriz == 'F')[0])

# BFS para encontrar el camino más corto
def bfs(start, end):
    rows, cols = matriz.shape
    queue = deque([start])
    visited = set()
    visited.add(start)
    path = {start: None}
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            break
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimientos: arriba, abajo, izquierda, derecha
            nr, nc = current[0] + dr, current[1] + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
                path[(nr, nc)] = current
    
    # Reconstruir el camino más corto
    step = end
    camino = []
    
    while step:
        camino.append(step)
        step = path[step]
    
    camino.reverse()
    return camino

# DFS para encontrar la ruta más larga
def dfs(start, end):
    rows, cols = matriz.shape
    stack = [(start, [start])]
    visited = set()
    max_path = []
    
    while stack:
        (current, path) = stack.pop()
        
        if current == end:
            if len(path) > len(max_path):
                max_path = path
            continue
        
        visited.add(current)
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimientos: arriba, abajo, izquierda, derecha
            nr, nc = current[0] + dr, current[1] + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                stack.append(((nr, nc), path + [(nr, nc)]))
    
    return max_path

# Ejecutar BFS y DFS para obtener las rutas
camino_corto = bfs(start, end)
camino_largo = dfs(start, end)

# Guardar los caminos en un archivo
with open("ruta_matrices.txt", "w") as f:
    # Imprimir el camino más corto
    f.write("Ruta más corta:\n")
    for (r, c) in camino_corto:
        f.write(f"({r}, {c}) -> {matriz[r, c]}\n")
    
    # Imprimir el camino más largo
    f.write("\nRuta más larga:\n")
    for (r, c) in camino_largo:
        f.write(f"({r}, {c}) -> {matriz[r, c]}\n")

print("Las rutas han sido guardadas en 'ruta_matrices.txt'.")
