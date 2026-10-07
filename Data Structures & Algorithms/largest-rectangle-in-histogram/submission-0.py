from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Guardará pares: (indice_de_inicio, altura)

        for i, h in enumerate(heights):
            #el nuevo rectangulo inicia en la columna iterada
            start = i
            
            #antes de agregarlo al stack, reviso si hay rectangulos previos mas pequeños
            # para agregarlos a este rectangulo, sino simplemente genero un nuevo rectangulo 
            # que luego va a ser "consumido" por otro rectangulo mayor o al finalizar
            while stack and stack[-1][1] > h:
                #saco el rectangulo menor
                index, height = stack.pop()  
                #obtengo mi nueva area y veo si es la nueva maxima              
                max_area = max(max_area, (i-index)*height)
                #extiendo mi rectangulo "incluyendo" este rectangulo menor
                start = index 
            
            #añado el nuevo rectangulo a la pila
            stack.append((start, h))

        # Una vez terminado el bucle, pueden quedar barras en la pila.
        # Estas son las barras que pudieron expandirse hasta el mismísimo final del arreglo.
        for i, h in stack:
            final = len(heights)
            max_area = max(max_area, (final-i)*h)
            pass 

        return max_area