from tinyq import TinyQ


def test_priority_order():
    q = TinyQ()
    q.push("low", priority=5)
    q.push("high", priority=1)
    assert q.pop() == "high"
    assert q.pop() == "low"
    assert q.pop() is None


def test_ttl_expiry():
    t = [0.0]
    q = TinyQ(clock=lambda: t[0])
    q.push("short", ttl=1)
    q.push("long", ttl=100)
    t[0] = 5.0
    assert q.pop() == "long"
    assert q.pop() is None


def test_default_max_size():
    q = TinyQ()
    assert q.max_size == 128
