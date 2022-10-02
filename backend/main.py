import os
import io
from sentimentanalysis import get_song_info

from video_to_text import VideoToText
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException

app = FastAPI()

@app.get("/hello")
def hello_view(name: str = "Human"):
    return {"message": f"Hello there, {name}!"}

@app.post("/add-music")
def add_music(file: UploadFile):
    # TODO: call video_to_text

    # save file to disk
    with open(file.filename, "wb") as f:
        f.write(file.file.read())

    vtt = VideoToText()
    res = vtt.video_to_text(file.filename)

    # Type of res: TranscriptSegment[]
    print(res)

    # TODO: call kincent/daniel's code to figure out sentiments
    sentiments = get_song_info(res['segments'])
    
    # TODO: from sentiment, figure out which musics to insert

    # TODO: add music

    # TODO: return the actual clip as an output? or S3 bucket lol idk

    return {"music": "TODO"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
