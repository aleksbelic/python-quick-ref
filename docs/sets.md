# Sets

Unordered collections using `{}` with no duplicates. Duplicates are silently ignored.

## Creating sets

Order is not guaranteed; each element appears only once.

```python
s1 = {'Mr', 'Mrs', 'Miss', 'Mr'}
print(len(s1))  # 3, duplicate is being ignored
```

!!! tip "Deduplication trick"
    Use `set(my_list)` to remove duplicates from a list, then `list(...)` to convert back if needed.
