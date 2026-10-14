# Files & Paths

Read and write files with `open()`, and build paths with `pathlib`.

## Writing a file

Open with mode `'w'` (write, truncates the file) or `'a'` (append). Always use `with` so the file is closed even if an error occurs, and pass an `encoding`.

```python
with open('notes.txt', 'w', encoding='utf-8') as file:
    file.write('first line\n')
    file.write('second line\n')

with open('notes.txt', 'a', encoding='utf-8') as file:
    file.write('third line\n')
```

## Reading a file

`read()` returns the whole content as one string. Iterating over the file yields one line at a time — the right choice for big files.

```python
with open('notes.txt', encoding='utf-8') as file:
    content = file.read()
print(content)

with open('notes.txt', encoding='utf-8') as file:
    for line in file:
        print(line.rstrip('\n'))
```

Other options: `readline()` reads one line, `readlines()` returns a list of lines.

## File modes

| Mode | Meaning |
| --- | --- |
| `'r'` | read (default); error if the file doesn't exist |
| `'w'` | write; creates the file or **erases** an existing one |
| `'a'` | append to the end |
| `'x'` | create; error if the file already exists |
| `'b'` | add to another mode for binary data: `'rb'`, `'wb'` |

## pathlib

`Path` objects are the modern way to work with file system paths. Join with `/` — it works on every operating system.

```python
from pathlib import Path

folder = Path('reports') / '2026'
folder.mkdir(parents=True, exist_ok=True)

file_path = folder / 'summary.txt'
file_path.write_text('all good\n', encoding='utf-8')
print(file_path.read_text(encoding='utf-8'))  # all good

print(file_path.name)  # summary.txt
print(file_path.stem)  # summary
print(file_path.suffix)  # .txt
print(file_path.parent)  # reports/2026
print(file_path.exists())  # True
```

## Listing files

```python
for path in sorted(Path('reports').glob('**/*.txt')):  # ** searches sub-folders
    print(path)  # reports/2026/summary.txt

for entry in sorted(Path('.').iterdir()):
    kind = 'dir' if entry.is_dir() else 'file'
    print(kind, entry.name)
```

## Paths relative to the script

A relative path like `'data/file.csv'` resolves against the **working directory** — wherever you launched Python from. To find files next to your script no matter where it is run from, start from `__file__`.

```python
BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / 'data' / 'user-data.csv'
print(data_file.exists())  # True when the file sits next to the script
```

## Handling missing files

```python
try:
    Path('missing.txt').read_text(encoding='utf-8')
except FileNotFoundError:
    print('No such file')
```

!!! warning "Gotcha: `'w'` erases the file"
    Opening an existing file with `'w'` truncates it immediately — even if your code later fails. Use `'x'` to refuse to overwrite, or `'a'` to add.

!!! tip "Always pass `encoding='utf-8'`"
    Without it, Python uses the platform default (which differs between Windows and Linux/macOS) and non-ASCII text can break.
