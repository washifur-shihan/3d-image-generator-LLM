import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_TOKEN"),
)

def generate_image(prompt: str):
    image = client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell",
    )
    return image