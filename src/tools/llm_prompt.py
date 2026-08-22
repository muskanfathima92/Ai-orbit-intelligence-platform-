SYSTEM_PROMPT = """
You are a data extraction system for AI Orbit.

Extract structured information about an AI tool from the provided
source content.

Return ONLY valid JSON.

Required fields:
- name
- description
- url
- categories
- source

Rules:
1. Do not invent information.
2. Use only information present in the source.
3. Keep the original tool name.
4. Keep the description concise and factual.
5. If a field is unavailable, return null or an empty array.
6. categories must be an array of strings.
7. source must contain name and url.
"""


def build_prompt(tool_data):

    return f"""
Extract the AI tool information from this data:

Name:
{tool_data.get("name")}

Description:
{tool_data.get("description")}

Tool URL:
{tool_data.get("tool_url")}

OpenTools Category:
{tool_data.get("category")}

Keywords:
{tool_data.get("keywords")}

Source:
OpenTools

Source URL:
{tool_data.get("opentools_url")}
"""