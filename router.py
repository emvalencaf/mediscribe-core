from fastapi import APIRouter, File, UploadFile

from stt.services import start_transcription
from llm.ai import generate_medical_record as invoke_generate_medical_record
from helpers.load_file import load_file, load_txt_file

api_router = APIRouter()

@api_router.post("/generate_medical_record")
def generate_medical_record(file: UploadFile = File(...)):
    """
    Endpoint to generate a medical record based on an uploaded audio file.

    This endpoint handles the following steps:
    1. Uploads the file to the server.
    2. Transcribes the audio file into text.
    3. Generates a medical record from the transcription.
    4. Saves the result in a markdown file.
    
    :param file: The audio file to be uploaded and transcribed.
    :return: A dictionary containing the result of the medical record generation.
    """
    file_uri = load_file(file=file)
    
    transcription = start_transcription(file_uri)
    
    res = invoke_generate_medical_record(input=transcription)
    
    load_txt_file(content=res[0],
                  filename="result.md",
                  partition="medical_record")
    
    return {
        "result": {
            "transcription" : transcription,
            "medical_record" : res[0]
            },
        "metadata": {
            "llm_model_details": res[1], 
        },
    }