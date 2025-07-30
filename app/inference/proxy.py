import hashlib
import os
import openai
from app.crypto.signer import sign_output
from app.cache.cache_manager import get_from_cache, store_in_cache

openai.api_key = os.getenv("OPENAI_API_KEY")

async def handle_inference(prompt: str):
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()

    cached = get_from_cache(prompt_hash)
    if cached:
        return cached

    # 🔥 Real AI call using GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    output = response.choices[0].message["content"]

    signature = sign_output(output.encode())

    result = {
        "output": output,
        "hash": prompt_hash,
        "signature": signature.hex()
    }

    store_in_cache(prompt_hash, result)
    return result
