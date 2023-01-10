from FBrain.BrainDB.AnalyzedDB import AnalyzedDB

class BrainData:
    db = AnalyzedDB()
    analyzed_webpages = []
    analyzed_words = []
    analyzed_stop_words = []
    analyzed_sentences = []

    def __init__(self):
        self.init_data()

    def init_data(self):
        self.analyzed_words = self.db.get_analyzed_words()
        self.analyzed_stop_words = self.db.get_analyzed_stop_words()
        self.analyzed_webpages = self.db.get_analyzed_webpages()