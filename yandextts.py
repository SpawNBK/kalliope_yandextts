import requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from yandex_speech import TTS

from kalliope.core import FileManager
from kalliope.core.TTS.TTSModule import TTSModule, FailToLoadSoundFile, MissingTTSParameter
import logging


logging.basicConfig()
logger = logging.getLogger("kalliope")


class Yandextts(TTSModule):
    def __init__(self, **kwargs):
        super(Yandextts, self).__init__(**kwargs)

	self.speaker = kwargs.get('speaker', None)
        self.key = kwargs.get('key', None)
        self._check_parameters()

    def say(self, words):
        """
        :param words: The sentence to say
        """

        self.generate_and_play(words, self._generate_audio_file)

    def _check_parameters(self):
        """
        Check parameters are ok, raise MissingTTSParameterException exception otherwise.
        :return: true if parameters are ok, raise an exception otherwise

               .. raises:: MissingTTSParameterException
        """
        if self.language == "default" or self.language is None or self.key is None or self.speaker is None:
            raise MissingTTSParameter("[YandexTTS] Missing parameters, check documentation !")
        return True

    def _generate_audio_file(self):
        """
        Generic method used as a Callback in TTSModule
            - must provided the audio file and write it on the disk

        .. raises:: FailToLoadSoundFile
        """

        # Since the gTTS lib disabled the SSL verification we get rid of insecure request warning
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        tts = TTS(self.speaker,"mp3", self.key, self.language)
	tts.generate(text=self.words)
        
        # OK we get the audio we can write the sound file
        tts.save(self.file_path)
        
        # Re enable the warnings to avoid affecting the whole kalliope process 
        warnings.resetwarnings()
        
