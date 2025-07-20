from config import search_serper

def find_competitors(parsed):
    query = f"{parsed['solution']} {', '.join(parsed['keywords'])}"
    results = search_serper(query)

    competitors = []
    for res in results:
        competitors.append({
            "title": res.get("title"),
            "snippet": res.get("snippet"),
            "link": res.get("link")
        })

    return competitors
