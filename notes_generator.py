import whisper
from moviepy.editor import VideoFileClip
from googletrans import Translator

model = whisper.load_model("base")
translator = Translator()


# ✅ Add all languages here (easy to modify anytime)
LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "bn": "Bengali",
    "ta": "Tamil",
    "te": "Telugu",
    "mr": "Marathi",
    "gu": "Gujarati",
    "kn": "Kannada",
    "ml": "Malayalam",
    "or": "Odia",
    "ur": "Urdu"
}


def extract_audio(video_path, audio_path="temp.wav"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    return audio_path


def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]


def summarize_text(text):
    sentences = text.split(".")
    return ". ".join(sentences[:6])


def generate_notes(video_path):
    audio = extract_audio(video_path)
    transcript = speech_to_text(audio)

    notes_en = summarize_text(transcript)

    notes = {}

    # English first
    notes["en"] = notes_en

    # Translate to all other languages automatically
    for code in LANGUAGES:
        if code == "en":
            continue
        translated = translator.translate(notes_en, dest=code).text
        notes[code] = translated

    return notes
