from FA.JEngines.JarticleEnhancer.JProcess import process_article
from FCM.Jarticle.jProvider import jPro
from F import LIST, DICT
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
    return enhanced_articles


if __name__ == '__main__':
    test = RUN(saveToDB=False, returnArticles=True)
    print(test)