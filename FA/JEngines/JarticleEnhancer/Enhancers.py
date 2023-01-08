from FA.JEngines import CategoryEngine, TickerEngine
from FNLP.Language import Summarizer, Keywords, Words
from FCM.Jarticle.jCompany import jCompany
from FBrain.JHelpers import NLTK
from F import LIST, DICT, DATE
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

jcompany = jCompany()

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

def get_company_reference(article):
    Log.i("Company Reference Engine...")
    tickers = DICT.get("tickers", article)
    if not tickers:
        return False
    references = {}
    for key in tickers:
        id = jcompany.get_company_id_for_ticker(key)
        if id and key not in references.keys():
            references[key] = id
    return references

def get_summary(article):
    Log.i("Summary Engine...")
    body = DICT.get("body", article, default="False")
    summary = Summarizer.summarize(body, 4)
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

def find_pronouns(content:str):
    results = Words.find_proper_nouns_v2(content)
    return results

""" 
    -> [MASTER]
"""
def enhance_article(article, content):
    article = categorizer(article)
    article["keywords"] = get_keywords(article)
    article["summary"] = get_summary(article)
    article["tickers"] = sozin(content)
    article["company_ids"] = get_company_reference(article)
    article["sentiment"] = get_sentiment(content)
    article["proper_nouns"] = find_pronouns(content)
    # article["source_rank"] = get_source_page_rank(article)
    article["updatedDate"] = DATE.mongo_date_today_str()
    return article