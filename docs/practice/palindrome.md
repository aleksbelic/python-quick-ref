# Palindrome

Check whether a string reads the same forward and backward, ignoring case and non-alphanumeric characters.

```python
def is_palindrome(word: str) -> bool:
    """
    Check if a given string is a palindrome (sequence of alphanumeric characters that reads the same forward and backward).

    Args:
        word (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    wordWithOnlyAlphanumericCharacters = ''.join(char.lower() for char in word if char.isalnum())
    return wordWithOnlyAlphanumericCharacters == wordWithOnlyAlphanumericCharacters[::-1]
```

```python
is_palindrome("A man, a plan, a canal: Panama!")  # True
is_palindrome("python")                            # False
```

!!! tip "The `[::-1]` trick"
    Slicing with a step of `-1` reverses any sequence — the idiomatic way to compare a string against its mirror.
