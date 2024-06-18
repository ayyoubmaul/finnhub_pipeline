import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="<changes with your own api key>")

    news = finnhub_client.general_news('general', min_id=0)

    return news
