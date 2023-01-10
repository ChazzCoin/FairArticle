from FM.DBDatabase import DBDatabase
from FM.QueryHelper import Q


class Provider(DBDatabase):
    db_core = None
    db_brain: DBDatabase = None
    db_research: DBDatabase = None
    article_collection = None

    def __init__(self):
        super().__init__()
        self.connect_to_research()

    def connect_to_research(self):
        self.db_core = DBDatabase().connect("192.168.1.180", 27017)
        self.db_research = self.db_core.database("research")
        self.db_brain = self.db_core.database("brain")
        self.article_collection = self.db_research.collection("articles")

    def get_articles(self, limit=100):
        return self.article_collection.base_query({}, limit=limit)

    def get_articles_not_analyzed(self, limit=100):
        webpage_id_collection = self.db_brain.collection("analyzed_webpages")
        webpages_ids = webpage_id_collection.base_query({}, limit=0)
        if not webpages_ids:
            temp = self.db_core.database("research").collection("articles").base_query({}, limit=limit)
            return temp
        ids = self.prepare_webpage_ids(webpages_ids)
        return self.db_core.database("research").collection("articles").base_query({"_id": {"$nin": ids}}, limit=limit)

    @staticmethod
    def prepare_webpage_ids(webpage_ids: list):
        ids = []
        id_queries = []
        for webpage in webpage_ids:
            temp_id = webpage["_id"]
            single_query = {"_id": Q.NOT_EQUALS(temp_id)}
            ids.append(temp_id)
            id_queries.append(single_query)
        return ids