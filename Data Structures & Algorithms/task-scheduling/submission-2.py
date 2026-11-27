from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        conteo = Counter(tasks)
        # Max-heap con las frecuencias negativas (no necesitamos el nombre de la tarea)
        max_heap = [-cnt for cnt in conteo.values()]
        heapq.heapify(max_heap)
        
        cola_espera = deque()  # Guarda pares: [frecuencia_restante, tiempo_disponible]
        time = 0
        
        while max_heap or cola_espera:
            time += 1
            
            if max_heap:
                # Ejecutamos la tarea más frecuente (sumar 1 reduce la magnitud del negativo)
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    # Estará disponible después de n intervalos
                    cola_espera.append([cnt, time + n])
            
            # Si la primera tarea en espera ya cumplió su enfriamiento, vuelve al heap
            if cola_espera and cola_espera[0][1] == time:
                heapq.heappush(max_heap, cola_espera.popleft()[0])
                
        return time