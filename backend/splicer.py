from pydub import AudioSegment


def cut(audio: AudioSegment, start: float, end: float):
    start = int(start * 1000)
    end = int(end * 1000)

    return audio[start:end]


def load_files(filenames):
    musics = dict()

    for filename in filenames:
        musics[filename] = AudioSegment.from_mp3(filename)

    return musics


"""

[
    {
        "start": 0,
        "end": 10,
        "song": "asdf.mp3"
    },
]
"""


def overlay_music(base_file, segments):
    base_audio = AudioSegment.from_mp3(base_file)

    music_map = load_files(set([s["song"] for s in segments]))

    print(music_map)

    for segment in segments:
        song_audio = music_map[segment["song"]]
        start = segment["start"]
        end = segment["end"]

        song_audio = cut(song_audio, 0, end - start) - 15
        song_audio = low_high_beginning(song_audio)
        song_audio = high_low_end(song_audio)

        base_audio = base_audio.overlay(song_audio, position=start * 1000)

    return base_audio


def low_high_beginning(audio):
    duration = 200
    db_less = 10
    steps = 5

    beginning_audio = audio[:duration] - db_less

    for i in range(1, steps):
        next_audio = audio[duration * i: duration * (i + 1)] - (db_less - i)
        beginning_audio = beginning_audio + next_audio

    return beginning_audio + audio[duration * steps:]


def high_low_end(audio):
    duration = 200
    db_less = 10
    steps = 5

    end_audio = audio[-duration:] - db_less

    for i in range(1, steps):
        prev_audio = audio[-duration * (i + 1): -duration * i] - (db_less - i)
        end_audio = prev_audio + end_audio

    return audio[:-duration*steps] + end_audio
