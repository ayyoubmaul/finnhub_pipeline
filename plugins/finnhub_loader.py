import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cplfjshr01qjtk5490p0cplfjshr01qjtk5490pg")

    news = finnhub_client.general_news('general', min_id=0)

    return news
