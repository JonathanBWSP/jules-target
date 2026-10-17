# tinyq

A tiny in-memory priority queue with TTL expiry. Pure Python, no dependencies.

Documentation: http://149.248.4.51:8081/docs/tinyq/

```python
from tinyq import TinyQ
q = TinyQ()
q.push("job-a", priority=5, ttl=30)
q.pop()  # -> "job-a"
```

Run tests with `python -m pytest`.

Contributions welcome. Open an issue first for anything beyond a small fix.
