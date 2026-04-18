from dotenv import load_dotenv
load_dotenv()

import io
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse


from app.schemas import ImageRequest
from app.llm_service import build_image_prompt
from app.image_service import generate_image



app = FastAPI(title="Cartoon Football Image Generator")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/generate")
def generate(req: ImageRequest):
    try:
        llm_result = build_image_prompt(req.prompt, req.style)

        # If the LLM returns plain text instead of JSON, use fallback
        final_prompt = req.prompt
        try:
            parsed = json.loads(llm_result["raw"])
            final_prompt = parsed.get("prompt", req.prompt)
        except Exception:
            final_prompt = f"{req.prompt}, {req.style}, high detail, cinematic lighting"

        image = generate_image(final_prompt)

        buf = io.BytesIO()
        image.save(buf, format="PNG")
        buf.seek(0)

        return StreamingResponse(buf, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))