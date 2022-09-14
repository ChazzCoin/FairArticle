from FA.JEngines.JarticleEnhancer.JProcess import process_article
from FA.JEngines import CategoryEngine
from FA.JEngines import TickerEngine
from FA.JHelpers import NLTK
from FNLP.Language import Summarizer, Keywords
from F import LIST, DICT, DATE
from FCM.Jarticle.jProvider import jPro
# from FCM.Jarticle.jdexes.jCompany import jCompany
from F.LOG import Log

Log = Log("Jarticle.Engine.Processor.ArticleProcessor_v2")

WORDS = "words"
BODY = "body"
TITLE = "title"
DESCRIPTION = "description"

"""
-> Maintains the lifecycle of processing a list of hookups
"""

LAST_UPDATE = "May 19 2022"

JP = jPro()

def RUN(articles=None, saveToDB=True, returnArticles=False):
    """ -> MASTER PROCESSOR ID CREATED HERE <- """
    if not articles:
        articles = JP.get_ready_to_enhance()
    if not articles:
        return False
    arts = LIST.flatten(articles)
    # Alert.send_alert(f"Jarticle: STARTING New Enhancements. COUNT=[ {len(arts)} ]")
    overall_count = 0
    enhanced_articles = []
    for article in arts:
        if not article:
            continue
        overall_count += 1
        id = DICT.get("_id", article)
        date = DICT.get("published_date", article, "unknown")
        Log.i(f"Enhancing Article ID=[ {id} ], DATE=[ {date} ], COUNT=[ {overall_count} ]")
        e_art = process_article(article, isUpdate=False)
        if saveToDB:
            # -> Update Article in MongoDB
            JP.update_article(e_art)
        if returnArticles:
            enhanced_articles.append(e_art)
    Log.i(f"Enhanced {overall_count} Articles!")
    # Alert.send_alert(f"Jarticle: FINISHING New Enhancements.")
    return enhanced_articles


def categorizer(article):
    Log.i("Category Engine...")
    return CategoryEngine.process_single_article(article, isUpdate=True)

def sozin(content):
    Log.i("Ticker Engine...")
    tickers = TickerEngine.extract_all(content)
    stock_tickers = LIST.get(0, tickers)
    crypto_tickers = LIST.get(1, tickers)
    Log.d("Tickers: " + str(tickers))
    if stock_tickers and crypto_tickers:
        return tickers
    elif stock_tickers:
        return stock_tickers
    elif crypto_tickers:
        return crypto_tickers
    return False

# def get_company_reference(article):
#     Log.i("Company Reference Engine...")
#     tickers = DICT.get("tickers", article)
#     if not tickers:
#         return False
#     jc = jCompany.constructor_jcompany()
#     references = {}
#     for key in tickers:
#         id = jc.get_company_id_for_ticker(key)
#         if id and key not in references.keys():
#             references[key] = id
#     return references

def get_summary(article):
    Log.i("Summary Engine...")
    body = DICT.get("body", article, default="False")
    summary = Summarizer.summarize(body, 4)
    # summary = Language.text_summarizer(body, 4)
    return summary

def get_keywords(article):
    Log.i("Keywords Engine...")
    title = DICT.get("title", article, default="False")
    body = DICT.get("body", article, default="False")
    keywords = Keywords.keywords(str(body) + str(title))
    newList = []
    for item in keywords:
        newList.append(item)
    return newList

def get_sentiment(content):
    Log.i("Sentiment Engine...")
    sentiment = NLTK.get_content_sentiment(content)
    return sentiment

# def get_source_page_rank(article):
#     Log.i("Page Rank Engine...")
#     from jarEngine.Helper import PageRank
#     url = DICT.get("url", article, "unknown")
#     rank = PageRank.get_page_rank(url)
#     return rank

# -> [MASTER]
def enhance_article(article, content):
    article = categorizer(article)
    article["keywords"] = get_keywords(article)
    article["summary"] = get_summary(article)
    article["tickers"] = sozin(content)
    # article["company_ids"] = get_company_reference(article)
    article["sentiment"] = get_sentiment(content)
    # article["source_rank"] = get_source_page_rank(article)
    article["updatedDate"] = DATE.mongo_date_today_str()
    return article

def update_enhanced_summary(article):
    article["summary"] = get_summary(article)
    return article

if __name__ == '__main__':
    test = RUN(saveToDB=False, returnArticles=True)
    print(test)