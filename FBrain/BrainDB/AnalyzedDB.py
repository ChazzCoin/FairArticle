from FM.DBDatabase import DBDatabase
from FM.QueryHelper import O, Q

"""
    - 1. Save all words and their count.
        "analyzed_words" collection
    - 2. Get all words and their count.
        "analyzed_words" collection
        "word" - "word_count" - "word_score"
"""
ANALYZED_WEBPAGES = "analyzed_webpages"
ANALYZED_WORDS = "analyzed_words"
ANALYZED_STOP_WORDS = "analyzed_stop_words"

class AnalyzedWordsDB:
    db_brain = None
    # db_collection = None
    model_categories = {}
    analyzed_words = None
    analyzed_stop_words = None
    analyzed_webpages = None


    def __init__(self):
        self.connect_to_brain()

    def connect_to_brain(self):
        self.db_brain = DBDatabase().connect("192.168.1.180", 27017).database("brain")
        self.analyzed_words = self.db_brain.collection(ANALYZED_WORDS)
        self.analyzed_stop_words = self.db_brain.collection(ANALYZED_STOP_WORDS)
        self.analyzed_webpages = self.db_brain.collection(ANALYZED_WEBPAGES)

    def addUpdate_word_counts(self, word_counts:[{}], collection_name:str):
        collection = self.db_brain.collection(collection_name)
        return collection.addUpdate_records(word_counts)

    def save_word_counts(self, word_counts:[{}], collection_name:str):
        collection = self.db_brain.collection(collection_name)
        return collection.add_records(word_counts)

    def get_all_word_counts(self):
        return self.analyzed_words.base_query({}, limit=0)

    def get_all_stop_word_counts(self):
        return self.analyzed_stop_words.base_query({}, limit=0)

    def get_all_webpage_ids(self):
        return self.analyzed_webpages.base_query({}, limit=0)

    def addUpdate_webpage_references(self, webpage_ids):
        for model in webpage_ids:
            findQuery = { "_id": O.TO_OBJECT_ID(model["webpage_id"]) }
            self.analyzed_webpages.update_record(findQuery, model)





if __name__ == '__main__':
    results = AnalyzedWordsDB().get_all_word_counts()
    print(results)