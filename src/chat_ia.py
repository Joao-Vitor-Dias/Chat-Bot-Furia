from transformers import pipeline
from dotenv import load_dotenv
import os
from huggingface_hub import login

load_dotenv()

HUGGING_FACE_KEY = os.getenv("HUGGING_FACE_TOKEN")

login(HUGGING_FACE_KEY)

pipe = pipeline("text-generation", model="", device = "cuda")

mensagem = [
    {"role": "user", "content": "Qual a cor do ceu?"},
]
print(pipe(mensagem))