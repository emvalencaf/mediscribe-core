from typing import Tuple
from langchain_core.prompts import ChatPromptTemplate

def get_system_role() -> Tuple[str, str]:
    """
    Returns the system role for the AI assistant in a healthcare setting.

    The system role instructs the AI to act as a helpful virtual assistant for healthcare professionals.

    :return: A tuple containing the role name ("system") and the system's role description.
    """
    
    return ("system", "Você é um assistente virtual da área de saúde útil e prestativa, sua tarefa é assistir ao profissional de saúde.")

def get_user_role() -> Tuple[str, str]:
    """
    Returns the user role for generating a medical record based on transcription.

    The user role provides detailed instructions on how to transcribe the medical consultation
    into a medical record in markdown format.

    :return: A tuple containing the role name ("human") and the user role description with formatting guidelines.
    """
    
    return ("human", """
            A sua tarefa é gerar um prontuário médico com base na transcrição da consulta.
            
            Análise cuidadosamente os detalhes, e leve o tempo necessário para pensar em como transcrever a consulta médica.
            
            Caso não tenha entendido algo da transcrição, afirme que não foi possível compreender X e destaque (com markdown) o que não foi capaz de compreender.
            
            A sua saída deve ser em markdown conforme o exemplo fornecido.
            
            Exemplo:
            # Dados da consulta
            
            | nome | idade | gênero | queixa principal | data consulta |
            | - | - | - | - | - |
            | <nome> | <idade> | <gênero> | <queixa principal> | <data da consulta> |
            
            # História da doença atual (HDA)
            <relato do paciente>
            # Antecedentes pessoais
            <antecedentes do paciente, histórico de doença, histórico familiar>.
            # Exame físico
            <descrever o exame físico>
            # Hipóteses diagnósticas:
            <descrever as hipóteses, listar>
            # Conduta
            <listar e descrever condutas>      
            # Impressão
            <impressões do médico em relação ao estado do paciente>
            
            Transcrição:
            {transcription}
            Prontuário:      
            """)

def get_chat_prompt_template() -> ChatPromptTemplate:
    """
    Creates and returns a ChatPromptTemplate instance based on the system and user roles.

    This function fetches the system role and user role, then uses them to create
    a prompt template to be used by the model.

    :return: An instance of ChatPromptTemplate created from the system and user roles.
    """
    system_role = get_system_role()
    user_role = get_user_role()

    return ChatPromptTemplate.from_messages(
        [system_role, user_role]
    )
