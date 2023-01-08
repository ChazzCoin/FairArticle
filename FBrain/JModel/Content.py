import datetime

from F.LOG import Log
from FNLP.Language import Words

from F import DATE, CONVERT, DICT, LIST
from F.CLASS import FairClass
from FNLP.Engines.Words import Analyzers
from FM.DBDatabase import DATABASE, COLLECTION

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

# TODO: GET ALL WORD COUNTS FROM BRAIN
#   MERGE NEW COUNT.
#   UPDATE BRAIN.
class ContentModel(FairClass):
    # Internal Only
    webpage_models = []
    # Main
    contents: list = []
    tokens: list = []
    tokens_by_content: list = []
    score: int = 0
    # Analyzer
    words_counted: int = None
    unique_words: list = None
    unique_words_count: int = None
    scores: dict = None
    stop_scores: dict = None
    top_x_words: dict = None
    # Extras
    dates_analyzed: list = []
    dates_analyzed_count: int = 0
    webpages_analyzed_count: int = 0
    category_scores: dict = {}
    createdDate: datetime = None
    updatedDate: datetime = TODAY

    def run_analyzer(self, saveToBrain=False):
        breakdown = Analyzers.analyze_content(self.tokens)
        self.fromJson(breakdown)
        self.unique_words_count = len(self.unique_words)
        if saveToBrain:
            self.finish_and_save_to_the_brain()
        return breakdown

    def add_webpages(self, webpages:list):
        for ac in Log.ProgressBarYielder(webpages, prefix="Preparing Content..."):
            self.add_webpage(ac)

    def add_webpage(self, webpage:dict):
        # Internal for The Brain
        id = DICT.get("_id", webpage, default="Unknown")
        new_date = DICT.get("pub_date", webpage, None)
        model = { "webpage_id": id, "webpage_date": new_date, "updatedDate": TODAY }
        self.webpage_models.append(model)
        # Extract Values only from Dict/Obj
        new_content = CONVERT.dict_TO_List_OF_Values(webpage)
        self.contents.append(new_content)
        # Create and Add Tokens
        new_tokens = Words.to_words_v2(str(new_content))
        self.tokens_by_content.append(new_tokens)
        # Add Date
        if new_date:
            self.dates_analyzed.append(new_date)
        # Category Scores
        # cat_scores = DICT.get("category_scores", webpage, None)
        # if cat_scores:
        #     self.category_scores = DICT.add_word_count(self.category_scores, cat_scores)
        self.post_add_webpage_work()

    def post_add_webpage_work(self):
        self.tokens = LIST.flatten(self.tokens_by_content)
        self.dates_analyzed = LIST.remove_duplicates(self.dates_analyzed)
        self.dates_analyzed_count = len(self.dates_analyzed)
        self.webpages_analyzed_count = len(self.contents)

    def finish_and_save_to_the_brain(self):
        self.addUpdate_webpage_references()

    """ Update The Brain """

    def addUpdate_webpage_references(self):
        db = DATABASE("192.168.1.180", "brain")
        collection = db.collection("analyzed_webpages")
        for model in self.webpage_models:
            findQuery = { "webpage_id": model["webpage_id"] }
            collection.update_record(findQuery, model)
        db.client.close()

    """ Import/Export """

    def import_model(self, obj:dict):
        """ Load JSON Model """
        self.fromJson(obj)

    def export_model(self):
        """ Export Model as JSON"""
        return self.toJson(removeNone=True)

    def print_model(self):
        print(self.toJson())


"""
    -> Merge two ContentModels
"""



















































