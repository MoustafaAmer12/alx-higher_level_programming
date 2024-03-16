#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 = (tuple_a[0] if len(tuple_a) > 0 else 0,
          tuple_a[1] if len(tuple_a) > 1 else 0)
    t2 = (tuple_b[0] if len(tuple_b) > 0 else 0,
          tuple_b[1] if len(tuple_b) > 1 else 0)
    a = tuple(map(sum, zip(t1, t2)))
    return a
