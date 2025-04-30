from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


generator = pipeline(
    "text-generation",
    model="gpt2",
    device=0)

app = FastAPI()


class Bodey(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Text Generation API</title>
        </head>
        <body>
            <h1>Text Generation API</h1>
            <form action="/generate" method="post">
                <textarea name="text" rows="4" cols="50"></textarea><br>
                <input type="submit" value="Generate">
            </form>
        </body>
    </html>
    """

@app.post("/generate")
async def generate_text(body: Bodey):
    text = body.text
    generated_text = generator(text, max_length=50, num_return_sequences=1)
    return {"generated_text": generated_text[0]['generated_text']}