from typing import Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_core.messages import BaseMessage

from langchain_groq import ChatGroq


from config import global_settings

def get_llm_settings() -> Dict[str, str]:
    """
    Retrieves the settings for the large language model (LLM).

    :return: A dictionary containing the model URI, temperature, and max tokens.
    """
    return {
        "model": global_settings.LLM_MODEL_URI,
        "temperature": global_settings.LLM_TEMPERATURE,
        "max_tokens": global_settings.LLM_MAX_TOKENS
    }

def get_llm() -> ChatGroq:
    """
    Initializes and returns the ChatGroq instance with LLM settings.

    :return: An instance of the ChatGroq model, configured with the settings.
    """
    settings = get_llm_settings()
    
    return ChatGroq(api_key=global_settings.GROQ_API_KEY, **settings)

def get_model(prompt_template: ChatPromptTemplate) -> RunnableSerializable[dict, BaseMessage]:
    """
    Initializes a model using the provided prompt template and LLM settings.

    :param prompt_template: A template used for formatting the prompts.
    :return: A model that combines the prompt template with the LLM for generating responses.
    """
    llm = get_llm()
    
    return prompt_template | llm