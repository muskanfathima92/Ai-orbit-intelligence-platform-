from scraper import scrape_tool


URL = "https://opentools.ai/tools/nymos"


data = scrape_tool(URL)


if data:

    print("\n========== RESULT ==========\n")

    for key, value in data.items():

        print(
            f"{key}: {value}"
        )

else:

    print(
        "No tool data found."
    )