from datetime import timedelta
import whisper
import moviepy.editor as mp
from googletrans import Translator
import os
from tqdm import tqdm


# Function to ask for the path to the video file
def ask_for_video_path():
    while True:
        video_path = input("Enter the path to the video file: ").strip('"')
        if os.path.exists(video_path):
            return video_path
        else:
            print("File not found. Please try again.")


# Function to extract audio from video
def extract_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile("audio.mp3")
    audio.close()


# Function to ask for the language to translate to
def ask_for_language():
    allowed_languages = [
        "No translation",
        "ar",
        "en",
        "es",
        "fr",
        "de",
        "it",
        "ja",
        "ko",
        "pt",
        "ru",
        "zh-CN",
    ]
    print("Choose a language to translate to: ")
    for i, lang in enumerate(allowed_languages):
        print(f"{i}. {lang}")
    while True:
        try:
            language = int(input("Enter the language to translate to: "))
            if language in range(1, 12):
                return allowed_languages[language]
            elif language == 0:
                return None
            else:
                print("Please choose a valid number.")
        except Exception as e:
            print("Error: ", e)


# Function to translate the text
def translate_text(t, l):
    translator = Translator()
    translated = translator.translate(t, dest=l).text
    return translated


# Function to ask for the path to save the subtitle file
def ask_for_save_path():
    while True:
        save_path = input("Enter the path to save the subtitle file: ").strip('"')
        if os.path.exists(save_path):
            return save_path
        else:
            print("File not found. Please try again.")


# Function to transcribe the audio
def transcribe(audio, subtitle_path="", lang=None):
    model = whisper.load_model("base")
    result = model.transcribe(audio, fp16=False, verbose=False)

    segments = result["segments"]
    subtitle_file_path = os.path.join(subtitle_path, f"subtitle_{lang}.srt")
    if os.path.exists(subtitle_file_path):
        os.remove(subtitle_file_path)

    total_segments = len(segments)  # Total number of segments for progress calculation

    # Initialize the progress bar
    with tqdm(total=total_segments, desc="Translating") as pbar:
        for segment in segments:
            startTime = str(0) + str(timedelta(seconds=int(segment["start"]))) + ",500"
            endTime = str(0) + str(timedelta(seconds=int(segment["end"]))) + ",500"
            if lang:
                text = translate_text(segment["text"], lang)
            else:
                text = segment["text"]

            subtitle_segment = (
                f"{segment['id'] + 1}\n{startTime} --> {endTime}\n{ text }\n\n"
            )
            # Writting to the output subtitle file
            with open(subtitle_file_path, "a", encoding="utf-8") as srt_file:
                srt_file.write(subtitle_segment)

            pbar.update(1)  # Update progress bar after processing each segment
    # remove audio file after translation
    os.remove("audio.mp3")
    print("Subtitles generated successfully")


if __name__ == "__main__":
    video = ask_for_video_path()
    subtitle_path = ask_for_save_path()
    lang = ask_for_language()
    extract_audio(video)
    transcribe("audio.mp3", subtitle_path, lang)
