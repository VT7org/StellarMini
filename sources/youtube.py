from youtubesearchpython import VideosSearch

def search_youtube(query):
    results = VideosSearch(query, limit=1).result()
    if not results["result"]:
        return None
    r = results["result"][0]
    return {
        "id": r["id"],
        "title": r["title"],
        "link": r["link"],
        "duration": r["duration"]
    }