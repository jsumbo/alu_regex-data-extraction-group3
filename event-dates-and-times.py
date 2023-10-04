#!/usr/bin/python3
# Creating a  regular expression that prints Event dates/times follow the pattern "MMM DD, YYYY - hh:mm AM/PM" with standard date and 12-hour time formatting.
import re
pattern = r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2},\s\d{4}\s-\s\d{2}:\d{2}\s(?:AM|PM)\b'

text = "Most awaited event  Dec 15, 2023 - 11:59 PM"
matches = re.findall(pattern, text)

for match in matches:
    print(match)
