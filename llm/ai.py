from langchain_core.runnables import RunnableSerializable
from langchain_core.messages import BaseMessage

from llm.model import get_model
from llm.prompts.generate_medical_record import get_chat_prompt_template

def ai_medical_record() -> RunnableSerializable[dict, BaseMessage]:
    """
    Initializes and returns the AI model for generating medical records.

    :return: The AI model object used for processing prompts.
    """
    prompt_template = get_chat_prompt_template()
    
    return get_model(prompt_template=prompt_template)


def generate_medical_record(input: str) -> tuple:
    """
    Generates a medical record based on the provided transcription input.

    :param input: A string containing the transcription to be processed.
    :return: A tuple containing the content of the medical record and metadata about the response.
    """
    ai = ai_medical_record()
    
    res = ai.invoke(input={ "transcription": input })
    
    return res.content, res.response_metadata
