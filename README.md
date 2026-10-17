# tinyq

A tiny in-memory priority queue with TTL expiry. Pure Python, no dependencies.

```python
from tinyq import TinyQ
q = TinyQ()
q.push("job-a", priority=5, ttl=30)
q.pop()  # -> "job-a"
```

Run tests with `python -m pytest`.

Contributions welcome. Open an issue first for anything beyond a small fix.

## License

Released under the [MIT License](LICENSE).
