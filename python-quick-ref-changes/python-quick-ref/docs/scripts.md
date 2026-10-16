# Scripts & CLI

Turn code into a program you run from the terminal: an entry point, command-line arguments, and exit codes.

## The `__main__` guard

A file can be both imported and run. Code under `if __name__ == '__main__':` runs only when the file is executed directly, not when it is imported.

```python
def main():
    print('running as a script')


if __name__ == '__main__':
    main()
```

## sys.argv

`sys.argv` is the raw list of command-line words; the first item is the script name. It's fine for tiny scripts.

```python
import sys

print(sys.argv[1:])  # arguments after the script name, e.g. python hi.py a b -> ['a', 'b']
```

## argparse

`argparse` parses arguments, validates them, and generates `--help` for free.

```python
import argparse


def build_parser():
    parser = argparse.ArgumentParser(description='Greet someone.')
    parser.add_argument('name', help='who to greet')  # positional, required
    parser.add_argument('--times', type=int, default=1, help='repeat count')
    parser.add_argument('--shout', action='store_true', help='use upper case')
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    message = f'Hello, {args.name}!'
    if args.shout:
        message = message.upper()
    for _ in range(args.times):
        print(message)
    return 0


main(['Aleks', '--times', '2', '--shout'])
# HELLO, ALEKS!
# HELLO, ALEKS!
```

From a terminal that would be `python greet.py Aleks --times 2 --shout`.

!!! tip "Accept `argv` as a parameter"
    Giving `main()` an optional `argv` list (as above) lets you test it by calling `main(['Aleks'])` instead of faking the command line.

## Exit codes

A program reports success or failure to the shell through its exit code: `0` means success, anything else means failure. Use `sys.exit()` to stop with a code.

```python
import sys

if __name__ == '__main__':
    sys.exit(main())  # 0 on success; a non-zero return value signals failure
```

`sys.exit('message')` prints the message to stderr and exits with code `1`. It works by raising `SystemExit`, so `finally` blocks and [context managers](context-managers.md) still run on the way out.

!!! tip "quit() vs sys.exit()"
    `quit()` and `exit()` are REPL helpers. In scripts, always use `sys.exit()` with a status code (`0` for success).

## Environment variables

Configuration such as API keys belongs in environment variables, not in the source code.

```python
import os

home = os.environ.get('HOME', 'unknown')
debug = os.environ.get('DEBUG', '0') == '1'
print(type(debug).__name__)  # bool
```

!!! warning "Gotcha: `os.environ['X']` raises `KeyError`"
    Use `os.environ.get('X', default)` unless the variable is truly required.
