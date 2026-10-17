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


def test_size():
    t = [0.0]
    q = TinyQ(clock=lambda: t[0])
    assert q.size() == 0

    q.push("no_ttl")
    q.push("short", ttl=1)
    q.push("long", ttl=100)
    assert q.size() == 3

    t[0] = 5.0
    # "short" expired, "no_ttl" and "long" remain
    assert q.size() == 2

    q.pop()  # pops "no_ttl" or "long" depending on priority/counter (both priority 0, "no_ttl" popped)
    assert q.size() == 1

    t[0] = 200.0
    # "long" expired as well
    assert q.size() == 0
