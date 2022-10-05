from F import DATE
from FCM.FQ import AO
from FCM.Jarticle import JQ
from FCM.Jarticle.jProvider import jPro

class harkPipe:
    DATE_RANGE = lambda gte, lte: {"$match": {"pub_date": {"$gte": DATE.TO_DATETIME(gte), "$lte": DATE.TO_DATETIME(lte)}}}
    CATEGORY = lambda categoryName: { "$match": { "category": { "$eq": categoryName } } }

class MetaFeeds:
    meta_v1 = lambda gte, lte: [
        # { "$match": { "pub_date": { "$gte": weekBack, "$lte": DATE.TO_DATETIME(today) } } },
        harkPipe.DATE_RANGE(gte, lte),
        { "$match": { "$or": [JQ.SEARCH_ALL_STRICT(search_term="virtual world"), JQ.SEARCH_ALL_STRICT(search_term="metaverse"), { "category": { "$eq": "metaverse" } }]}},
        { "$sort": { "pub_date": -1 }},
        { AO.LIMIT: 500 }
    ]
    meta_v2 = lambda gte, lte: [
        # { "$match": { "pub_date": { "$gte": weekBack, "$lte": DATE.TO_DATETIME(today) } } },
        harkPipe.DATE_RANGE(gte, lte),
        harkPipe.CATEGORY("metaverse"),
        { "$sort": {"pub_date": -1 } },
        {AO.LIMIT: 500}
    ]

class harkPro(jPro):

# "2022-09-01T00:00:00.000Z"#
    def get_meta_feed_v1(self, daysBack=7):
        today = DATE.get_now_month_day_year_str()
        weekBack = DATE.subtract_days(today, daysBack=daysBack, toString=False)
        m2 = MetaFeeds.meta_v1(weekBack, today)
        results = self.base_aggregate(m2)
        return results

    def get_meta_feed_v2(self, daysBack):
        today = DATE.get_now_month_day_year_str()
        weekBack = DATE.subtract_days(today, daysBack=daysBack, toString=False)
        m2 = MetaFeeds.meta_v2(weekBack, today)
        results = self.base_aggregate(m2)
        return results


if __name__ == '__main__':
    hk = harkPro()
    print(hk.get_meta_feed_v2())