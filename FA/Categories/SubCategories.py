
MAX_WEIGHT = 200
HIGH_WEIGHT = 130
MIDDLE_WEIGHT = 75
LOW_WEIGHT = 25
MINI_WEIGHT = 10
NANO_WEIGHT = 3

class SubCategories:

    government = { "government": 100, "taxes": 100, "politics": 100, "politician": 100, "politicians": 100,
                   "senate": 100, "congress": 100, "house of representatives": 100, "dc": 10, "washington": 10,
                   "washington dc": 30, "capital hill": 10, "white house": 50 }
    finance = { "finance": 100, "money": 50, "economy": 100, "supply": MIDDLE_WEIGHT, "demand": LOW_WEIGHT,
                "supply and demand": HIGH_WEIGHT, "jobs": LOW_WEIGHT, "labor market": MIDDLE_WEIGHT }
    news = { "news": 100, "article": 100, "": 100 }
    social = { "twitter": 100, "tweet": 100, "reddit": 100 }
    engineering = { "engineering": 100, "architecture": 100, "architect": 100 }
    humanities = { "humanities": 100, "green": 5, "": 100 }
    history = { "history": 100, "historic": 100, "historical": 100, "historian": 100, "historians": 100 }
    sports = { "soccer": 100, "football": 100, "basketball": 100, "sports": 100 }

    @staticmethod
    def get_sub_category_names():
        test = SubCategories.__dict__.keys()
        variables = []
        for item in test:
            if str(item).startswith("__"):
                continue
            elif str(item).startswith("keys"):
                continue
            elif str(item).__contains__("_"):
                continue
            else:
                variables.append(item)
        return variables