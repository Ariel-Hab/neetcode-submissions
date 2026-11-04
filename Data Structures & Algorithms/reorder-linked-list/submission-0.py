class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        current = head
        # Frenamos cuando quede 1 o 2 nodos por procesar
        while current.next and current.next.next:
            # 1. Reiniciar la búsqueda desde current para encontrar el penúltimo
            penultimo = current
            while penultimo.next.next is not None:
                penultimo = penultimo.next
                
            # 2. El último nodo es el siguiente al penúltimo
            last = penultimo.next
            
            # 3. Cortar el enlace del penúltimo para no crear un ciclo
            penultimo.next = None
            
            # 4. Insertar 'last' entre 'current' y 'current.next'
            next_node = current.next
            current.next = last
            last.next = next_node
            
            # 5. Avanzar al siguiente nodo original
            current = next_node