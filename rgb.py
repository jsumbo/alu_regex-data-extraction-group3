import re

def extract_rgb(api_response):
    pattern = r'rgb\((\d+), (\d+), (\d+)\)'
    matches = re.findall(pattern, api_response)
    return matches