import re

url = input("URL: ").strip()
if matches := re.search(r".[com|net|in|org]/([^/]+)", url):
    print(f"Twitter username: @{matches.group(1)}")