from FM.DBDatabase import DBDatabase
from FM.QueryHelper import Q


class Provider(DBDatabase):
    db_brain: DBDatabase = None
    db_research: DBDatabase = None

    def get_articles(self, limit=100):
        article_collection = self.db_research.collection("articles")
        return article_collection.base_query({}, limit=limit)

    def get_articles_not_analyzed(self, limit=100):
        article_collection = self.db_research.collection("articles")
        webpage_id_collection = self.db_brain.collection("analyzed_webpages")
        webpages_ids = webpage_id_collection.base_query({}, limit=0)
        query = self.prepare_webpage_ids(webpages_ids)
        return article_collection.base_query(query, limit=limit)

    @staticmethod
    def prepare_webpage_ids(webpage_ids: list):
        ids = []
        id_queries = []
        for webpage in webpage_ids:
            temp_id = webpage["_id"]
            single_query = {"_id": Q.NOT_EQUALS(temp_id)}
            ids.append(temp_id)
            id_queries.append(single_query)
        return Q.OR(id_queries)