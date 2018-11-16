# kalliope_yandextts

Yandex text to speech for kalliope


Shamelessly inspired from https://github.com/SpawNBK/kalliope_yandextts


## Synopsis

Kalliope speaking from yandex


## Installation

  ```
  kalliope install --git-url https://github.com/SpawNBK/kalliope_yandextts.git
  ```
  after install tts you need do small operation:
   - open file /usr/local/lib/python2.7/dist-packages/yandex_speech/tts.py in texteditor
   - replace line 'extension = "." + self.__params["format"]' to 'extension = ".tts"'

## Notes

speakers: Speaker. Female: "jane", "oksana", "alyss", "omazh". Male: "zahar", "ermil"

in settings.yml do:

default_text_to_speech: "yandextts"

text_to_speech:
  - yandextts:
      language: "ru-RU"
      speaker: "alyss"
      key: "secret key"
