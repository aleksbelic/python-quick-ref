# Collections

The `collections` module ships specialised containers that save you from writing the same boilerplate again and again.

## Counter

Counts hashable items. `most_common()` returns the top entries.

```python
from collections import Counter

counts = Counter('mississippi')
print(counts)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(counts['s'])  # 4
print(counts['z'])  # 0, missing items count as zero
print(counts.most_common(2))  # [('i', 4), ('s', 4)]
```

## defaultdict

A dict that creates a missing value on first access, so you don't need to check `if key in d`.

```python
from collections import defaultdict

by_letter = defaultdict(list)
for word in ['apple', 'avocado', 'banana', 'blueberry', 'cherry']:
    by_letter[word[0]].append(word)

print(dict(by_letter))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

## deque

A double-ended queue with fast appends and pops at both ends. A list is slow at the front.

```python
from collections import deque

queue = deque(['a', 'b', 'c'])
queue.append('d')  # add right
queue.appendleft('z')  # add left
print(queue.popleft())  # z
print(queue.pop())  # d
print(queue)  # deque(['a', 'b', 'c'])

last_three = deque(maxlen=3)  # drops the oldest item when full
for n in range(6):
    last_three.append(n)
print(list(last_three))  # [3, 4, 5]
```

## namedtuple

A tuple whose fields also have names.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # 3 4
print(p)  # Point(x=3, y=4)

x, y = p  # still unpackable like a tuple
print(x + y)  # 7
```

!!! tip "namedtuple or dataclass?"
    Use `namedtuple` for small immutable records that should behave like tuples. For defaults, methods, and mutability, reach for a [dataclass](dataclasses.md).
