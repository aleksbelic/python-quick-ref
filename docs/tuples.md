# Tuples

Ordered, immutable collections using `()`. Allow duplicates and mixed data types.

## Creating tuples

Like lists, but cannot be changed after creation.

```python
t1 = ('Mr', 'Mrs', 'Miss')
print(len(t1))  # 3

t2 = ('Mr', 123, 'Miss')
print(t2)  # ('Mr', 123, 'Miss')
```

!!! tip "When to use tuples"
    Use a tuple for fixed data that should never change — e.g. coordinates, record fields, or dictionary keys.
