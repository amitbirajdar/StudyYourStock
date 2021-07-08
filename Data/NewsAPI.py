from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='794a246d0ed64c36b374079dd785f179')

# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           language='en')

# /v2/everything
all_articles = newsapi.get_everything(q='DraftKings Inc',
                                      from_param='2021-02-07',
                                      to='2021-03-06',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

# /v2/sources
sources = newsapi.get_sources()
print(all_articles)
print()