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