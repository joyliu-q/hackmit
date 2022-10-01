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

model = whisper.load_model("tiny")
options = whisper.DecodingOptions(language="en")

def mp4_to_mp3(mp4_path, mp3_path):
  os.system(f"ffmpeg -i {mp4_path} {mp3_path}")

# Detect the audio language. If it's not english, translate to english.
def detect_and_translate(audio_path):
  audio = whisper.load_audio(audio_path)

  # make log-Mel spectrogram and move to the same device as the model
  mel = whisper.log_mel_spectrogram(audio).to(model.device)

  # detect the spoken language
  _, probs = model.detect_language(mel)
  print(f"Detected language: {max(probs, key=probs.get)}")

  # decode the audio
  options = whisper.DecodingOptions()
  result = whisper.decode(model, mel, options)

  # print the recognized text
  print(result.text)


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

video_to_text("barackobamafederalplaza.mp3")
