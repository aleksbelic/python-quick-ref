# Text & Encoding

What a string really is, how text becomes bytes, and why "it works on my machine" breaks when files cross computers.

## Characters, code points, bytes

Three layers are easy to mix up:

| Layer | What it is | Python type |
| --- | --- | --- |
| **Code point** | a number that Unicode assigns to a character, written `U+00E9` | one item of a `str` |
| **Encoding** | a rule that turns code points into bytes (UTF-8, UTF-16, Latin-1...) | `str.encode()` / `bytes.decode()` |
| **Bytes** | the raw `0–255` values stored in a file or sent over a network | `bytes` |

A Python `str` is a sequence of **Unicode code points**. A `bytes` object is a sequence of **byte values**. They are different types, and you convert between them deliberately.

```python
text = 'é'
data = text.encode('utf-8')
print(data)                  # b'\xc3\xa9'  (2 bytes for 1 character)
print(data.decode('utf-8'))  # é
print(ord('é'), chr(233))    # 233 é
```

## UTF-8

UTF-8 is the encoding to use unless you have a specific reason not to. It is variable-length (1–4 bytes per code point), backward-compatible with ASCII, and the default for source files, the web, and JSON. Other encodings you will see are UTF-16 (common on Windows internals), Latin-1 (`latin-1`, one byte per character, 256 characters only), and legacy Windows code pages such as `cp1252`.

Encoding with the wrong rule gives garbled text (*mojibake*) or an error:

```python
print('é'.encode('latin-1'))   # b'\xe9'
try:
    b'\xe9'.decode('utf-8')
except UnicodeDecodeError as error:
    print(type(error).__name__)  # UnicodeDecodeError
```

`encode()` and `decode()` accept an `errors=` policy: `'strict'` (raise, the default), `'replace'` (insert a substitute character), `'ignore'` (drop). Silent policies hide data loss, so use them only when losing data is acceptable.

## Where encodings sneak in

Any time text crosses the boundary of your program it must be encoded or decoded: reading and writing files, network traffic, subprocess output, environment variables. The risk is relying on a *default*. Before Python 3.15 the default for `open()` came from the operating system's locale, so the same program could read a file correctly on Linux and fail on Windows. Python 3.15 changed the default to UTF-8 everywhere; passing `encoding='utf-8'` explicitly is still the portable habit ([Files & Paths](files.md)).

!!! tip "The Unicode sandwich"
    Decode bytes to `str` as soon as data enters your program, work with `str` internally, and encode back to bytes only on the way out.

## `len()` counts code points, not what you see

One visible "character" can be several code points: `é` can be a single code point (`U+00E9`) or `e` plus a combining accent (`U+0065 U+0301`). Emoji built from several parts are longer still.

```python
import unicodedata

a = '\u00e9'      # é as one code point
b = 'e\u0301'     # e + combining accent
print(len(a), len(b))   # 1 2
print(a == b)           # False, though they look identical
print(unicodedata.normalize('NFC', b) == a)  # True
```

**Normalization** (`NFC`, `NFD`) converts text to a canonical form so equivalent strings compare equal. Normalize before comparing or storing user-entered text.

For case-insensitive comparison use `casefold()` instead of `lower()`: it follows Unicode rules, so `'straße'.casefold() == 'STRASSE'.casefold()` is `True`.

## Source code and identifiers

Python source is UTF-8 by default, so string literals can contain any language, and you can write `'\u00e9'` or `'\N{LATIN SMALL LETTER E WITH ACUTE}'` when you want to be explicit. Identifiers may contain letters from other scripts, but ASCII names keep code easier to share.

## `str` versus `bytes` in practice

- File opened in **text mode** (`'r'`, `'w'`): you get `str`, decoding/encoding with the `encoding` you pass.
- File opened in **binary mode** (`'rb'`, `'wb'`): you get `bytes`, with no decoding at all (images, archives, PDFs).
- Mixing the two (`'a' + b'b'`) raises `TypeError`.
- `bytearray` is the mutable counterpart of `bytes`.
