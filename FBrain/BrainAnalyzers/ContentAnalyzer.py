from F.LOG import Log
from FBrain.BrainDB.ArticleProvider import Provider
from FBrain.BrainModels.BrainManager import BrainManager
from FNLP.LanguageManagers.ContentManager import ContentManager

"""
checklist

1. get webpages/article id's already looked at... "analyzed_webpages"
2. Query for webpages that do not have the _id of "analyzed_webpages"
3. Add Articles to ContentModel()
4. Get BrainModel()
4. Run Analyzer
5. Merge ContentModel with BrainModel
6. Update Brain

- ContentModel
- BrainModel
- BrainDB
- BrainMath
"""

"""
Analyzer 
Manager
Engine

"""

Log = Log("Word-Analyzer")
# Database Setup
p = Provider()
articles = p.get_articles_not_analyzed(limit=10000)

""" Analyzing Content from Articles """
cModel1 = ContentManager()
cModel1.add_webpages(articles)
cModel1.run_analyzer()

""" Merge Analyzed Content with BrainDatan"""
brainManager = BrainManager(contentManager=cModel1)
brainManager.run()
