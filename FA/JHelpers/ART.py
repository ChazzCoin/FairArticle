from datetime import datetime
import F
from F import DICT, LIST

def remove_duplicate_articles(listOfArticles:[]):
    cleaned_list = []
    for item in listOfArticles:
        newItem = DICT.remove_key_value("_id", item)
        cleaned_list.append(newItem)
    noDups = LIST.remove_duplicates(cleaned_list)
    return noDups

def get_content(article):
    title = DICT.get("title", article, False)
    body = DICT.get("body", article, False)
    description = DICT.get("description", article, False)
    content = F.combine_args_str(title, body, description)
    return content

