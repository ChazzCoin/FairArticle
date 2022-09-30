from F import DICT
import F
from FA.JEngines.JarticleEnhancer import Enhancers, MetaEnhancers

from F.LOG import Log
Log = Log("Jarticle.Engine.Processor.ArticleProcessor_v2")

LAST_UPDATE = "May 19 2022"

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
    content = F.combine_args_str(title, body, description)
    # -> Enhancers
    enhanced_article = Enhancers.enhance_article(article=article, content=content)
    enhanced_article = MetaEnhancers.enhance_article(article=enhanced_article)
    return enhanced_article