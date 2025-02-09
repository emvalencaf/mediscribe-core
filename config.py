from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from os import getenv
from typing import Optional

load_dotenv(dotenv_path='./.env')


class GlobalConfig(BaseSettings):
    """
    A configuration class to manage application settings using environment variables.

    This class uses Pydantic's `BaseSettings` to automatically read and validate
    environment variables. It includes settings for API versioning, Groq API key,
    speech-to-text and language model URIs, and backend/frontend configurations.

    Attributes:
        API_PREFIX_STR (str): The API prefix for routes.
        API_V_STR (str): The version of the API.
        GROQ_API_KEY (str): The API key for accessing Groq services.
        LLM_MODEL_URI (str): The URI of the language model to be used.
        LLM_MAX_TOKENS (int): The maximum number of tokens allowed for the language model.
        LLM_TEMPERATURE (int): The temperature setting for the language model.
        STT_MODEL_URI (str): The URI of the speech-to-text model.
        BACKEND_PORT (int): The port where the backend server will run.
        BACKEND_HOST (str): The host for the backend server.
        FRONTEND_URL (str): The URL of the frontend application.
    """
    
    API_PREFIX_STR: str = "/api"
    API_V_STR: str = getenv("API_V_STR", "v1")

    GROQ_API_KEY: str = getenv("GROQ_API_KEY")
    
    if not GROQ_API_KEY:
        raise ValueError("You must provide a GROQ API key for running this app...")
    
    LLM_MODEL_URI: str = getenv("LLM_MODEL_URI", "llama-3.3-70b-versatile")
    LLM_MAX_TOKENS: int = int(getenv("LLM_MAX_TOKENS", 1080))
    LLM_TEMPERATURE: int = int(getenv("LLM_TEMPERATURE", 0))
    
    STT_MODEL_URI: str = getenv("STT_MODEL_URI", "whisper-large-v3-turbo")
    
    BACKEND_PORT: int = int(getenv("BACKEND_PORT", 8000))
    BACKEND_HOST: str = getenv("BACKEND_HOST", "localhost")
    
    FRONTEND_URL: str = getenv("FRONTEND_URL", "http://localhost:6000")
    
    class Config:
        case_sensitive = True

        
        
global_settings: GlobalConfig = GlobalConfig()