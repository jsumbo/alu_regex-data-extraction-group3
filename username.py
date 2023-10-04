import re

def extract_usernames(api_response):
    pattern = r'@(\w+)'
    matches = re.findall(pattern, api_response)
    return matches