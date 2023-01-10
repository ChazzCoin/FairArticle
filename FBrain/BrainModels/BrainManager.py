from F.LOG import Log
from FBrain.BrainDB.BrainData import BrainData
from FBrain.BrainModels.BaseModel import BaseBrain
from FBrain.BrainModels.Variables import BrainVariables

from FBrain import BrainMath
from FNLP.LanguageManagers import ContentManager, WordsManager

Log = Log("BrainManager")


"""
BrainModel -> Gets existing data from Brain Database.
            - Imports/Merges in ContentModel.
            - Updates Brain Database.

ContentModel -> Facilitates each of the following models.
WordModel -> Breaks down All Words in content.
SentenceModel -> Breaks down All Sentences in content.
ParagraphModel -> Breaks down All Paragraphs in content.
"""
class BrainManager(BaseBrain, BrainVariables):
    brainData: BrainData = BrainData()
    contentManager: ContentManager.ContentManager = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        self.prepare_for_brain()
        self.update_brain_database()

    def add_content_manager(self, content_manager:[ContentManager]):
        self.contentManager = content_manager

    def prepare_for_brain(self):
        mw: WordsManager.WordsManager = self.contentManager.model_words
        self.analyzed_words_for_db = BrainMath.add_word_frequency_counts(self.brainData.analyzed_words, mw.overall_counts)
        self.analyzed_stop_words_for_db = BrainMath.add_word_frequency_counts(self.brainData.analyzed_stop_words, mw.overall_stop_counts)
        self.analyzed_webpages_for_db = mw.webpage_models

    def update_brain_database(self):
        self.brainData.db.addUpdate_analyzed_words(self.analyzed_words_for_db, "analyzed_words")
        self.brainData.db.addUpdate_analyzed_words(self.analyzed_stop_words_for_db, "analyzed_stop_words")
        self.brainData.db.addUpdate_webpage_references(self.analyzed_webpages_for_db)


