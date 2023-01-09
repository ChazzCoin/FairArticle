import datetime

from F.LOG import Log
from FBrain.BrainModels.BaseModel import BaseBrain
from FBrain.BrainModels.Variables import BrainVariables
from FM.QueryHelper import O
from FNLP.Language import Words

from F import DATE, CONVERT, DICT, LIST
from FM.DBDatabase import DATABASE, COLLECTION
from FBrain.BrainDB.AnalyzedDB import AnalyzedWordsDB
from FBrain import BrainMath
from FNLP.Models.Content import ContentModel

Log = Log("ContentModel")
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

"""
BrainModel -> Gets existing data from Brain Database.
            - Imports/Merges in ContentModel.
            - Updates Brain Database.

ContentModel -> Facilitates each of the following models.
WordModel -> Breaks down All Words in content.
SentenceModel -> Breaks down All Sentences in content.
ParagraphModel -> Breaks down All Paragraphs in content.
"""
class BrainModel(BaseBrain, BrainVariables, ContentModel):
    db_brain = None
    awdb = AnalyzedWordsDB()
    # contentModel: ContentModel = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_brain_data()

    def get_brain_data(self):
        self.original_brain_counts = self.awdb.get_all_word_counts()
        self.original_brain_stop_counts = self.awdb.get_all_stop_word_counts()
        self.original_webpage_models = self.awdb.get_all_webpage_ids()

    def add_content_models(self, content_models:[ContentModel]):
        for model in Log.ProgressBarYielder(content_models, prefix="Merging in ContentModels..."):
            self.merge_model(model)

    def add_content_model(self, content_model:ContentModel):
        self.merge_model(content_model)

    # TODO: DON'T DO THIS HERE!
    def merge_with_brain(self):
        temp_counts = BrainMath.add_word_frequency_counts(self.original_brain_counts, self.counts)
        self.new_analyzed_counts = LIST.SORT_BY_DICT_KEY(temp_counts, "count")
        temp_stop_counts = BrainMath.add_word_frequency_counts(self.original_brain_stop_counts, self.stop_counts)
        self.new_analyzed_stop_counts = LIST.SORT_BY_DICT_KEY(temp_stop_counts, "count")

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



















































