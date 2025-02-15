from pydub import AudioSegment
import whisper
import openai
import os

# Set your OpenAI API Key
openai.api_key = "your_openai_api_key_here"

def extract_audio_from_video(video_file):
    """Extract audio from a video file using pydub"""
    print("Extracting audio from video...")
    audio = AudioSegment.from_file(video_file, format="mp4")
    audio_file = "extracted_audio.mp3"
    audio.export(audio_file, format="mp3")
    print(f"Audio extracted to: {audio_file}")
    return audio_file

def transcribe_audio(audio_file):
    """Transcribe the audio using Whisper"""
    print("Transcribing audio...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    print("Transcription completed.")
    return result["text"]

def summarize_text(text):
    """Summarize the transcribed text using OpenAI GPT"""
    print("Summarizing the transcription...")
    prompt = f"Summarize the following text:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    summary = response['choices'][0]['message']['content']
    print("Summary generated.")
    return summary

def summarize_video(video_file):
    """Main function to summarize a video"""
    audio_file = extract_audio_from_video(video_file)
    transcript = transcribe_audio(audio_file)
    summary = summarize_text(transcript)
    return summary

if __name__ == "__main__":
    video_file = "https://www.youtube.com/watch?v=XslI8h7cGDs&list=PLxCzCOWd7aiFM9Lj5G9G_76adtyb4ef7i"  # Replace with your video file path
    if os.path.exists(video_file):
        summary = summarize_video(video_file)
        print("\nVideo Summary:\n", summary)
    else:
        print("Error: Video file not found.")

