import text2emotion as te
import json
import random
import nltk

from video_to_text import TranscriptSegment


songs = {
    "Happy": ["HAPPY"],
    "Sad": ["SAD"],
    "Angry": ["ANGRY"],
    "Surprise": ["SURPRISE"],
    "Fear":["FEAR"],
    "Neutral": ["NEUTRAL"]
}


test_data =[TranscriptSegment("I am happy", 0, 1), TranscriptSegment("I am sad", 1, 2), TranscriptSegment("I am angry", 2, 3), TranscriptSegment("I am surprised", 3, 4), TranscriptSegment("I am afraid", 4, 5), TranscriptSegment("I am neutral", 5, 6)]


def get_song_info(sentences):
    song = None
    output = []
    for i in range(len(sentences)):
        print(sentences[i])
        emotion = get_emotion(sentences[i].text)
        song = songs[emotion][random.randint(0, len(songs[emotion])- 1)]

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
