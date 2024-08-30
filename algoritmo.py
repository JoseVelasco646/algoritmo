import numpy as np

import numpy as np

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
                    [1,-3,1,0,1,2,3,1,-2,3,3,0,3]
                   
                   ])
etiquetas_filas = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m']
numeros_columnas = list(range(1, matriz.shape[0] + 1))

print("    ", end="")
for letra in etiquetas_filas:
    print(f"  {letra}  ", end="")

print()

for i in range(matriz.shape[0]):
    print(f"{numeros_columnas[i]:<4}", end="")

    for j in range(matriz.shape[1]):
        print(f"{matriz[i, j]:<5}", end="")

    print()