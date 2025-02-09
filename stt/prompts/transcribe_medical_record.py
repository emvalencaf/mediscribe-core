def get_stt_prompt() -> str:
    """
    Returns the prompt for the speech-to-text model.

    This prompt is used to guide the transcription model to recognize that a medical consultation is being dictated.

    :return: A string containing the prompt for the transcription model.
    """
    return "Médico ditando a consulta médica"
