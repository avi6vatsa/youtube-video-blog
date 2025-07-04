import os
import requests

def get_transcript(youtube_url):
    """
    Fetch transcript from YouTube using Apify pintostudio/youtube-transcript-scraper actor.
    Returns transcript text or None if failed.
    """
    APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
    if not APIFY_API_TOKEN:
        raise ValueError("APIFY_API_TOKEN not set in environment variables.")

    api_url = f"https://api.apify.com/v2/acts/pintostudio~youtube-transcript-scraper/run-sync-get-dataset-items?token={APIFY_API_TOKEN}"
    payload = {
        "videoUrl": youtube_url
    }
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, list) or not data:
            print("Transcript not found in Apify response.")
            return None
        segments = data[0].get("data", [])
        transcript_lines = [seg["text"] for seg in segments if "text" in seg]
        transcript = "\n".join(transcript_lines)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript from Apify: {e}")
        return None 