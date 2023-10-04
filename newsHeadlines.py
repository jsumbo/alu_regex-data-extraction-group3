import re

# Sample API response containing news headlines
api_response = """
Breaking News: Earthquake in Region A
Latest Sports: Football Finals this Weekend
Entertainment Update: New Movie Release
Invalid Format Headline
Invalid:Format:Headline
"""

headline_pattern = r'([^:]+): (.+)'

matches = re.findall(headline_pattern, api_response)

for match in matches:
    headline, subheader = match[0], match[1]
    print(f"{headline}: {subheader}")
