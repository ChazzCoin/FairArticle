from datetime import datetime

from FDate import DATE

from FSON import DICT
from FLog.LOGGER import Log

Log = Log("FArt.ART")

def sort_articles_by_date(articles, toDict=True):
    by_date_dict = {}
    with_dates = []
    without_dates = []

    for art in articles:
        pDate = DICT.get("published_date", art, False)
        if not pDate:
            without_dates.append(art)
            continue
        with_dates.append(art)
    sorted_articles = sorted(with_dates, key=lambda k: k.get("published_date"), reverse=True)

    if not toDict:
        return sorted_articles

    # today = DATE.mongo_date_today_str()
    # range_of_dates = DATE.get_range_of_dates_by_day(today, 20)

    for i in sorted_articles:
        current_date = DICT.get("published_date", i, False)
        by_date_dict = DICT.add_key_value(current_date, i, by_date_dict, forceListAsValue=True)

    return by_date_dict

def sort_articles_by_score(articles, reversedOrder=True):
    Log.v(f"sort_hookups_by_score: IN: {articles}")
    sorted_articles = sorted(articles, key=lambda k: k.get("score"), reverse=reversedOrder)
    return sorted_articles

def remove_duplicate_articles():
    pass