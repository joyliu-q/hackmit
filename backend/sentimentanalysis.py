import text2emotion as te
import json
import random


songs = {
    "happy": ["data/Bliss.mp3", "data/Island.mp3"],
    "sad": ["data/test.mp3"],
    "angry": ["data/test.mp3"],
    "surprise": ["data/test.mp3"],
    "fear":["data/test.mp3"],
    "neutral": ["data/test.mp3"]

}


test_data =[{'start': 120, 'end': 300, 'text': 'and then obama said'}]


def get_song_info(data):
    sentences = data.copy()
    song = None
    for i in range(len(sentences)):
        print(sentences[i])
        emotion = get_emotion(sentences[i]['text'])
        song = songs[emotion][random.randint(0, len(songs[emotion])- 1)]

    return {
            'start': sentences[i]['start'],
            'end': sentences[i]['start'],
            'song': song
        }



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

print(get_song_info(test_data))