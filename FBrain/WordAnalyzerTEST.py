from F.LOG import Log
from FM.DBDatabase import DBDatabase
from FBrain.JModel.Content import ContentModel

Log = Log("Word-Analyzer")
# Database Setup
db = DBDatabase().connect("192.168.1.180", 27017).database("research")
collection = db.collection("articles")

""" Grabbing Articles """
# -> Get Articles/Main Content
# todo: add date and such to fairmongo
# todo: organize this as well by date...
articles = collection.base_query({ }, limit=100)
# articles = LIST.flatten(articlesOne, articlesTwo, articlesThree, articlesFour, articlesFive)
""" Analyzing Content from Articles """
cModel = ContentModel()
cModel.add_webpages(articles)
cModel.run_analyzer(saveToBrain=True)
print(cModel)



