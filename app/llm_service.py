

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def build_image_prompt(user_prompt: str, style: str) -> dict:
    system = """
You are a prompt engineer for AI image generation.
Return valid JSON with:
- prompt
- negative_prompt

Rules:
- Make the prompt vivid and production-ready.
- Keep the subject aligned with the user's request.
- Emphasize style, lighting, pose, composition, and background.
- For celebrity-inspired requests, avoid exact identity-copy wording if needed.
"""

    completion = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": system},
            {
                "role": "user",
                "content": f"User request: {user_prompt}\nStyle: {style}"
            },
        ],
        temperature=0.8,
    )

    text = completion.choices[0].message.content
    return {"raw": text}