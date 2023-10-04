import re

# Contains the regex search term
pattern = r'^[A-Z][A-Z][A-Z]\d{3}$'

# Contains the text being matched with regex
text = "ABC123"

# Matches the text with our regex search term
matches = re.findall(pattern, text)

# Prints matches found
for match in matches:
    print(match)