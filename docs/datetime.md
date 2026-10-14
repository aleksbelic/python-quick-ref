# Dates & Times

The `datetime` module handles dates, times, and durations.

## Creating dates and datetimes

```python
from datetime import date, datetime, timedelta

d = date(2026, 1, 15)
dt = datetime(2026, 1, 15, 13, 45, 30)

print(d)  # 2026-01-15
print(dt)  # 2026-01-15 13:45:30
print(d.year, d.month, d.day)  # 2026 1 15
print(d.weekday())  # 3, Monday is 0
```

The current moment:

```python
today = date.today()
now = datetime.now()
print(type(now).__name__)  # datetime
```

## Arithmetic with timedelta

Subtracting two dates gives a `timedelta`. You can add a `timedelta` to a date.

```python
deadline = date(2026, 3, 1)
print(deadline - d)  # 45 days, 0:00:00
print((deadline - d).days)  # 45

print(d + timedelta(days=30))  # 2026-02-14
print(dt - timedelta(hours=2))  # 2026-01-15 11:45:30
```

## Formatting with strftime

`strftime()` turns a datetime into text using format codes.

```python
print(dt.strftime('%Y-%m-%d'))  # 2026-01-15
print(dt.strftime('%d.%m.%Y %H:%M'))  # 15.01.2026 13:45
print(dt.strftime('%A, %B %d'))  # Thursday, January 15
```

| Code | Meaning | Code | Meaning |
| --- | --- | --- | --- |
| `%Y` | 4-digit year | `%H` | hour (24h) |
| `%m` | month `01`-`12` | `%M` | minute |
| `%d` | day `01`-`31` | `%S` | second |
| `%A` | weekday name | `%B` | month name |

## Parsing text

`strptime()` parses text with a format. For ISO 8601 text, `fromisoformat()` is simpler.

```python
parsed = datetime.strptime('15.01.2026 13:45', '%d.%m.%Y %H:%M')
print(parsed)  # 2026-01-15 13:45:00

print(dt.isoformat())  # 2026-01-15T13:45:30
print(datetime.fromisoformat('2026-01-15T13:45:30') == dt)  # True
```

## Time zones

A *naive* datetime has no time zone; an *aware* one does. Store and compute in UTC, convert to local time only for display.

```python
from datetime import timezone
from zoneinfo import ZoneInfo

utc_time = datetime(2026, 1, 15, 12, 0, tzinfo=timezone.utc)
print(utc_time)  # 2026-01-15 12:00:00+00:00

belgrade = utc_time.astimezone(ZoneInfo('Europe/Belgrade'))
print(belgrade)  # 2026-01-15 13:00:00+01:00
```

!!! warning "Gotcha: naive and aware datetimes don't mix"
    Comparing or subtracting a naive and an aware datetime raises `TypeError`. Make everything aware (`datetime.now(timezone.utc)`) or everything naive — don't mix.

!!! tip "On Windows"
    `zoneinfo` needs time zone data that Windows doesn't ship. Install it with `python -m pip install tzdata`.
