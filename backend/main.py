import os
from splicer import overlay_music
from sentimentanalysis import get_song_info

from video_to_text import VideoToText
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.mount("/data", StaticFiles(directory="data"), name="data")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello")
def hello_view(name: str = "Human"):
    return {"message": f"Hello there, {name}!"}

@app.post("/add-music")
def add_music(file: UploadFile):
    # TODO: call video_to_text

    saved_path = os.path.join("data", file.filename)
    # save file to disk
    with open(saved_path, "wb") as f:
        f.write(file.file.read())

    vtt = VideoToText()
    audio_path = vtt.extract_audio(saved_path)
    res = vtt.video_to_text(audio_path)

    # Type of res: TranscriptSegment[]

    # TODO: call kincent/daniel's code to figure out sentiments
    sentiments = get_song_info(res['segments'])

    # TODO: from sentiment, figure out which musics to insert

    result_audio = overlay_music(audio_path, sentiments)

    new_audio_path = "data/result.mp3"
    result_audio.export(new_audio_path, format="mp3")
    print("EXPOteD")

    # TODO: add music
    os.system(f"mkdir -p data")
    os.system(f'touch "{saved_path}"')
    os.system(f'ffmpeg -i {saved_path} -i {new_audio_path} -c:v copy -map 0:v:0 -map 1:a:0 "data/result.mp4" -y')

    # copy file over to ../frontend/public
    # os.system(f'cp {saved_path} ../frontend/src/{saved_path} -y')

    # TODO: return the actual clip as an output? or S3 bucket lol idk

    return {"path": saved_path}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
