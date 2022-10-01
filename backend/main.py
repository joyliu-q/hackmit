from backend.video_to_text import VideoToText
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/hello")
def hello_view(name: str = "Human"):
    return {"message": f"Hello there, {name}!"}

@app.get("/add-music")
def add_music(file: bytes = File(...)):
    if len(file) == 0:
        raise HTTPException(status_code=400, detail="File must have some content.")
    if len(file) > 10 << 20:
        raise HTTPException(status_code=400, detail="File must be less than 10MB.")
    
    # TODO: call video_to_text
    vtt = VideoToText()
    vtt.upload_file(file)
    vtt.video_to_text("data/" + file.filename)

    # TODO: call kincent/daniel's code to figure out sentiments

    # TODO: from sentiment, figure out which musics to insert

    # TODO: add music

    # TODO: return the actual clip as an output? or S3 bucket lol idk

    return {"music": "TODO"}
