class LLMClient:

    def extract(self, system_prompt, user_prompt):
        """
        Send data to the configured LLM
        and return structured JSON.

        This method will be connected to the
        team's chosen LLM provider later.
        """

        raise NotImplementedError(
            "LLM provider is not configured yet."
        )