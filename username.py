import re

url = input("URL: ").strip()
if matches := re.search(r".[com|net|in|org]/([a-z0-9_]+)", url):
    print(f"Twitter username: @{matches.group(1)}")