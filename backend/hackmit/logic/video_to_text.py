import os
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

model = whisper.load_model("base")
options = whisper.DecodingOptions(language="en")

def mp4_to_mp3(mp4_path, mp3_path):
  os.system(f"ffmpeg -i {mp4_path} {mp3_path}")

def transcribe_audio(audio_path):
  print(whisper.load_audio(audio_path))
  transcript = model.transcribe(audio_path)
  transcript['segments'] = [TranscriptSegment(s['text'], s['start'], s['end']) for s in transcript['segments']]
  print(transcript)
  return transcript
  
def video_to_text(video_path):
  audio_path = video_path + "_audio.mp3"
  mp4_to_mp3(video_path, audio_path)
  transcribe_audio(video_path)

video_to_text("../../data/barackobamafederalplaza.mp3")