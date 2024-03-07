# Video Subtitle Translator

This Python script allows you to generate subtitles for a video file by transcribing its audio content and optionally translating the text into different languages.

### [Google Colab🎯](https://colab.research.google.com/drive/1qrxsADA7rQgzKj0FIzr0RM-y-YYXt3Rx?usp=sharing)
## How It Works

1. Input Video: You provide the path to the video file.
2. Audio Extraction: The script extracts the audio from the video.
3. Language Selection: You choose whether to translate the subtitles and select the desired language.
4. Transcription: The audio is transcribed, and subtitles are generated.
5. Translation: If selected, the subtitles are translated into the chosen language.
6. Output: Subtitles are saved in the SubRip (.srt) format.

## Dependencies

- [moviepy](https://zulko.github.io/moviepy/install.html) : Used for extracting audio from the video.
- [ffmpeg](https://ffmpeg.org/) : A complete, cross-platform solution to record, convert and stream audio and video.
- [whisper](https://github.com/openai/whisper) : Provides the transcription model.
- [googletrans](https://py-googletrans.readthedocs.io/en/latest/) : Utilized for text translation. Note: if it didn't work ``` pip install googletrans==4.0.0-rc1 ```
- [tqdm](https://pypi.org/project/tqdm/) : Displays a progress bar during transcription and translation.

## Note

- Ensure that the necessary models are downloaded and available to the script.
- This script utilizes resources such as CPU and memory, especially during transcription and translation processes, so it's advisable to use it on machines with sufficient resources.
- Depending on the length of the video and the selected translation options, the process may take some time.

##

Feel free to contribute and improve this project! If you encounter any issues or have suggestions, please open an issue or pull request.

**Disclaimer** : This project relies on external services such as Google Translate, and usage may be subject to their terms and conditions. Please review and comply with their policies when using this script.
