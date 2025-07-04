import os
from dotenv import load_dotenv
from utils.apify_youtube import get_transcript
from utils.openai_analysis import analyze_transcript, research_with_openai
from utils.google_docs import upload_markdown
from utils.anthropic_claude import generate_blog_post_with_claude

# Load environment variables
load_dotenv()
print("APIFY_API_TOKEN:", os.getenv("APIFY_API_TOKEN"))

def get_youtube_transcript(youtube_url):
    """Fetch transcript from YouTube using Apify."""
    # TODO: Implement Apify YouTube transcript extraction
    pass

def analyze_with_openai(transcript):
    """Analyze transcript with OpenAI (summary, outline, key points)."""
    # TODO: Implement OpenAI analysis
    pass

def research_with_perplexity(topic):
    """Do extra research with Perplexity API."""
    # TODO: Implement Perplexity research
    pass

def combine_and_send_to_anthropic(analysis, research):
    """Combine analysis and research, send to Anthropic (Claude) for blog draft."""
    # TODO: Implement Anthropic Claude integration
    pass

def save_as_markdown(content, filename):
    """Save content as a markdown file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved to {filename}")

def save_as_text(content, filename):
    """Save content as a plain text file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved to {filename}")

def run_for_url(youtube_url, row_id=None, sheet_id=None):
    print(f"Processing YouTube URL: {youtube_url}")
    transcript = get_transcript(youtube_url)
    if not transcript:
        print("Failed to fetch transcript.")
        return
    analysis = analyze_transcript(transcript)
    if not analysis:
        print("Failed to analyze transcript.")
        return
    research = research_with_openai(transcript)
    if not research:
        print("Failed to get research from OpenAI.")
        return
    blog_post = generate_blog_post_with_claude(analysis, research)
    if not blog_post:
        print("Failed to generate blog post with Claude.")
        return
    save_as_markdown(blog_post, "blog_post.md")
    save_as_text(blog_post, "blog_post.txt")
    upload_markdown("blog_post.md", title="YouTube Blog Post")
    print("Blog post generated for:", youtube_url)

def main():
    youtube_url = input("Enter YouTube video URL: ")
    transcript = get_transcript(youtube_url)
    if not transcript:
        print("Failed to fetch transcript. Exiting.")
        return
    analysis = analyze_transcript(transcript)
    if not analysis:
        print("Failed to analyze transcript. Exiting.")
        return
    print("\n--- SUMMARY ---\n", analysis['summary'])
    print("\n--- OUTLINE ---\n", analysis['outline'])
    print("\n--- KEY POINTS ---\n", analysis['key_points'])
    research = research_with_openai(transcript)
    if not research:
        print("Failed to get research from OpenAI. Exiting.")
        return
    print("\n--- RESEARCH ---\n", research)
    blog_post = generate_blog_post_with_claude(analysis, research)
    if not blog_post:
        print("Failed to generate blog post with Claude. Exiting.")
        return
    print("\n--- BLOG POST ---\n", blog_post)
    save_as_markdown(blog_post, "blog_post.md")
    save_as_text(blog_post, "blog_post.txt")
    # Upload to Google Docs
    upload_markdown("blog_post.md", title="YouTube Blog Post")

if __name__ == "__main__":
    main() 