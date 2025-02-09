from typing import Dict, Any
from stt.client import get_groq_client
from config import global_settings
from stt.prompts.transcribe_medical_record import get_stt_prompt
from helpers.load_file import load_txt_file

def start_transcription(filename: str) -> Dict[str, Any]:
    """
    Starts the transcription process by sending an audio file to the Groq API for transcription.

    This function reads an audio file, sends it to the Groq API for transcription, and saves
    the transcription result into a text file.

    :param filename: The path to the audio file to be transcribed.
    :return: A dictionary containing the transcription result from the Groq API.
    """
    client = get_groq_client()
    
    prompt = get_stt_prompt()
    
    with open(filename, "rb") as file:    
        transcription = client.audio.transcriptions.create(
                file=file,
                model=global_settings.STT_MODEL_URI,
                response_format="text",
                prompt=prompt,
                language="pt",
                temperature=0.0
            )
    
    print("transcription: ", transcription)
    
    load_txt_file(transcription,
                  "transcription.txt")
    
    return transcription
