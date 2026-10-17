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


def test_clear():
    q = TinyQ()
    q.push("item1")
    q.push("item2", priority=1)
    assert len(q) == 2
    q.clear()
    assert len(q) == 0
    assert q.pop() is None
