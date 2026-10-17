"""tinyq - a tiny in-memory priority queue with TTL expiry."""
import heapq
import itertools
import time

__all__ = ["TinyQ"]


class TinyQ:
    def __init__(self, clock=time.monotonic):
        self._heap = []
        self._counter = itertools.count()
        self._clock = clock

    def push(self, item, priority=0, ttl=None):
        """Push item. Lower priority number pops first. ttl in seconds, None = never expires."""
        expires = None if ttl is None else self._clock() + ttl
        heapq.heappush(self._heap, (priority, next(self._counter), expires, item))

    def pop(self):
        """Pop the highest-priority unexpired item, or None if empty."""
        heap = self._heap
        # Fast exit if heap is empty without querying clock
        if not heap:
            return None

        now = None
        clock = self._clock
        heappop = heapq.heappop
        while heap:
            priority, _, expires, item = heappop(heap)
            # If item has no TTL, avoid reading system clock
            if expires is None:
                return item
            if now is None:
                now = clock()
            if expires > now:
                return item
        return None

    def __len__(self):
        return len(self._heap)
