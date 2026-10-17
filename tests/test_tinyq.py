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


def test_peek():
    t = [0.0]
    q = TinyQ(clock=lambda: t[0])
    assert q.peek() is None

    q.push("low", priority=5)
    q.push("high", priority=1, ttl=2)

    # peek returns highest priority item without popping
    assert q.peek() == "high"
    assert q.peek() == "high"

    # advance time so high expires
    t[0] = 3.0
    assert q.peek() == "low"
    assert q.pop() == "low"
    assert q.peek() is None
