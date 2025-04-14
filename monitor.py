import requests
from datetime import datetime

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.nonexistentwebsite.fake"
]

def check_websites():
    for site in websites:
        try:
            response = requests.get(site, timeout=5)
            status = "UP" if response.status_code == 200 else f"DOWN ({response.status_code})"
        except requests.exceptions.RequestException as e:
            status = f"DOWN (Error: {e})"

        print(f"{datetime.now()} - {site} is {status}")

if __name__ == "__main__":
    check_websites()
