import feedparser

def get_news():

    feed = feedparser.parse("https://feeds.feedburner.com/TheHackersNews")

    news = []

    for item in feed.entries[:10]:

        news.append({
            "title": item.title,
            "link": item.link,
            "date": item.published
        })

    return news