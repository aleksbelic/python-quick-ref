# Concurrency

Doing several things "at once": the vocabulary, the three models Python offers (threads, processes, `asyncio`), the Global Interpreter Lock, and how to choose.

## Concurrency vs parallelism

- **Concurrency**: structuring a program so several tasks *make progress* in overlapping time. They may take turns on a single CPU core.
- **Parallelism**: tasks literally *run at the same instant* on different CPU cores.

Concurrency helps when a program **waits**; parallelism helps when it **computes**. So the first question is always: what is the bottleneck?

| Workload | Time is spent on... | Typical examples |
| --- | --- | --- |
| **I/O-bound** | waiting for disk, network, databases | web requests, reading many files |
| **CPU-bound** | calculating | image processing, number crunching, parsing huge data |

## The Global Interpreter Lock (GIL)

In standard CPython, a lock called the GIL ensures only **one thread executes Python bytecode at a time**. It protects the interpreter's internal bookkeeping (reference counts, see [How Python Works](how-python-works.md#memory-management)) and keeps single-threaded code fast, but has a major consequence:

- threads **can** overlap while waiting for I/O, because the GIL is released during blocking calls (and in many C extensions);
- threads **cannot** speed up pure-Python CPU work, since only one runs at a time.

There is movement on this front. Python 3.13 introduced an experimental **free-threaded** build without the GIL, and in 3.14 it became officially supported as an optional build. Python 3.15 continues the work (for example, official macOS installers now include free-threading support). The standard build still has the GIL, and libraries must be compatible, so check what your environment really uses before relying on it.

## The three models

| Model | Module | Runs as | Best for | Cost |
| --- | --- | --- | --- | --- |
| **Threads** | `threading`, `concurrent.futures.ThreadPoolExecutor` | several threads, one process | I/O-bound work | shared memory → race conditions |
| **Processes** | `multiprocessing`, `concurrent.futures.ProcessPoolExecutor` | separate interpreters, each with its own GIL | CPU-bound work | startup time; data must be copied (pickled) between processes |
| **`asyncio`** | `asyncio` | one thread, cooperative tasks | many simultaneous I/O waits (thousands of connections) | needs `async`-aware libraries; one blocking call stalls everything |

Threads are scheduled by the operating system and can be interrupted at almost any moment. `asyncio` tasks are scheduled by an **event loop** and give up control *only* at `await`, which makes them easier to reason about but dependent on every task cooperating.

## async / await

`async def` defines a **coroutine**; `await` pauses it until something it waits for is ready, letting the event loop run other tasks meanwhile.

```python
import asyncio


async def fetch(name, delay):
    await asyncio.sleep(delay)      # stands in for network I/O
    return f'{name} done'


async def main():
    async with asyncio.TaskGroup() as group:   # 3.11+: structured concurrency
        first = group.create_task(fetch('a', 1))
        second = group.create_task(fetch('b', 1))
    print(first.result(), second.result())     # both finish in ~1s, not 2s


asyncio.run(main())
```

A `TaskGroup` waits for all its tasks and, if several fail, raises an [`ExceptionGroup`](try-except.md#exception-groups-and-except).

## Shared state and race conditions

When several threads change the same data, the result can depend on timing. Even `counter += 1` is **not atomic**: it reads, adds, and writes back in separate steps, and another thread can slip in between, losing an update.

Defences, in order of preference:

1. **Avoid sharing.** Pass data in, return results out, give each worker its own copy.
2. **Pass messages** through a thread-safe `queue.Queue` instead of touching shared variables.
3. **Lock** the critical section (`with lock:`; see [Context Managers](context-managers.md)), keeping it as short as possible.

Locking carries its own hazard, **deadlock**: two threads each hold one lock and wait forever for the other's. Acquire locks in a consistent order, or avoid needing more than one.

## Choosing

```text
waiting on I/O, a few dozen tasks      → threads (ThreadPoolExecutor)
waiting on I/O, thousands of tasks     → asyncio
heavy computation                      → processes (ProcessPoolExecutor), or a library
                                          that releases the GIL (NumPy), or free-threading
one task, simple script                → none of the above
```

`concurrent.futures` offers the same simple interface (`submit`, `map`, futures) for threads and processes, which makes switching between them cheap. Python 3.14 also added `concurrent.interpreters` for running multiple isolated interpreters in one process.

!!! warning "Gotcha: more workers is not always faster"
    Concurrency adds overhead. If the tasks are tiny or the machine has few cores, a plain loop can win. Measure ([Complexity & Patterns](complexity.md)).
