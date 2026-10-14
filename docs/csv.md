# CSV

Read and write comma-separated files with the `csv` module.

## Reading rows

`csv.reader` yields each row as a list. Unpack it into variables.

```python
import csv

# Reading from a CSV file:
with open('./data/user-data.csv') as my_csv_file:
    csv_reader = csv.reader(my_csv_file)
    for row in csv_reader:
        name, email, age = row
        print(f'Name: {name}, Email: {email}, Age: {age}')
```

## Skipping a header row

Call `next()` once on the reader to skip the header line.

```python
# Reading from a CSV file with a header row & skipping it:
with open('./data/user-data-with-header.csv') as my_csv_file_with_header:
    csv_reader = csv.reader(my_csv_file_with_header)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        name, email, age = row
        print(f'Name: {name}, Email: {email}, Age: {age}')
```

## Reading with DictReader

`DictReader` uses the header row as keys, so columns are accessed by name.

```python
# Reading from a CSV file with a header row & DictReader:
with open('./data/user-data-with-header.csv') as my_csv_file_with_header:
    csv_dict_reader = csv.DictReader(my_csv_file_with_header)  # type: ignore
    for user_row in csv_dict_reader:
        print(f'Name: {user_row["name"]}, Email: {user_row["email"]}, Age: {user_row["age"]}')
```

## Writing with DictWriter

Pass `fieldnames`, write the header first, then the rows.

```python
# Writing to a CSV file from a list of dictionaries:
some_user_data = [
    {'name': 'David', 'email': 'david@example.com', 'age': 30},
    {'name': 'Eva', 'email': 'eva@example.com', 'age': 22},
    {'name': 'Frank', 'email': 'frank@example.com', 'age': 27},
]
with open('./data/write-user-data.csv', 'w') as write_user_data_csv_file:
    csv_dict_writer = csv.DictWriter(write_user_data_csv_file, fieldnames=['name', 'email', 'age'])
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(some_user_data)
```

!!! tip "Paths are relative to where you run"
    `'./data/...'` resolves against the working directory, so run the script from `src/theory/` where the `data/` folder lives. For a script that works from anywhere, resolve paths from `__file__` instead:

    ```python
    from pathlib import Path

    DATA_DIR = Path(__file__).parent / "data"
    ```

!!! tip "reader vs DictReader"
    Use `reader` for simple positional data. Use `DictReader` / `DictWriter` when the file has a header row and you want name-based access.
