import json
from pathlib import Path
import psycopg2


INPUT = Path(
    "data/tools/results/ai_orbit_tools_deduplicated.json"
)

DB = {
    "host": "localhost",
    "port": 5432,
    "database": "ai_orbit",
    "user": "postgres",
    "password": "muskan"
}


# Load validated JSON
with open(INPUT, "r", encoding="utf-8") as f:
    tools = json.load(f)


# Connect to PostgreSQL
connection = psycopg2.connect(**DB)
cursor = connection.cursor()


query = """
INSERT INTO tools
(
    id,
    entity_type,
    name,
    description,
    url,
    categories,
    source
)
VALUES
(
    %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb
)
ON CONFLICT (id)
DO UPDATE SET
    name = EXCLUDED.name,
    description = EXCLUDED.description,
    url = EXCLUDED.url,
    categories = EXCLUDED.categories,
    source = EXCLUDED.source;
"""


for tool in tools:

    cursor.execute(
        query,
        (
            tool["id"],
            tool["entity_type"],
            tool["name"],
            tool["description"],
            tool["url"],
            json.dumps(tool["categories"]),
            json.dumps(tool["source"])
        )
    )


connection.commit()

print(
    f"Successfully inserted {len(tools)} tools into PostgreSQL."
)


cursor.close()
connection.close()
