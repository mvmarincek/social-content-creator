import os
import base64
import tempfile
from typing import Optional
from agno.tools import Toolkit
from agno.utils.log import logger

try:
    import openai
except ImportError:
    raise ImportError("`openai` not installed. Please install using `pip install openai`")


class OpenAITTSTools(Toolkit):
    def __init__(
        self,
        voice: str = "alloy",
        model: str = "tts-1",
        target_directory: Optional[str] = None,
    ):
        super().__init__(name="openai_tts")
        self.voice = voice
        self.model = model
        self.target_directory = target_directory
        self.register(self.text_to_speech)
        self.register(self.get_voices)

    def get_voices(self) -> str:
        """Get list of available OpenAI TTS voices with descriptions.
        
        Returns:
            str: JSON string with available voices
        """
        voices = {
            "alloy": "Neutral and balanced voice, good for general content",
            "echo": "Warm and conversational male voice",
            "fable": "Expressive British accent, good for storytelling",
            "onyx": "Deep and authoritative male voice",
            "nova": "Friendly and energetic female voice, great for social media",
            "shimmer": "Soft and pleasant female voice"
        }
        return str(voices)

    def text_to_speech(self, text: str, voice: Optional[str] = None) -> str:
        """Convert text to speech using OpenAI TTS API.
        
        Args:
            text: The text to convert to speech
            voice: Optional voice to use (alloy, echo, fable, onyx, nova, shimmer)
            
        Returns:
            str: URL or path to the generated audio file
        """
        try:
            client = openai.OpenAI()
            
            selected_voice = voice or self.voice
            
            response = client.audio.speech.create(
                model=self.model,
                voice=selected_voice,
                input=text
            )
            
            if self.target_directory:
                os.makedirs(self.target_directory, exist_ok=True)
                file_path = os.path.join(self.target_directory, f"speech_{hash(text)}.mp3")
            else:
                tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
                file_path = tmp.name
                tmp.close()
            
            response.stream_to_file(file_path)
            
            with open(file_path, "rb") as f:
                audio_bytes = f.read()
                audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
            
            logger.info(f"Audio generated successfully: {file_path}")
            
            return f"Audio gerado com sucesso. Arquivo salvo em: {file_path}\nBase64 (primeiros 100 chars): {audio_base64[:100]}...\nVoz utilizada: {selected_voice}"
            
        except Exception as e:
            logger.error(f"Error generating audio: {e}")
            return f"Erro ao gerar audio: {str(e)}"
