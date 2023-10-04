import re

def extract_ingredients(api_response):
    pattern = r'([a-zA-Z\s]+)'
    matches = re.findall(pattern, api_response)
    return matches