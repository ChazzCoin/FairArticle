from F import DICT, LIST
from F.LOG import Log
from FM.DBDatabase import DBDatabase
from FNLP.Engines.Words import Frequency
from FBrain.JHelpers import ART
from FBrain.BrainModels import WordModel

MODEL = WordModel()

Log = Log("Word-Analyzer")
# Database Setup
db = DBDatabase().connect("192.168.1.180", 27017).database("research")
collection = db.collection("articles")

""" Grabbing Articles """
# -> Get Articles/Main Content
# Log.ProgressBar(0, 5, prefix="Downloading Articles")
# todo: add date and such to fairmongo
# todo: organize this as well by date...
articles = collection.base_query({ "category": "Unknown" }, limit=20000)
# articles = LIST.flatten(articlesOne, articlesTwo, articlesThree, articlesFour, articlesFive)

""" Extracting Content from Articles """
# -> Convert Articles to Raw Content
Log.i(f"Extracting Content from {len(articles)} Articles...")
# article_contents = []
# todo: analyze each article, update result object one by one...
# todo: so merge this loop with the progress bar yielder!
# for arty in articles:
#     # todo: take out -> [ date, category, source ]
#     article_contents.append(ART.extract_content(arty))

""" Analyzing Content from Articles """
# # -> Analyze All Content
# Log.i("Analyzing Content...")
# raw_results = []
# all_stop_scores = []
# all_unique_words = []
#
# for ac in Log.ProgressBarYielder(article_contents, prefix="Analyzing"):
#     temp = Frequency.analyze_content(ac)
#     temp_stop_scores = DICT.get("stop_scores", temp, None)
#     temp_unique_words = DICT.get("unique_words", temp, None)
#     all_unique_words.append(temp_unique_words)
#     if temp_stop_scores:
#         all_stop_scores.append(temp_stop_scores)
#     raw_results.append(temp)
#
# all_unique_words = LIST.flatten(all_unique_words)
# unique_words = LIST.remove_duplicates(all_unique_words)


def analyze_articles(articles):
    Log.i("Analyzing Content...")
    raw_results = []
    all_stop_scores = []
    all_unique_words = []

    # Loop Articles
    for current_article in Log.ProgressBarYielder(articles, prefix="Analyzing"):
        # 1. Extract Content
        article_contents = ART.extract_content(current_article)
        # 2. Analyze Content
        temp = Frequency.analyze_content(article_contents)
        # 3. Prepare Results
        temp_stop_scores = DICT.get("stop_scores", temp, None)
        temp_unique_words = DICT.get("unique_words", temp, None)
        all_unique_words.append(temp_unique_words)
        if temp_stop_scores:
            all_stop_scores.append(temp_stop_scores)
        raw_results.append(temp)


"""
    -> Creating the Report <-
"""
# -> SUM Stop Scores
Log.i("Summing up the report...")
raw_stop_scores = Frequency.combine_add_word_frequency_counts(all_stop_scores)
total_stop_scores = DICT.order_by_value(raw_stop_scores)
top_stop_scores = []
i = 0
for key in total_stop_scores:
    if i >= 20:
        break
    top_stop_scores.append((key, total_stop_scores[key]))
    i += 1

# -> SUM All Counted Words
total_word_count = 0
for r in raw_results:
    temp_count = DICT.get("word_count", r, None)
    total_word_count += temp_count

""" Print Report Results """
print("Total Articles Analyzed:", len(articles))
print("Unique Words Analyzed", len(unique_words))
print("Total Words Counted:", total_word_count)
print("Most Frequent Words by Count:")
for item in top_stop_scores:
    print(item)

