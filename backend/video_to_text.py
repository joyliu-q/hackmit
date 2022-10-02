import os
import shutil
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import whisper
from fastapi import UploadFile

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

  def upload_file(self, file: UploadFile):
    # save file locally
    with open("data/" + file.filename, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)

  def extract_audio(self, video_path):
      audio_path = video_path + "_audio.mp3"
      os.system(f'ffmpeg -i "{video_path}" "{audio_path}" -y')
      return audio_path

  def video_to_text(self, audio_path):
      return self.transcribe_audio(audio_path)

  def transcribe_audio(self, audio_path):
    print(whisper.load_audio(audio_path))
    transcript = self.model.transcribe(audio_path)
    transcript['segments'] = [TranscriptSegment(s['text'], s['start'], s['end']) for s in transcript['segments']]
    return transcript    

# Example usage
# vtt = VideoToText()
# vtt.video_to_text("../../data/barackobamafederalplaza.mp3")
