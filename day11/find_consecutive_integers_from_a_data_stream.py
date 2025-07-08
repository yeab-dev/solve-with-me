from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.stream = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        
        if num == self.value:
            self.count += 1
        
        if len(self.stream) > self.k:
            removed = self.stream.popleft()
            if removed == self.value:
                self.count -= 1

        return len(self.stream) == self.k and self.count == self.k
