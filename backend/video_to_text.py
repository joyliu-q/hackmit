import os
import shutil
import numpy as np

import whisper

class TranscriptSegment:
  def __init__(self, text, start_time, end_time):
    self.text = text
    self.start_time = start_time
    self.end_time = end_time
  def __str__(self):
    return f"{self.text} ({self.start_time} - {self.end_time})"
  def __repr__(self):
    return str(self)

class VideoToText:
  def __init__(self):
    self.model = whisper.load_model("base")
    self.options = whisper.DecodingOptions(language="en")

  def upload_file(self, file = File(...)):
    # save file locally
    with open("data/" + file.filename, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)

  def video_to_text(self, video_path):
      audio_path = video_path + "_audio.mp3"
      os.system(f"ffmpeg -i {video_path} {audio_path}")
      self.transcribe_audio(audio_path)

  def transcribe_audio(self, audio_path):
    print(whisper.load_audio(audio_path))
    transcript = self.model.transcribe(audio_path)
    transcript['segments'] = [TranscriptSegment(s['text'], s['start'], s['end']) for s in transcript['segments']]
    print(transcript)
    return transcript    

# Example usage
vtt = VideoToText()
vtt.video_to_text("../../data/barackobamafederalplaza.mp3")