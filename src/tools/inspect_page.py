import requests
from bs4 import BeautifulSoup


URL = "https://opentools.ai/tools/nymos"

headers = {
    "User-Agent": "Mozilla/5.0"
}


# Download the page
response = requests.get(
    URL,
    headers=headers,
    timeout=20
)

print("Status:", response.status_code)

response.raise_for_status()


# Parse HTML
soup = BeautifulSoup(
    response.text,
    "html.parser"
)


# Find the exact text "Utilities"
element = soup.find(
    string=lambda s:
    s and s.strip() == "Utilities"
)


if element:

    print("\nFOUND CATEGORY!")

    print("\nText:")
    print(element.strip())

    print("\nParent HTML:")
    print(
        element.parent.prettify()
    )

    print("\nGrandparent HTML:")
    print(
        element.parent.parent.prettify()
    )

else:

    print(
        "\nUtilities was not found."
    )