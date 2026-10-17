"""tinyq - a tiny in-memory priority queue with TTL expiry."""
import heapq
import itertools
import time

__all__ = ["TinyQ"]


class TinyQ:
    def __init__(self, max_size=128, clock=time.monotonic):
        self.max_size = max_size
        self._heap = []
        self._counter = itertools.count()
        self._clock = clock

    def push(self, item, priority=0, ttl=None):
        """Push item. Lower priority number pops first. ttl in seconds, None = never expires."""
        expires = None if ttl is None else self._clock() + ttl
        heapq.heappush(self._heap, (priority, next(self._counter), expires, item))

    def pop(self):
        """Pop the highest-priority unexpired item, or None if empty."""
        now = self._clock()
        while self._heap:
            priority, _, expires, item = heapq.heappop(self._heap)
            if expires is None or expires > now:
                return item
        return None

    def __len__(self):
        return len(self._heap)
