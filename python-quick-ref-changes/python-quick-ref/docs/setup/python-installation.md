# Python Installation

This reference assumes a reasonably recent Python — `3.11` or newer is a good baseline (the build tooling for this site needs it, and several lessons mention features from 3.10 onwards). Check what you have first:

```
python3 --version
```

!!! tip "`python` vs `python3`"
    On Linux and macOS, `python` may not exist or may point to an old Python 2. Always use `python3` (and `pip3`) unless you've verified otherwise.

## Windows

Download the installer from [python.org/downloads](https://www.python.org/downloads/). During installation, tick **Add python.exe to PATH**, then verify in a new terminal:

```
py --version
```

## Linux

Install via your package manager, for example on Debian/Ubuntu:

```
sudo apt install python3
```

!!! warning "Gotcha: distro Python can be old"
    Long-term-support distributions ship the Python version that was current when they were released, which may be older than 3.11. Check with `python3 --version`. If it is too old, use [uv](tooling.md#uv) or your distribution's newer-Python packages rather than replacing the system Python (system tools depend on it).

Then verify:

```
python3 --version
```

## macOS

Download the installer from [python.org/downloads](https://www.python.org/downloads/), or via Homebrew:

```
brew install python
```

Then verify:

```
python3 --version
```

## Or let `uv` install it

[uv](https://docs.astral.sh/uv/) can download and manage Python versions for you on any operating system — see [Tooling](tooling.md#uv).

```
uv python install 3.11
```

## Check pip

Python ships with pip, but confirm it's there and up to date:

```
python3 -m pip --version
python3 -m pip install --upgrade pip
```

!!! tip "Next step"
    Once Python is installed, create an isolated [Virtual Env](virtual-env.md) before installing any packages.
