### Overview

Simpe way to create a bot with Natural Language Understanding.
Bot using RASA NLU to answer different questions. Using Wikipedia as failover.
You can use Python 2 or Python 3.

### Install Package

```
pip3 install slackclient rasa_nlu scipy scikit-learn sklearn-crfsuite numpy spacy wolframalpha wikipedia
python3 -m spacy download en
```

### Run with Python 3

Install dependencies from Dockerfile and run:

```
python3 bot.py
```

### Run it with Docker

 - Wikipedia API.
 - Greet Answer.

```
docker build -t bot . && docker run bot
```

### RASA

Create initial intentions - https://rasahq.github.io/rasa-nlu-trainer/. During the Bot start we run training process based on `./modelDB/rasa-data.json` intentions. Later we work with messages we can parse, also Bot stores all unparsed messages so we can check them later.