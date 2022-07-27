from JEngines import JarticleEnhancer
from Downloader import ArticleDownloader
import Crawler

MAX_THRESHOLD = 100

def crawl(url, maxThreshold=MAX_THRESHOLD, enhance=False):
    obj = Crawler.run_ListMode(url=url, maxQueue=maxThreshold)
    if obj.articles:
        return obj.articles if not enhance else __enhance_articles(obj.articles)
    return obj

def download(url, enhance=False):
    result = ArticleDownloader.download_article(url)
    if result:
        return result if not enhance else __enhance_articles(result)
    return False

def __enhance_articles(articles):
    return JarticleEnhancer.RUN(articles=articles, saveToDB=False, returnArticles=True)