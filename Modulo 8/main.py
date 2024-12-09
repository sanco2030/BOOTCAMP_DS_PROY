from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sentiment_analyzer.analyzer import SentimentAnalyzer
import os

app = FastAPI()

class TextInput(BaseModel):
    text: str

analyzer = SentimentAnalyzer()

@app.get("/", summary="Página principal")
async def serve_frontend():
    file_path = os.path.join("static", "index.html")
    return FileResponse(file_path)

@app.post("/sentiment", summary="Analizar sentimiento")
async def analyze_text(input: TextInput):
    text = input.text
    sentiment = analyzer.predict(text)
    return {"text": text, "sentiment": sentiment}


app.mount("/static", StaticFiles(directory="static"), name="static")
