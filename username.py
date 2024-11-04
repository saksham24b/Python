import re

url = input("URL: ").strip()
if matches := re.search(r".com/([^/]+)", url):
    print(f"Twitter username: @{matches.group(1)}")