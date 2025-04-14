from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Template

app = FastAPI()
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

@app.get("/play", response_class=HTMLResponse)
async def play(id: str, title: str, artist: str):
    with open("templates/player.html") as f:
        template = Template(f.read())
    return template.render(video_id=id, title=title, artist=artist)
