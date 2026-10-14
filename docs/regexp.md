# Regular Expressions

Match and transform text patterns with the `re` module.

## search()

Returns a `Match` object for the first match anywhere in the string, or `None`.

```python
import re

# search - returns a Match object if there is a match anywhere in the string
matches = re.search("^The.*Spain$", "The rain in Spain")
print(matches)
#<re.Match object; span=(0, 17), match='The rain in Spain'>

if matches is not None:
    print(matches[0])
    #The rain in Spain
```

## sub()

Replaces matches with a string. `\s` matches any whitespace.

```python
text = "The rain in Spain"

new_text2 = re.sub("Spain", "Italy", text)
print(new_text2)
#The rain in Italy

new_text3 = re.sub('\\s', "-", text)
print(new_text3)
#The-rain-in-Spain
```

!!! tip "Guard the Match"
    `re.search()` returns `None` when nothing matches. Always check for `None` before indexing the result.
