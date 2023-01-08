import datetime
from F import DATE
from F.CLASS import FairClass
from FNLP.Engines.Words import Analyzers

BASE_MODEL = lambda word, score, in_webpages, out_webpages: {
                                                                "word": word,
                                                                "score": score,
                                                                "in_webpages": in_webpages,
                                                                "out_webpages": out_webpages
                                                              }
"""
word = name of word
count = number of times this word has been seen
score = algo for giving a word a score (seen, 

"""
WQ = lambda word: { "word": word }
TODAY = DATE.TO_DATETIME(DATE.mongo_date_today_str())
ENGLISH_WORD = lambda word, first_letter, letter_count, isFirstCapital: \
    {
    "word": word,
    "first_letter": first_letter,
    "letter_count": letter_count,
    "isFirstCapital": isFirstCapital,
    "updatedDate": TODAY
    }

class WordModel(FairClass):
    word: str = None
    count: int = 0
    score: int = 0
    # Analyzer
    first_letter: str = None
    letter_count: int = None
    isFirstCapital: bool = False
    # Extras
    dates_analyzed: int = 0
    webpages_analyzed: int = 0
    webpages_seen: int = 0
    category_scores = None
    createdDate: datetime = None
    updatedDate: datetime = TODAY

    def __init__(self, word, **kwargs):
        super().__init__(**kwargs)
        self.word = word
        self.run_analyzer()

    def run_analyzer(self):
        breakdown = Analyzers.analyze_word(self.word)
        self.fromJson(breakdown)
        return breakdown

    def update_score(self, new_score):
        pass

    def update_category_scores(self):
        pass

    def update_in_webpages(self):
        pass

    def update_out_webpages(self):
        pass

    def import_model(self):
        """ Load JSON Model """
        pass

    def export_model(self):
        """ Export Model as JSON"""
        return self.toJson(removeNone=True)

    def print_model(self):
        print(self.toJson())