import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


URL = "https://opentools.ai/tools"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    URL,
    headers=headers,
    timeout=20
)

print("Status:", response.status_code)
print("HTML length:", len(response.text))

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print("\n========== LINKS ==========\n")

links = soup.find_all("a", href=True)

print("Total links found:", len(links))

for link in links[:100]:

    text = link.get_text(
        " ",
        strip=True
    )

    href = link.get("href")

    print(
        "TEXT:",
        text[:80]
    )

    print(
        "HREF:",
        href
    )

    print("---")