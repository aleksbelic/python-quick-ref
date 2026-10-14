# Palindrome

Check whether a string reads the same forward and backward, ignoring case and non-alphanumeric characters.

```python
def is_palindrome(word: str) -> bool:
    """Check if a string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        word (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned = "".join(char.lower() for char in word if char.isalnum())
    return cleaned == cleaned[::-1]
```

```python
print(is_palindrome("A man, a plan, a canal: Panama!"))  # True
print(is_palindrome("python"))  # False
```

!!! tip "The `[::-1]` trick"
    Slicing with a step of `-1` reverses any sequence — the idiomatic way to compare a string against its mirror.
