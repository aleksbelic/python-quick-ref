# Python Installation

You need Python `3.11` or newer for this project (required by dependencies). Check what you have first:

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

## Check pip

Python ships with pip, but confirm it's there and up to date:

```
python3 -m pip --version
python3 -m pip install --upgrade pip
```

!!! tip "Next step"
    Once Python is installed, create an isolated [Virtual Env](virtual-env.md) before installing any packages.
