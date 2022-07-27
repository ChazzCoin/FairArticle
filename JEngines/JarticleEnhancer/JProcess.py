from FSON import DICT
from fairNLP import Language
from JEngines import JarticleEnhancer

from Jarticle.jProvider import jPro
from FLog.LOGGER import Log
Log = Log("Jarticle.Engine.Processor.ArticleProcessor_v2")

LAST_UPDATE = "May 19 2022"

JP = jPro()

# -> Master Runner of Single Article
def process_article(article, isUpdate):
    updated_date = DICT.get("updatedDate", article, False)
    source = DICT.get("source", article, "False")
    if not isUpdate and updated_date or source == "twitter" or source == "reddit":
        return
    if isUpdate and updated_date == LAST_UPDATE:
        return
    # -> Setup
    title = DICT.get("title", article)
    body = DICT.get("body", article)
    description = DICT.get("description", article)
    # -> Combine All Main Content (Title, Body, Description)
    content = Language.combine_args_str(title, body, description)
    # -> Enhancers
    enhanced_article = JarticleEnhancer.enhance_article(article=article, content=content)
    # -> Update Article in MongoDB
    JP.update_article(enhanced_article)


if __name__ == '__main__':
    RUN()