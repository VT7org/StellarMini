# Telegram Music Bot + Web Player

A professional-grade Telegram bot that plays music in a web or mini app using modular sources.

## Features
- Modular source system (YouTube now, easily extendable)
- Web app styled player (toggle app/web style)
- FastAPI backend
- Dockerized deployment

## Setup
1. Set up `.env`:
```
TELEGRAM_BOT_TOKEN=your_token
YOUTUBE_API_KEY=your_youtube_key
```

2. Run:
```
docker-compose up --build
```

3. In Telegram, send `/play <song>` to your bot!

## Add Sources
Create a file in `sources/` with a `search(query)` function returning:
```python
{
  "title": "Song Title",
  "artist": "Artist Name",
  "id": "video_or_track_id"
}
```

Update `song_router.py` to use it.