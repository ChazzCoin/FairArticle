from datetime import datetime
from F import DICT, LIST

def remove_duplicate_articles(listOfArticles:[]):
    cleaned_list = []
    for item in listOfArticles:
        newItem = DICT.remove_key_value("_id", item)
        cleaned_list.append(newItem)
    noDups = LIST.remove_duplicates(cleaned_list)
    return noDups
