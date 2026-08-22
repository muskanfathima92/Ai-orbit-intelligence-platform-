import json


class MockLLMClient:

    def extract(self, system_prompt, user_prompt):

        data = json.loads(user_prompt)

        tool = data["tool_data"]

        return {
            "name": tool.get("name"),
            "description": tool.get("description"),
            "url": tool.get("url"),
            "categories": (
                [tool["category"]]
                if tool.get("category")
                else []
            ),
            "source": {
                "name": data["source"]["name"],
                "url": data["source"]["url"]
            }
        }