
from F.LOG import Log
from FBrain.BrainDB import DB
from FBrain.BrainModels.Brain import BrainModel
# from FBrain.BrainModels.Content import ContentModel
from FM.QueryHelper import O, Q
from FNLP.Models.Content import ContentModel

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

Log = Log("Word-Analyzer")
# Database Setup

client = DB.CLIENT("192.168.1.180", 27017)
db_research = DB.get_research_db(client)
collection_articles = db_research.collection("articles")
db_brain = DB.get_brain_db(client)
collection_webpages = db_brain.collection("analyzed_webpages")

""" Grabbing Articles """
# -> Get Articles/Main Content
# todo: add date and such to fairmongo
# todo: organize this as well by date...
webpage_refs = collection_webpages.base_query({}, limit=0)
ids = []
id_queries = []
if webpage_refs:
    for webpage in webpage_refs:
        temp_id = webpage["_id"]
        single_query = {"_id": Q.NOT_EQUALS(temp_id)}
        ids.append(temp_id)
        id_queries.append(single_query)
    final_query = Q.OR(id_queries)
else:
    final_query = {}



articles = collection_articles.base_query(final_query, limit=5)
articles2 = collection_articles.base_query(final_query, limit=5)
# articles = LIST.flatten(articlesOne, articlesTwo, articlesThree, articlesFour, articlesFive)
""" Analyzing Content from Articles """
cModel1 = ContentModel()
cModel1.add_webpages(articles)
cModel1.run_analyzer()


cModel2 = ContentModel()
cModel2.add_webpages(articles2)
cModel2.run_analyzer()

cModel1.absorb_content_model(cModel2)
print(cModel1)

brainModel = BrainModel()
brainModel.add_content_model(cModel1)
brainModel.merge_with_brain()
print(brainModel)
