class MinStack:
    def __init__(self):
        # Guardaremos tuplas de la forma: (valor, minimo_hasta_ahora)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # Si la pila está vacía, el valor es también el mínimo
            self.stack.append((val, val))
        else:
            # Comparamos el nuevo valor con el mínimo del elemento anterior
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]