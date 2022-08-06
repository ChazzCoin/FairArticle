from FA.JEngines import JarticleEnhancer
from FW.Core.CoreDownloaders import ArticleDownloader
from FW import Crawler

MAX_THRESHOLD = 100

def crawl(url=None, maxThreshold=MAX_THRESHOLD, enhance=False):
    if not url:
        return "No Url"
    obj = Crawler.run_ListMode(url=url, maxQueue=maxThreshold)
    if obj.articles:
        return obj.articles if not enhance else __enhance_articles(obj.articles)
    return obj

def download(url=None, enhance=False):
    if not url:
        return "No Url"
    result = ArticleDownloader.download_article(url)
    if result:
        return result if not enhance else __enhance_articles(result)
    return False

def __enhance_articles(articles):
    return JarticleEnhancer.RUN(articles=articles, saveToDB=False, returnArticles=True)

if __name__ == '__main__':
    import FaiRoutines
    url1 = "https://www.nbcnews.com/politics/justice-department/justice-department-investigating-trumps-actions-part-jan-6-probe-rcna40167"
    url2 = "https://towardsdatascience.com/a-step-by-step-guide-to-scheduling-tasks-for-your-data-science-project-d7df4531fc41"
    func1 = FaiRoutines.FairFunction(download, url1)
    func0 = FaiRoutines.FairFunction(download, url2)
    routine1 = FaiRoutines.FairRoutine(functions=[func1, func0])
    routine1.start_await()
    print(routine1)