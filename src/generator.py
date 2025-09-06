# src/generator.py

import os
from dotenv import load_dotenv # type: ignore
from mistralai import Mistral # type: ignore

# Load API key
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    raise ValueError("❌ MISTRAL_API_KEY not found in .env file")

# Initialize client
client = Mistral(api_key=api_key)

# Platform-specific style templates
PLATFORM_STYLES = {
    "twitter": "Make it short, punchy, with hashtags if relevant. Max 280 characters.",
    "linkedin": "Make it professional, structured, with 2-3 short paragraphs.",
    "instagram": "Make it casual, friendly, and include emojis if natural.",
    "facebook": "Make it conversational, engaging, and suitable for a broad audience.",
    "default": "General social media style."
}

# Post length guides
LENGTH_GUIDES = {
    "short": "Keep it very concise, no more than 1-2 sentences.",
    "medium": "Write 2-3 short paragraphs.",
    "long": "Write a detailed post with multiple paragraphs and examples."
}


def generate_post(
    long_form_text: str,
    platform: str,
    tone: str = "default",
    length: str = "medium",
    temperature: float = 0.7
) -> str:
    """
    Generate a platform-specific social post using Mistral AI.

    Args:
        long_form_text (str): The input article/blog text.
        platform (str): Target platform (twitter, linkedin, etc.).
        tone (str): Writing tone (default, professional, casual, etc.).
        length (str): Post length (short, medium, long).
        temperature (float): Creativity setting (0.2 - 1.0).

    Returns:
        str: Generated social media post.
    """

    style = PLATFORM_STYLES.get(platform.lower(), PLATFORM_STYLES["default"])
    length_guide = LENGTH_GUIDES.get(length, LENGTH_GUIDES["medium"])

    prompt = f"""
    You are an expert social media content writer.
    
    Task: Rewrite the following content into a post for {platform}.
    Tone: {tone}.
    Style: {style}.
    Length: {length_guide}.
    
    Content:
    {long_form_text}
    """

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )

    return response.choices[0].message.content
