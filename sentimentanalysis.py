import text2emotion as te
import json
import random


songs = {
    "happy": ["Bliss.mp3", "Island.mp3"],
    "sad": ["test"],
    "angry": ["test"],
    "surprise": ["test"],
    "fear":["test"],
    "neutral": ["test"]

}


data = """[{
    "start": "1:00",
    "end": "3:00",
    "text": "testing then"
}]
"""

def get_song_info():
    sentences = json.loads(data)
    song = None
    for i in range(len(sentences)):
        print(sentences[i])
        emotion = get_emotion(sentences[i]['text'])
        song = songs[emotion][random.randint(0, len(songs[emotion]))]

    return song



def get_emotion(text):
    emotions = te.get_emotion(text)
    result = None
    highest = 0

    neutral = False

    for emotion in emotions:
        if emotions[emotion] > highest:
            result = emotion
            highest = emotions[emotion]
            neutral = False
        elif emotions[emotion] == highest:
            neutral = True

    if neutral:
        return "neutral"

    return result

print(get_song_info())