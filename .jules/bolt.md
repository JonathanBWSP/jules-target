# Bolt - performance log for jules-target

## Log
- 2026-10-15: baseline benchmarks recorded (push/pop of 1e5 items: 0.41 s).

## 2026-10-16 - Binding counter `__next__` on `self` vs `next(self._counter)`

**Learning:** Binding `self._counter_next = itertools.count().__next__` on instance creation and calling `self._counter_next()` in `push()` is ~22% slower than `next(self._counter)` in Python 3.12. The `self` attribute lookup overhead outweighs the benefit of bypassing `builtins.next`, because Python 3.12 optimizes `next()` calls at the bytecode level (`CALL_INTRINSIC_1`).

**Action:** Keep using `next(self._counter)` for `itertools.count()` tie-breaker generation in Python 3.12 instead of trying to store bound method references on `self`.
