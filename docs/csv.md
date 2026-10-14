# CSV

Read and write comma-separated files with the `csv` module. The examples use these two files:

```csv title="data/user-data.csv"
Anna,anna@example.com,30
Ben,ben@example.com,22
Cleo,cleo@example.com,28
```

```csv title="data/user-data-with-header.csv"
name,email,age
Anna,anna@example.com,30
Ben,ben@example.com,22
Cleo,cleo@example.com,28
```

!!! note "The `data/` files are illustrative"
    These CSV files don't exist in the repo — save the contents above to matching paths to run the snippets below as-is.

!!! tip "Open CSV files with `newline=''`"
    The `csv` module handles line endings itself. Always open files with `newline=''` (and `encoding='utf-8'`) so quoted fields containing line breaks, and Windows line endings, work correctly.

## Reading rows

`csv.reader` yields each row as a list of strings. Unpack it into variables.

```python
import csv

with open('./data/user-data.csv', newline='', encoding='utf-8') as my_csv_file:
    csv_reader = csv.reader(my_csv_file)
    for row in csv_reader:
        name, email, age = row
        print(f'Name: {name}, Email: {email}, Age: {age}')
```

## Skipping a header row

Call `next()` once on the reader to skip the header line.

```python
with open('./data/user-data-with-header.csv', newline='', encoding='utf-8') as my_csv_file:
    csv_reader = csv.reader(my_csv_file)
    next(csv_reader)  # skip the header row
    for row in csv_reader:
        name, email, age = row
        print(f'Name: {name}, Email: {email}, Age: {age}')
```

## Reading with DictReader

`DictReader` uses the header row as keys, so columns are accessed by name.

```python
with open('./data/user-data-with-header.csv', newline='', encoding='utf-8') as my_csv_file:
    for user in csv.DictReader(my_csv_file):
        print(f'Name: {user["name"]}, Email: {user["email"]}, Age: {user["age"]}')
```

## Writing with DictWriter

Pass `fieldnames`, write the header first, then the rows.

```python
some_user_data = [
    {'name': 'David', 'email': 'david@example.com', 'age': 30},
    {'name': 'Eva', 'email': 'eva@example.com', 'age': 22},
    {'name': 'Frank', 'email': 'frank@example.com', 'age': 27},
]

with open('./data/write-user-data.csv', 'w', newline='', encoding='utf-8') as out_file:
    writer = csv.DictWriter(out_file, fieldnames=['name', 'email', 'age'])
    writer.writeheader()
    writer.writerows(some_user_data)
```

## Writing with writer

`csv.writer` writes plain lists. It quotes fields that contain commas for you.

```python
with open('./data/write-rows.csv', 'w', newline='', encoding='utf-8') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['name', 'note'])
    writer.writerow(['Ana', 'likes pizza, pasta'])  # comma is quoted automatically
```

## Numbers are strings

Every value comes back as a `str`. Convert what you need.

```python
with open('./data/user-data-with-header.csv', newline='', encoding='utf-8') as my_csv_file:
    ages = [int(row['age']) for row in csv.DictReader(my_csv_file)]

print(sum(ages) / len(ages))  # 26.666666666666668
```

!!! tip "Paths are relative to where you run"
    `'./data/...'` resolves against the working directory, so run the script from the folder that contains `data/`. For a script that works from anywhere, resolve paths from `__file__` — see [Files & Paths](files.md#paths-relative-to-the-script).

!!! tip "reader vs DictReader"
    Use `reader` for simple positional data. Use `DictReader` / `DictWriter` when the file has a header row and you want name-based access.

!!! tip "Bigger data?"
    For anything beyond simple files — grouping, joins, statistics — look at the third-party `pandas` library.
