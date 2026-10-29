from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        # Cada key tendrá una lista de tuplas: (timestamp, value)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key)
        if not values:
            return ""

        # Usamos bisect_right buscando una tupla con (timestamp + 1) o un valor alto,
        # o especificando key con una función lambda:
        idx = bisect.bisect_right(values, timestamp, key=lambda x: x[0])

        # idx apunta a la posición donde iría; el elemento válido más cercano <= timestamp es idx - 1
        return values[idx - 1][1] if idx > 0 else ""