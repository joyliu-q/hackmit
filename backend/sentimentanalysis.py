import text2emotion as te
import json
import random
import nltk
import os

from video_to_text import TranscriptSegment

songs = {
    "Happy": [],
    "Sad": [],
    "Angry": [],
    "Surprise": [],
    "Fear": [],
    "Neutral": []
}


test_data = [TranscriptSegment("I am happy", 0, 1), TranscriptSegment("I am sad", 1, 2), TranscriptSegment(
    "I am angry", 2, 3), TranscriptSegment("I am surprised", 3, 4), TranscriptSegment("I am afraid", 4, 5), TranscriptSegment("I am neutral", 5, 6)]


def populate_song():
    path = "./data/Songs"
    for key in songs:
        dir_list = os.listdir(os.path.join(path, key))
        dir_list = [os.path.join(path, key, file) for file in dir_list]
        print(dir_list)
        songs[key] = dir_list


def get_song_info(sentences):
    song = None
    output = []

    emotions = list(map(lambda x: get_emotion(x.text), sentences))

    populate_song()
    for i in range(len(sentences)):
        print(sentences[i])
        emotion = emotions[i]

        if i > 0 and emotions[i - 1] == emotion:
            output[len(output) - 1]['end'] = sentences[i].end_time
        else:
            song = songs[emotion][random.randint(0, len(songs[emotion]) - 1)]
            output.append({
                'start': sentences[i].start_time,
                'end': sentences[i].end_time,
                'song': song
            })

    return output


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
        return "Neutral"

    return result


nltk.download("omw-1.4")

print(get_song_info(test_data))
