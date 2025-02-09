from groq import Groq


from config import global_settings


def get_groq_client() -> Groq:
    """
    Initializes and returns a Groq client instance using the provided API key.

    This function creates a Groq client configured with the API key stored in global settings.

    :return: An instance of the Groq client configured with the API key.
    """
    return Groq(api_key=global_settings.GROQ_API_KEY)