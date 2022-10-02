import os
import io

from video_to_text import VideoToText
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
    if len(file) == 0:
        raise HTTPException(status_code=400, detail="File must have some content.")
    if len(file) > 10 << 20:
        raise HTTPException(status_code=400, detail="File must be less than 10MB.")
    
    # TODO: call video_to_text
    vtt = VideoToText()
    vtt.upload_file(file)
    res = vtt.video_to_text("data/" + file.filename)

    # Type of res: TranscriptSegment[]

    # TODO: call kincent/daniel's code to figure out sentiments
    
    # TODO: from sentiment, figure out which musics to insert

    # TODO: add music

    # TODO: return the actual clip as an output? or S3 bucket lol idk

    return {"music": "TODO"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)