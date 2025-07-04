import os
import requests

def generate_blog_post_with_claude(analysis, research, topic=None, keyword=None, audience=None, word_count_goal="1500-2000"):
    """
    Use Anthropic Claude to generate a blog post draft from analysis and research, using a detailed SEO-optimized prompt.
    Returns the blog post as a string.
    """
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    if not ANTHROPIC_API_KEY:
        raise ValueError("ANTHROPIC_API_KEY not set in environment variables.")

    # Claude API endpoint (v1/v2)
    url = "https://api.anthropic.com/v1/messages"

    # Use the provided topic, keyword, and audience, or fallback to summary/key points
    topic = topic or analysis.get('summary', 'the main topic of the video')
    keyword = keyword or "[INSERT PRIMARY KEYWORD HERE]"
    audience = audience or "[INSERT AUDIENCE DESCRIPTION HERE]"

    prompt = f"""
# Blog Writing Prompt: Create Engaging, SEO-Optimized Content

You are an expert blog writer tasked with creating high-quality content that is engaging, informative, SEO-optimized, and highly shareable. Follow these comprehensive guidelines:

## Content Strategy & Research
- **Research thoroughly**: Use current, credible sources and include recent statistics, studies, or data points
- **Understand the target audience**: Write for their knowledge level, interests, and pain points
- **Address search intent**: Ensure the content fully answers what readers are searching for
- **Provide unique value**: Offer fresh insights, personal experiences, or novel perspectives on the topic

## SEO Optimization
- **Keyword integration**: Naturally incorporate the primary keyword in:
  - Title (preferably near the beginning)
  - First paragraph
  - At least one H2 heading
  - Throughout the content (aim for 1-2% density)
  - Meta description (if writing one)
- **Use semantic keywords**: Include related terms and synonyms
- **Optimize headings**: Create descriptive H2 and H3 tags that include relevant keywords
- **Internal linking opportunities**: Suggest where internal links to related content would be valuable
- **Featured snippet optimization**: Structure content to answer common questions directly

## Structure & Formatting
- **Compelling headline**: Write a title that is:
  - Clear and descriptive
  - Includes the primary keyword
  - Creates curiosity or promises value
  - Under 60 characters for SEO
- **Hook opening**: Start with a compelling question, surprising statistic, story, or bold statement
- **Scannable format**: Use:
  - Short paragraphs (2-4 sentences)
  - Bullet points and numbered lists
  - Subheadings every 200-300 words
  - Bold text for key points
- **Logical flow**: Organize content with clear transitions between sections

## Engagement Techniques
- **Conversational tone**: Write as if speaking directly to the reader using "you"
- **Storytelling elements**: Include anecdotes, case studies, or examples
- **Interactive elements**: Pose questions to the reader, include polls, or suggest exercises
- **Visual content suggestions**: Recommend where images, infographics, or videos would enhance the content
- **Emotional connection**: Address reader pain points and aspirations
- **Actionable advice**: Provide specific, implementable tips and strategies

## Shareability Factors
- **Social media optimization**: 
  - Include quotable statements
  - Create content that sparks discussion
  - Address trending topics when relevant
- **Value-packed content**: Ensure every section provides genuine value
- **Controversial or contrarian angles**: When appropriate, challenge common assumptions
- **List formats**: Use numbered lists for easy sharing ("7 Ways to..." "5 Mistakes...")
- **Include data and statistics**: Make claims that people want to cite and share

## Technical Best Practices
- **Optimal length**: Aim for 1,500-2,500 words for in-depth topics
- **Reading level**: Write at an 8th-9th grade reading level for accessibility
- **Mobile optimization**: Use short sentences and paragraphs for mobile readers
- **Loading speed considerations**: Suggest optimized image placements

## Content Elements to Include
- **Introduction**: Hook + preview of what readers will learn
- **Main content sections**: 3-5 key points with supporting details
- **Examples and case studies**: Real-world applications
- **Expert quotes or statistics**: Third-party validation
- **Common objections**: Address potential counterarguments
- **Strong conclusion**: Summarize key takeaways
- **Clear call-to-action**: What should readers do next?

## Quality Assurance
- **Fact-check all claims**: Ensure accuracy and cite sources
- **Original content**: Provide fresh perspectives, not rehashed information
- **Grammar and readability**: Use clear, error-free writing
- **Value delivery**: Every paragraph should serve the reader's needs

## Shareability Checklist
- Does this teach something new or challenge conventional thinking?
- Would readers want to discuss this with colleagues or friends?
- Are there quotable insights or statistics?
- Does it solve a real problem readers face?
- Is it visually appealing and easy to scan?

## Final Instructions
When writing the blog post:
1. Start with a compelling, keyword-optimized title
2. Write an engaging introduction that hooks the reader
3. Develop the main content using the structure guidelines above
4. Include specific, actionable advice throughout
5. End with a strong conclusion and clear call-to-action
6. Suggest 3-5 relevant tags for the post
7. Provide a meta description (150-160 characters)

**Topic for this blog post**: {topic}
**Target keyword**: {keyword}
**Target audience**: {audience}
**Word count goal**: {word_count_goal}

---

Here is the analysis and research to use for the blog post:

Summary:
{analysis['summary']}

Outline:
{analysis['outline']}

Key Points:
{analysis['key_points']}

Research:
{research}

Now write the complete blog post following all these guidelines.
"""
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    data = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 4000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        # Claude's response is in result['content'][0]['text']
        blog_post = result['content'][0]['text']
        return blog_post.strip()
    except Exception as e:
        print(f"Error generating blog post with Claude: {e}")
        return None

def generate_blog_post(analysis, research):
    """Generate a blog post draft using Anthropic Claude."""
    # TODO: Implement Anthropic Claude API call
    pass 