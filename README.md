# kalliope_yandextts

Yandex text to speech for kalliope


Shamelessly inspired from https://github.com/SpawNBK/kalliope_yandextts


## Synopsis

Kalliope speaking from yandex


## Installation

  ```
  kalliope install --git-url https://github.com/SpawNBK/kalliope_yandextts.git
  ```

## Notes

speakers: Speaker. Female: "jane", "oksana", "alyss", "omazh". Male: "zahar", "ermil"

in settings.yml do:

```yaml
default_text_to_speech: "yandextts"

text_to_speech:
  - yandextts:
      language: "ru-RU"
      speaker: "alyss"
      key: "secret key"
```

you can also use cache
```yaml
default_text_to_speech: "yandextts"

text_to_speech:
  - yandextts:
      language: "ru-RU"
      speaker: "alyss"
      key: "secret key"
      cache: True
```
