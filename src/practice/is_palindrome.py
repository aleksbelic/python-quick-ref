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