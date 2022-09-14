from FA.Categories import Topics
from FA.JEngines import Categorizer
from F import DICT
from F import LIST
from FNLP.Language import Utils
from F.LOG import Log
Log = Log("Engine.Processor.TopicProcessor")

# UNKNOWN = "Unknown"
# UNSURE = "Unsure"
# UNCATEGORIZED = [UNSURE, UNKNOWN]
TOPIC = Topics.ALL_CATEGORIES()

# -> Master Runner
def process_list_of_articles(articles):
    # X. - Topic PROCESSOR - Loop all raw hookups, score/process each one.
    result_articles = []
    for article in articles:
        try:
            # -> BEGIN
            enhanced_art = process_single_article(article)
            result_articles.append(enhanced_art)
        except Exception as e:
            Log.e(f"Failed to process hookup. hookup= [ {article} ] ", error=e)
            continue
    return result_articles


def process_single_article(article, isUpdate=False):
    try:
        id = DICT.get("_id", article)
        cat_attempt = DICT.get("category", article, False)
        if not isUpdate and cat_attempt:
            return article
        Log.d(f"process_single_article_v1: article={id}")
        title = DICT.get("title", article)
        description = DICT.get("description", article)
        body = DICT.get("body", article)
        content = Utils.combine_args_str(title, description, body)
        # -> Score/Match Content
        main_cats = Categorizer.categorizer_layer2_db_models(content)
        # sub_cats = TOPIC.sub_categorizer(content)
        # -> Remove matched topics with low scores
        # -> Main Variables
        highest_main_cat_name = LIST.get(0, main_cats)
        highest_main_score = LIST.get(1, main_cats)
        matched_main_terms = LIST.get(2, main_cats)
        # -> Sub Variables
        # highest_topic_name = LIST.get(0, sub_cats)
        # highest_score = LIST.get(1, sub_cats)
        # matched_terms = LIST.get(2, sub_cats)
        Log.d(f"Setting ALL Variables: article={id}")
        # -> MAIN CATEGORY
        article["category"] = highest_main_cat_name
        article["category_scores"] = matched_main_terms
        article["score"] = highest_main_score
        # -> SUB CATEGORY
        # article["sub_category"] = highest_topic_name
        # article["sub_category_scores"] = matched_terms
        # article["sub_score"] = highest_score
        return article
    except Exception as e:
        print(f"Failed: {e}")
        return article

