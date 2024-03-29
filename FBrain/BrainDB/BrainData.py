from FBrain.BrainDB.AnalyzedDB import AnalyzedDB
from FBrain.BrainModels.MongoRecord import Records


class BrainData:
    db = AnalyzedDB()
    analyzed_webpages = Records()
    analyzed_words = Records()
    # smart_analyzed_words = Records()
    analyzed_words_by_date = Records()
    analyzed_stop_words = Records()
    analyzed_sentences = Records()

    def __init__(self):
        self.init_data()

    def init_data(self):
        self.analyzed_words.import_records(self.analyzed_words)
        self.analyzed_words_by_date.import_records(self.db.get_all_analyzed_words_by_date())
        # self.analyzed_stop_words = self.db.get_analyzed_stop_words()
        # self.analyzed_webpages = self.db.get_analyzed_webpages()

# b = BrainData()
# b.smart_analyzed_words.collection_name = "analyzed_words_fakkkke"
# first = b.smart_analyzed_words[0]
# ex = first.export()
# print(ex)