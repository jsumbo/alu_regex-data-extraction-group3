import re

# Contains the regex search term
pattern = r'[a-zA-Z0-9._%+-]{1,}\@[a-z0-9-.]{1,}\.[a-z]{2,}'

# Contains the text being matched with regex
text = "My email address is name@domain.com"

# Matches the text with our regex search term
matches = re.findall(pattern, text)

# Prints matches found
for match in matches:
    print(match)