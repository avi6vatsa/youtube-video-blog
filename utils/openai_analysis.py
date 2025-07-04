import openai
import os

def analyze_transcript(transcript):
    """
    Analyze transcript with OpenAI: generate summary, outline, and key points.
    Returns a dict with 'summary', 'outline', and 'key_points'.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set in environment variables.")
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    prompt = (
        "You are an expert content analyst. Given the following YouTube transcript, generate:\n"
        "1. A concise summary (3-5 sentences)\n"
        "2. A detailed outline (bulleted)\n"
        "3. 5-10 key points (bulleted)\n\n"
        "Transcript:\n"
        f"{transcript}\n\n"
        "Respond in this format:\n"
        "Summary:\n<summary>\n\n"
        "Outline:\n<outline>\n\n"
        "Key Points:\n<key points>\n"
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
            temperature=0.5
        )
        content = response.choices[0].message.content
        # Simple parsing based on expected format
        summary = outline = key_points = ""
        if "Summary:" in content:
            parts = content.split("Summary:", 1)[1].split("Outline:", 1)
            summary = parts[0].strip()
            if len(parts) > 1:
                rest = parts[1].split("Key Points:", 1)
                outline = rest[0].strip()
                if len(rest) > 1:
                    key_points = rest[1].strip()
        return {
            "summary": summary,
            "outline": outline,
            "key_points": key_points
        }
    except Exception as e:
        print(f"Error analyzing transcript with OpenAI: {e}")
        return None

def research_with_openai(transcript_or_topic):
    """
    Use OpenAI to find interesting facts, recent information, or use cases about the transcript or topic.
    Returns a string with the research findings.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set in environment variables.")
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    prompt = (
        "You are a research assistant. Based on the following transcript or topic, find and list interesting facts, recent developments, or real-world use cases that would enrich a blog post. "
        "If possible, include up-to-date or lesser-known information.\n\n"
        f"Transcript or topic:\n{transcript_or_topic}\n\n"
        "Respond with a bulleted list of research findings."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600,
            temperature=0.7
        )
        content = response.choices[0].message.content
        return content.strip()
    except Exception as e:
        print(f"Error researching with OpenAI: {e}")
        return None 