from F import LIST, DICT, DATE
from FM.DBDatabase import DBDatabase


"""
    - 1. Save all words and their count.
        "analyzed_words" collection
    - 2. Get all words and their count.
        "analyzed_words" collection
        "word" - "word_count" - "word_score"
"""


class AnalyzedWords:
    db_brain = None
    # db_collection = None
    model_categories = {}

    def __init__(self):
        self.connect_to_brain()

    def connect_to_brain(self):
        self.db_brain = DBDatabase().connect("192.168.1.180", 27017).database("brain")
        # self.db_collection = self.db_brain.collection("models")

    def addUpdate_word_counts(self, word_counts:[{}], collection_name:str):
        collection = self.db_brain.collection(collection_name)
        return collection.addUpdate_records(word_counts)
    def save_word_counts(self, word_counts:[{}], collection_name:str):
        collection = self.db_brain.collection(collection_name)
        return collection.add_records(word_counts)

    def get_all_word_counts(self):
        collection = self.db_brain.collection("analyzed_words")
        return collection.base_query({}, limit=0)


if __name__ == '__main__':
    results = AnalyzedWords().get_all_word_counts()
    print(results)