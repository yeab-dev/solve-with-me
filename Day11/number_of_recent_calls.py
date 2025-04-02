from collections import deque
class RecentCounter:
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] + 3000 < t:
            self.queue.popleft()
        return len(self.queue)