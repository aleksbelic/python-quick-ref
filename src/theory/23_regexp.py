import re

# search - returns a Match object if there is a match anywhere in the string
matches = re.search("^The.*Spain$", "The rain in Spain") 
print(matches)
#<re.Match object; span=(0, 17), match='The rain in Spain'>

if matches is not None:
    print(matches[0])
    #The rain in Spain

print('---')

# sub - replaces one or many matches with a string
text = "The rain in Spain"

new_text2 = re.sub("Spain", "Italy", text)
print(new_text2)
#The rain in Italy

new_text3 = re.sub('\\s', "-", text)
print(new_text3)
#The-rain-in-Spain

print('---')
