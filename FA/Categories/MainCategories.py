# from Utils import FILE
"""
-> Rules
1. Each "topic" has 3 attributes, a. search_terms b. weighted_terms c. rss_feeds
2. Each "topics" attribute starts with the topic name, underscores only.
"""
extended_stop_words = ["with", "more", "s", "has", "have", "they", "this", "their", "was", "not", "said", "also",
                       "most", "but", "from", "whether", "so", "ways", "if", "were", "have", "my", "being", "re", "what",
                       "where", "many", "other", "t", "i", "than", "had", "who", "amoung", "get", "say", "could", "way"]
# meta_names = FILE.load_dict_from_file("meta_names")
# -------------------------------------> CATEGORIES AND THEIR KEY-TERMS <-------------------------------------------- #

MAX_WEIGHT = 200
HIGH_WEIGHT = 130
MIDDLE_WEIGHT = 75
LOW_WEIGHT = 25
MINI_WEIGHT = 10
NANO_WEIGHT = 3

class MainCategories:
    # -> If any lists are added, add here.
    keys = ["search_terms", "weighted_terms", "rss_feeds", "secondary_weighted_terms", "url_sources"]

    def get_var(self, var_name):
        """  GETTER HELPER  """
        return self.__getattribute__(var_name)

    @staticmethod
    def combine_var_name(topic, term):
        return topic + "_" + term

    ####################################################################################################################
    # -> 0. General <-
    ####################################################################################################################
    general = "General"
    general_search_terms = ["business", "government", "federal government", "white house", "politics", "global news",
                            "news", "united states economy", "global economy", "president"]
    
    general_weighted_terms = {"thousand": LOW_WEIGHT,
                              "million": LOW_WEIGHT,
                              "billion": MIDDLE_WEIGHT,
                              "trillion": MIDDLE_WEIGHT,
                              "space": MINI_WEIGHT,
                              "mainstream": MINI_WEIGHT,
                              "property": NANO_WEIGHT,
                              "network": MINI_WEIGHT,
                              "future": LOW_WEIGHT,
                              "crowdfunding": NANO_WEIGHT,
                              "economy": MINI_WEIGHT,
                              "market valuation": MINI_WEIGHT,
                              "Metrics": NANO_WEIGHT,
                              "market action": NANO_WEIGHT,
                              "dominance": NANO_WEIGHT,
                              "assets": MINI_WEIGHT,
                              "Drops": NANO_WEIGHT,
                              "Dips": NANO_WEIGHT,
                              "value proposition": MINI_WEIGHT,
                              "fluctuates": NANO_WEIGHT,
                              "portfolio": NANO_WEIGHT,
                              "crash": NANO_WEIGHT,
                              "optimistic": NANO_WEIGHT,
                              "projections": NANO_WEIGHT,
                              "hedge fund": NANO_WEIGHT,
                              "hedgefund": NANO_WEIGHT,
                              "holders": NANO_WEIGHT,
                              "holder": NANO_WEIGHT,
                              "owns": NANO_WEIGHT,
                              "fund": NANO_WEIGHT,
                              "game": NANO_WEIGHT,
                              "gaming": NANO_WEIGHT,
                              "market capitalization": LOW_WEIGHT,
                              "developer": NANO_WEIGHT,
                              "development": NANO_WEIGHT,
                              "develop": NANO_WEIGHT,
                              "engineer": NANO_WEIGHT,
                              "engineering": NANO_WEIGHT,
                              "4g": MINI_WEIGHT,
                              "5g": MINI_WEIGHT,
                              "6g": MINI_WEIGHT,
                              "fiber": MINI_WEIGHT,
                              "optical": MINI_WEIGHT,
                              "fiber optic": MINI_WEIGHT,
                              "business": NANO_WEIGHT,
                              "businesses": NANO_WEIGHT,
                              "meeting": NANO_WEIGHT,
                              "meetings": NANO_WEIGHT,
                              "committee": NANO_WEIGHT,
                              "fed": MINI_WEIGHT,
                              "the fed": MINI_WEIGHT,
                              "federal": NANO_WEIGHT,
                              "federal reserve": LOW_WEIGHT,
                              "bull market": NANO_WEIGHT,
                              "bear market": NANO_WEIGHT,
                              "inflation": MINI_WEIGHT,
                              "deflation": MINI_WEIGHT,
                              "plunges": MINI_WEIGHT,
                              "leaked": MIDDLE_WEIGHT,
                              "announcement": MINI_WEIGHT}
    
    general_rss_feeds = ["http://feeds.marketwatch.com/marketwatch/topstories/",
                         "http://www.infoworld.com/index.rss",
                         "http://www.itworldcanada.com/feed",
                         "http://www.macworld.com/index.rss",
                         "http://www.roadtovr.com/feed",]

    ####################################################################################################################
    # -> 3. Weed <-
    ####################################################################################################################
    weed = "Weed"
    weed_search_terms = ['legalization', 'cannabis stock', 'cannabinoid-therapeutics', 'cannabinoid',
                         'medicinal marijuana', 'cannabis investors', 'pot stock', 'cannabis legalization',
                         'federal decriminalization', 'marijuana stocks', 'marijuana legalization bills',
                         'cannabis market', 'cannabis', 'weed', 'marijuana']

    weed_weighted_terms = {"legalization": MIDDLE_WEIGHT,
                           "decriminalization": MIDDLE_WEIGHT,
                           "cannabinoid": MAX_WEIGHT,
                           "cannabis": MAX_WEIGHT,
                           "marijuana": MAX_WEIGHT,
                           "pot": LOW_WEIGHT,
                           "weed": MAX_WEIGHT,
                           "stock": NANO_WEIGHT,
                           "therapeutics": LOW_WEIGHT,
                           "medicinal": HIGH_WEIGHT}

    weed_rss_feeds = []

    ####################################################################################################################
    # -> 3. Stocks <-
    ####################################################################################################################
    stocks = "Stocks"
    stocks_search_terms = ['merge', 'merger', 'acquisition', 'stepping down', 'IPO', 'partnering', 'stocks', 'economy']
    
    stocks_weighted_terms = {'merge': MINI_WEIGHT,
                             'merger': MIDDLE_WEIGHT,
                             'acquisition': HIGH_WEIGHT,
                             'stepping down': MIDDLE_WEIGHT,
                             'IPO': MIDDLE_WEIGHT,
                             'partnering': MIDDLE_WEIGHT,
                             'ROI': LOW_WEIGHT,
                             'Incentivize': LOW_WEIGHT,
                             'Monetize': MIDDLE_WEIGHT,
                             'Deliverable': MIDDLE_WEIGHT,
                             'Margin': MIDDLE_WEIGHT, 
                             'Accounts Payable': MIDDLE_WEIGHT,
                             'Accounts Receivable': LOW_WEIGHT,
                             'Capital': LOW_WEIGHT,
                             'Fixed Costs': MIDDLE_WEIGHT,
                             'Variable Costs': MIDDLE_WEIGHT, 
                             'Gross': MINI_WEIGHT,
                             'Net': MINI_WEIGHT,
                             'Benchmarking': LOW_WEIGHT,
                             'KPI': LOW_WEIGHT,
                             'Metrics': LOW_WEIGHT,
                             'Performance Review': MIDDLE_WEIGHT, 
                             'R&D': MIDDLE_WEIGHT, 
                             'B2B': MIDDLE_WEIGHT,
                             'B2C': LOW_WEIGHT,
                             'B2G': LOW_WEIGHT,
                             'Scalable': LOW_WEIGHT,
                             'Responsive Design': MIDDLE_WEIGHT, 
                             'Core Competency': LOW_WEIGHT, 
                             'Niche Market': MIDDLE_WEIGHT,
                             'Marketing': LOW_WEIGHT,
                             'Market Research': LOW_WEIGHT,
                             'Market Penetration': MIDDLE_WEIGHT,
                             'Inbound Marketing': MIDDLE_WEIGHT, 
                             'Assets': MIDDLE_WEIGHT,
                             'Liabilities': MIDDLE_WEIGHT,
                             'Revenue': LOW_WEIGHT,
                             'Expenses': LOW_WEIGHT,
                             'Balance sheet': MIDDLE_WEIGHT, 
                             'Net profit': MIDDLE_WEIGHT, 
                             'Net loss': HIGH_WEIGHT,
                             'Profit margin': MIDDLE_WEIGHT,
                             'Cash flow': MIDDLE_WEIGHT,
                             'cash flow': MIDDLE_WEIGHT,
                             'Depreciation': LOW_WEIGHT, 
                             'Fixed Asset': LOW_WEIGHT,
                             'Gross Profit': HIGH_WEIGHT,
                             'Intangible Asset': MINI_WEIGHT,
                             'Liquidity': LOW_WEIGHT,
                             'Profit & Loss': MIDDLE_WEIGHT,
                             'Shareholders Equity': MAX_WEIGHT,
                             'Annual Percentage': MINI_WEIGHT,
                             'Appraisal': MINI_WEIGHT,
                             'Balloon Loan': MIDDLE_WEIGHT,
                             'Bankruptcy': MIDDLE_WEIGHT,
                             'Bootstrapping': LOW_WEIGHT, 
                             'Business Credit': MIDDLE_WEIGHT,
                             'Collateral': MINI_WEIGHT,
                             'Credit Limit': MIDDLE_WEIGHT,
                             'Debt Consolidation': MIDDLE_WEIGHT,
                             "sell off": MIDDLE_WEIGHT,
                             "target market": MINI_WEIGHT,
                             "stockholder": MAX_WEIGHT,
                             "stockholders": MAX_WEIGHT,
                             "surges": LOW_WEIGHT,
                             "surge": MINI_WEIGHT,
                             "market capitalization": HIGH_WEIGHT,
                             "Change management": HIGH_WEIGHT,
                             "Lay off": HIGH_WEIGHT,
                             "dow jones": MAX_WEIGHT,
                             "dow": MIDDLE_WEIGHT, 
                             "s&p500": MAX_WEIGHT,
                             "nasdaq": MAX_WEIGHT,
                             "nyse": MAX_WEIGHT,
                             "shareholders": MAX_WEIGHT
                             }
    
    stocks_rss_feeds = ["http://feeds.marketwatch.com/marketwatch/topstories/", "https://seekingalpha.com/feed.xml",
                        "https://www.investing.com/rss/news_25.rss", "https://blog.wallstreetsurvivor.com/feed/",
                        "https://stockstotrade.com/blog/feed/",
                        "https://www.cnbc.com/id/LOW_WEIGHT409666/device/rss/rss.html?x=1",
                        "http://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms",
                        "https://mebfaber.com/feed/", "http://welcome.philstockworld.com/feed/",
                        "https://www.reddit.com/r/stocks/.rss"]
    stocks_reddit_communities = ['wallstreetbets', 'WallStreetbetsELITE', 'deepfuckingvalue', 'stocks', 'investing',
                                 'stockmarket']
    stocks_twitter_users = ['mcuban', 'elonmusk', 'PeterLBrandt', 'CNBC', 'SJosephBurns', 'elerianm', 'IBDinvestors',
                            'jimcramer', 'bespokeinvest', 'wsbmod', 'galgitron', 'thevrsoldier', 'glewmecorp']
    ####################################################################################################################
    # -> X. German <-
    ####################################################################################################################

    german = "German"
    german_search_terms = ['merge', 'merger', 'acquisition', 'stepping down', 'IPO', 'partnering']
    german_weighted_terms = {'merge': MINI_WEIGHT, 'merger': MINI_WEIGHT, 'acquisition': MINI_WEIGHT, 'stepping down': MINI_WEIGHT, 'IPO': MINI_WEIGHT, 'partnering': MINI_WEIGHT,
                             "Change management": MINI_WEIGHT, "Lay off": MINI_WEIGHT, "Kündigungen": MINI_WEIGHT, "Freiberufler": MINI_WEIGHT,
                             "Freelancer": MINI_WEIGHT, "Interim": MINI_WEIGHT, "Interim manager": MINI_WEIGHT, "Accounting": MINI_WEIGHT,
                             "Buchführung": MINI_WEIGHT, "Finance": MINI_WEIGHT, "Finanzen": MINI_WEIGHT, "Expansion": MINI_WEIGHT, "Stellenabbau": MINI_WEIGHT,
                             "Stellenaufbau": MINI_WEIGHT, "Einkauf": MINI_WEIGHT, "Michael page": MINI_WEIGHT, "Robert half": MINI_WEIGHT, "Hays": MINI_WEIGHT,
                             "Human Resources": MINI_WEIGHT, "HR": MINI_WEIGHT, "International": MINI_WEIGHT, "Business": MINI_WEIGHT, "Unternehmen": MINI_WEIGHT,
                             'BILANZ': 2, 'VERMÖGENSWERTE': 2, 'VERBINDLICHKEITEN': NANO_WEIGHT, 'EIGENKAPITAL': NANO_WEIGHT, 'EINNAHMEN': NANO_WEIGHT, 'AUFWAND': NANO_WEIGHT,
                             'GEWINN': 2, 'NETTOVERLUST': 2, 'KAPITALFLUSSRECHNUNG': NANO_WEIGHT, 'GEWINNMARGE': NANO_WEIGHT, 'VARIABLE KOSTEN': NANO_WEIGHT,
                             'Geld verdienen': NANO_WEIGHT, 'BARGELDFLUSS': 2, 'FESTKOSTEN': 2, 'Fixkosten': NANO_WEIGHT, 'Netto': NANO_WEIGHT, 'KPI': NANO_WEIGHT,
                              'Kernkompetenz': NANO_WEIGHT, 'Lieferbar': 2, 'Kreditorenbuchhaltung': 2, 'Debitorenbuchhaltung': NANO_WEIGHT,
                             'Skalierbar': NANO_WEIGHT, 'Leistungsüberprüfung': NANO_WEIGHT, 'Alleinstellungsmerkmal': NANO_WEIGHT}

    german_rss_feeds = ["https://www.wiwo.de/contentexport/feed/rss/schlagzeilen",
                        "https://www.wiwo.de/contentexport/feed/rss/themen",
                        "https://www.wiwo.de/contentexport/feed/rss/unternehmen",
                        "https://www.wiwo.de/contentexport/feed/rss/finanzen",
                        "https://rss.dw.com/xml/rss-de-all",
                        "https://rss.dw.com/xml/rss-de-eco",
                        "https://www.wirtschaftskurier.de/titelthema.html?type=9818",
                        "http://www.wirtschaftskurier.de/unternehmen.html?type=9818",
                        "http://www.wirtschaftskurier.de/finanzen.html?type=9818",
                        "http://www.stern.de/feed/standard/wirtschaft/",
                        "https://www.iwkoeln.de/rss/arbeitsmarkt.xml",
                        "https://www.iwkoeln.de/rss/bildung-und-fachkraefte.xml",
                        "https://www.spiegel.de/international/index.rss", "http://newsfeed.zeit.de/index",
                        "https://www.thelocal.de/feeds/rss.php", "https://www.deutschland.de/en/feed-news/rss.xml",
                        "https://itb-berlin-news.com/feed/", "https://munichnow.com/feed/",
                        "http://feeds.t-online.de/rss/politik", "http://munichnow.com/feed",
                        "https://newsfeed.zeit.de/index", "https://itb-berlin-news.com/feed",
                        "https://www.deutschland.de/en/feed-news/rss.xml", "https://www.spiegel.de/international/index.rss",
                        "https://www.thelocal.de/feeds/rss.php"
                        ]

    german_reddit_communities = ['wallstreetbets', 'WallStreetbetsELITE', 'deepfuckingvalue', 'stocks', 'investing',
                                 'stockmarket']
    german_twitter_users = ['mcuban', 'elonmusk', 'PeterLBrandt', 'CNBC', 'SJosephBurns', 'elerianm', 'IBDinvestors',
                            'jimcramer', 'bespokeinvest', 'wsbmod', 'galgitron', 'thevrsoldier', 'glewmecorp']

    ####################################################################################################################
    # -> X. Crypto <-
    ####################################################################################################################
    crypto = "Crypto"
    crypto_search_terms = ["decentralized", "crypto", "cryptocurrency", "bitcoin", "blockchain", "smart contract"]
    
    crypto_weighted_terms = {"metaverse": LOW_WEIGHT,
                             "roblox": LOW_WEIGHT,
                             "nft": MIDDLE_WEIGHT,
                             "nfts": MIDDLE_WEIGHT,
                             "nft's": MIDDLE_WEIGHT,
                             "decentraland": LOW_WEIGHT,
                             "meta": LOW_WEIGHT,
                             "sandbox": LOW_WEIGHT,
                             "mana": LOW_WEIGHT,
                             "parcel": LOW_WEIGHT,
                             "tokens": LOW_WEIGHT,
                             "fork": NANO_WEIGHT,
                             "hardfork": LOW_WEIGHT,
                             "softfork": LOW_WEIGHT,
                             "hard fork": LOW_WEIGHT,
                             "soft fork": LOW_WEIGHT,
                             "virtual": LOW_WEIGHT,
                             "vr": LOW_WEIGHT,
                             "nonfungible": LOW_WEIGHT,
                             "staking": LOW_WEIGHT,
                             "decentralized": HIGH_WEIGHT,
                             "crypto": MAX_WEIGHT,
                             "cryptocurrency": MAX_WEIGHT,
                             "blockchain": MAX_WEIGHT,
                             "dapp": HIGH_WEIGHT,
                             "opensea": HIGH_WEIGHT,
                             "ethereum": HIGH_WEIGHT,
                             "bitcoin": MAX_WEIGHT,
                             "xrp": HIGH_WEIGHT,
                             "ripple": MIDDLE_WEIGHT,
                             "xlm": LOW_WEIGHT,
                             "web3": MAX_WEIGHT,
                             "pos": LOW_WEIGHT,
                             "poe": LOW_WEIGHT,
                             "iot": NANO_WEIGHT,
                             "btc": HIGH_WEIGHT,
                             "eth": HIGH_WEIGHT,
                             "Nano Collaborative": HIGH_WEIGHT,
                             "nano": HIGH_WEIGHT, 
                             "Banano": LOW_WEIGHT,
                             "time wonderland": MIDDLE_WEIGHT,
                             "olympus dao": LOW_WEIGHT,
                             "sushiswap": MAX_WEIGHT,
                             "pancakeswap": HIGH_WEIGHT,
                             "Stablecoins": MINI_WEIGHT,
                             "stablecoin": HIGH_WEIGHT,
                             "altcoin market": HIGH_WEIGHT,
                             "alt market": HIGH_WEIGHT,
                             "alt season": HIGH_WEIGHT,
                             "erc7151": MAX_WEIGHT,
                             "erc1155": MAX_WEIGHT,
                             "smart contract": MAX_WEIGHT,
                             "solidity": MAX_WEIGHT, 
                             "truffle": HIGH_WEIGHT,
                             "ganache": HIGH_WEIGHT,
                             "dex": MIDDLE_WEIGHT,
                             "defi": HIGH_WEIGHT,
                             "decentralized exchange": HIGH_WEIGHT,
                             "centralized exchange": LOW_WEIGHT,
                             "ico": HIGH_WEIGHT,
                             "wallet": LOW_WEIGHT,
                             "minable": LOW_WEIGHT,
                             "coin": MINI_WEIGHT,
                             "token": MIDDLE_WEIGHT,
                             "proof of work": MAX_WEIGHT,
                             "proof of stake": MAX_WEIGHT,
                             "ercLOW_WEIGHT": MAX_WEIGHT,
                             "hodl": MIDDLE_WEIGHT,
                             "altcoin": MAX_WEIGHT,
                             "dao": HIGH_WEIGHT,
                             "coinbase": MAX_WEIGHT,
                             "cold wallet": HIGH_WEIGHT,
                             "hot wallet": HIGH_WEIGHT,
                             "gas": LOW_WEIGHT,
                             "initial coin offering": HIGH_WEIGHT,
                             "Satoshi Nakomoto": MAX_WEIGHT,
                             "stable coin": HIGH_WEIGHT,
                             "Vitalik Buterin": MAX_WEIGHT,
                             "Digital Currency": MAX_WEIGHT,
                             "Distributed Ledger Technology": MAX_WEIGHT,
                             "dlt": LOW_WEIGHT,
                             "kyc": LOW_WEIGHT,
                             "know your customer": MIDDLE_WEIGHT,
                             "Nonfungible tokens": MAX_WEIGHT,
                             "Proof of Authority": HIGH_WEIGHT,
                             "Public Ledger": MIDDLE_WEIGHT,
                             "collectible": HIGH_WEIGHT,
                             "collectibles": HIGH_WEIGHT,
                             "NFT Marketplace": MAX_WEIGHT,
                             "nft worlds": MIDDLE_WEIGHT,
                             }

    crypto_rss_feeds = ["https://cointelegraph.com/rss", "https://coindesk.com/feed", "https://news.bitcoin.com/feed",
                        "https://minergate.com/blog/feed/", "https://coinjournal.net/feed",
                        "https://cryptoinsider.com/feed", "http://www.newsbtc.com/feed",
                        "https://twitter.com/jaxx_io/feed", "https://bitcoinmagazine.com/feed",
                        "https://www.crypto-news.net/feed", "https://www.cryptoninjas.net/feed",
                        "https://ethereumworldnews.com/feed", "https://bravenewcoin.com/feed",
                        "http://www.financemagnates.com/feed", "http://www.cryptoquicknews.com/feed",
                        "http://cryptscout.com/feed", "http://www.coinnewsasia.com/feed"]

    ####################################################################################################################
    # -> X. Metaverse <-
    ####################################################################################################################
    metaverse = "Metaverse"
    metaverse_search_terms = [
                                "metaverse", "virtual world", "vr",
                                 "decentraland", "decentralized", "nft",
                                 "decentralized world", "augmented reality",
                                 "blockchain", "ethereum", "virtual reality"
                              ]
    metaverse_search_terms_test = ["metaverse", "virtual world", "nft"]


    """
    -> Update secondary words
    -> Grab from the database and match terms from virtual worlds...
    -> Update the enhancer to re-analyze..
    """

    metaverse_secondary_weighted_terms = {

        "land": MIDDLE_WEIGHT,
        "parcel": MIDDLE_WEIGHT,
        "virtual land": LOW_WEIGHT,
        "real estate": LOW_WEIGHT,
        "DAO": LOW_WEIGHT,
        "decentralized autonomous organization": MIDDLE_WEIGHT,
        "build": 3,
        "building": 3,
        "device": MIDDLE_WEIGHT,
        "glasses": LOW_WEIGHT

    }

    metaverse_weighted_terms = {
        "0xearth": MIDDLE_WEIGHT,
        "3d": LOW_WEIGHT,
        "activision blizzard": LOW_WEIGHT,
        "alterverse": LOW_WEIGHT,
        "amd": MIDDLE_WEIGHT,
        "ar glasses": MAX_WEIGHT,
        "ar goggles": MAX_WEIGHT,
        "ar headset": MAX_WEIGHT,
        "artificial intelligent": MINI_WEIGHT,
        "arvr": MIDDLE_WEIGHT,
        "assets": LOW_WEIGHT,
        "augmented reality": MAX_WEIGHT,
        "avatar": LOW_WEIGHT,
        "average price": NANO_WEIGHT,
        "binance": MINI_WEIGHT,
        "bitcoin": 2,
        "blockchain": MIDDLE_WEIGHT,
        "bought": NANO_WEIGHT,
        "btc": 2,
        "centralized": LOW_WEIGHT,
        "collectible": MIDDLE_WEIGHT,
        "collectibles": MIDDLE_WEIGHT,
        "creator economy": MIDDLE_WEIGHT,
        "crypto based": NANO_WEIGHT,
        "cryptobased": MIDDLE_WEIGHT,
        "cryptocountries": HIGH_WEIGHT,
        "cryptocurrency": LOW_WEIGHT,
        "dapp": MIDDLE_WEIGHT,
        "decentraland": MAX_WEIGHT,
        "decentralisation": MINI_WEIGHT,
        "decentralised": LOW_WEIGHT,
        "decentralised economy": MIDDLE_WEIGHT,
        "decentralized": MINI_WEIGHT,
        "decentralized app": LOW_WEIGHT,
        "decentralized application": LOW_WEIGHT,
        "decentralized economy": MIDDLE_WEIGHT,
        "decentralized world": MAX_WEIGHT,
        "democratisation": MINI_WEIGHT,
        "denations": LOW_WEIGHT,
        "disrupt": NANO_WEIGHT,
        "disruption": NANO_WEIGHT,
        "edge computing": MINI_WEIGHT,
        "eth": LOW_WEIGHT,
        "ether": LOW_WEIGHT,
        "ethereum": LOW_WEIGHT,
        "etherland": MIDDLE_WEIGHT,
        "fintech": LOW_WEIGHT,
        "fungible": LOW_WEIGHT,
        "gaming": LOW_WEIGHT,
        "gained momentum": LOW_WEIGHT,
        "glewme": MAX_WEIGHT,
        "glewme city": MAX_WEIGHT,
        "glewmecity": MAX_WEIGHT,
        "gpu": MIDDLE_WEIGHT,
        "haptic": MINI_WEIGHT,
        "haptic suit": MINI_WEIGHT,
        "haptics": MINI_WEIGHT,
        "hatchables": LOW_WEIGHT,
        "headset": NANO_WEIGHT,
        "horizon": MINI_WEIGHT,
        "horizon world": MIDDLE_WEIGHT,
        "horizon worlds": MIDDLE_WEIGHT,
        "human interface": MINI_WEIGHT,
        "infrastructure": NANO_WEIGHT,
        "innovation": 3,
        "intel": LOW_WEIGHT,
        "investment": NANO_WEIGHT,
        "investment opportunity": MINI_WEIGHT,
        "iot": MINI_WEIGHT,
        "land": LOW_WEIGHT,
        "loopring": LOW_WEIGHT,
        "mana": MIDDLE_WEIGHT,
        "meta": LOW_WEIGHT,
        "meta key": LOW_WEIGHT,
        "meta platform": MIDDLE_WEIGHT,
        "meta platforms": MIDDLE_WEIGHT,
        "metaverse": MAX_WEIGHT,
        "metaverse industry": MAX_WEIGHT,
        "microsoft": LOW_WEIGHT,
        "multiple platforms": MINI_WEIGHT,
        "nft": LOW_WEIGHT,
        "NFT Marketplace": MIDDLE_WEIGHT,
        "nft worlds": MIDDLE_WEIGHT,
        "nft's": MIDDLE_WEIGHT,
        "nfts": MIDDLE_WEIGHT,
        "Niantic": MINI_WEIGHT,
        "nonfungible": MIDDLE_WEIGHT,
        "nvidia": MIDDLE_WEIGHT,
        "oculus": HIGH_WEIGHT,
        "opensea": MIDDLE_WEIGHT,
        "ovr land": LOW_WEIGHT,
        "ownable": MIDDLE_WEIGHT,
        "ownables": MIDDLE_WEIGHT,
        "parcel": MIDDLE_WEIGHT,
        "play earn": MIDDLE_WEIGHT,
        "poe": MINI_WEIGHT,
        "polka city": LOW_WEIGHT,
        "pos": MINI_WEIGHT,
        "property value": LOW_WEIGHT,
        "real estate": LOW_WEIGHT,
        "roblox": HIGH_WEIGHT,
        "Roblox Corporation": LOW_WEIGHT,
        "sandbox": MIDDLE_WEIGHT,
        "sft": LOW_WEIGHT,
        "semi fungible": LOW_WEIGHT,
        "sha-256": MINI_WEIGHT,
        "sha256": MINI_WEIGHT,
        "smart chain": MINI_WEIGHT,
        "snap": MINI_WEIGHT,
        "solana": MAX_WEIGHT,
        "sold": MINI_WEIGHT,
        "somnium": MAX_WEIGHT,
        "somnium space": MAX_WEIGHT,
        "spatial computing": LOW_WEIGHT,
        "speculation": NANO_WEIGHT,
        "stake": NANO_WEIGHT,
        "staking": NANO_WEIGHT,
        "stock": MINI_WEIGHT,
        "store value": MINI_WEIGHT,
        "state channel": MINI_WEIGHT,
        "superworld": HIGH_WEIGHT,
        "TakeTwo": MINI_WEIGHT,
        "the sandbox": MAX_WEIGHT,
        "token": LOW_WEIGHT,
        "tokens": LOW_WEIGHT,
        "treeverse": LOW_WEIGHT,
        "ue5": MIDDLE_WEIGHT,
        "unity": HIGH_WEIGHT,
        "unreal engine": HIGH_WEIGHT,
        "Vans World": MINI_WEIGHT,
        "vegas city": LOW_WEIGHT,
        "victoria": LOW_WEIGHT,
        "victoria vr": MAX_WEIGHT,
        "victoriavr": MAX_WEIGHT,
        "virtual": MIDDLE_WEIGHT,
        "virtual land": HIGH_WEIGHT,
        "virtual meeting": HIGH_WEIGHT,
        "virtual meetings": HIGH_WEIGHT,
        "virtual reality": HIGH_WEIGHT,
        "virtual world": HIGH_WEIGHT,
        "virtual worlds": HIGH_WEIGHT,
        "vr": LOW_WEIGHT,
        "vr glasses": MIDDLE_WEIGHT,
        "vr goggles": MIDDLE_WEIGHT,
        "vr headset": MIDDLE_WEIGHT,
        "vr world": MAX_WEIGHT,
        "war raiders": LOW_WEIGHT,
        "wearable": LOW_WEIGHT,
        "wearables": LOW_WEIGHT,
        "web3": MIDDLE_WEIGHT,
        "web3 gaming": HIGH_WEIGHT,
        "web3 game": HIGH_WEIGHT
                                }

    metaverse_url_sources = [
        "https://nftplazas.com/",
        "https://cointelegraph.com/rss", "https://coindesk.com/feed", "https://news.bitcoin.com/feed",
        "https://minergate.com/blog/feed/", "https://coinjournal.net/feed",
        "https://cryptoinsider.com/feed", "http://www.newsbtc.com/feed",
        "https://twitter.com/jaxx_io/feed", "https://bitcoinmagazine.com/feed",
        "https://www.crypto-news.net/feed", "https://www.cryptoninjas.net/feed",
        "https://ethereumworldnews.com/feed", "https://bravenewcoin.com/feed",
        "http://www.financemagnates.com/feed", "http://www.cryptoquicknews.com/feed",
        "http://cryptscout.com/feed", "http://www.coinnewsasia.com/feed"

    ]
    # -> This master weighted list comes dynamically from meta_names.json
    # metaverse_weighted_terms = DICT.merge_dicts(meta_names, metaverse_weighted_custom_terms)
    metaverse_rss_feeds = [ "https://cointelegraph.com/rss", "https://coindesk.com/feed", "https://news.bitcoin.com/feed",
                            "https://minergate.com/blog/feed/", "https://coinjournal.net/feed",
                            "https://cryptoinsider.com/feed", "http://www.newsbtc.com/feed",
                            "https://twitter.com/jaxx_io/feed", "https://bitcoinmagazine.com/feed",
                            "https://www.crypto-news.net/feed", "https://www.cryptoninjas.net/feed",
                            "https://ethereumworldnews.com/feed", "https://bravenewcoin.com/feed",
                            "http://www.financemagnates.com/feed", "http://www.cryptoquicknews.com/feed",
                            "http://cryptscout.com/feed", "http://www.coinnewsasia.com/feed",
                            "https://decentraland.org/blog/feed.xml"]

    ####################################################################################################################
    # -> 5. Android <-
    ####################################################################################################################
    android = "Android"
    android_search_terms = ["android", "android os", "android studio", "android developer", "kotlin", "jetbrains"]
    
    android_weighted_terms = {"android": MAX_WEIGHT,
                              "java": MIDDLE_WEIGHT,
                              "kotlin": HIGH_WEIGHT,
                              "gradle": LOW_WEIGHT,
                              "coroutine": LOW_WEIGHT,
                              "jetpack": HIGH_WEIGHT,
                              "async": 2,
                              "google": MIDDLE_WEIGHT,
                              "vr": 2, "ar": 2,
                              "androiddevsummit": MAX_WEIGHT,
                              "certification": NANO_WEIGHT,
                              "beta": LOW_WEIGHT,
                              "alpha": LOW_WEIGHT,
                              "canary": 2,
                              "jetbrains": LOW_WEIGHT,
                              "api": 2,
                              "summit": NANO_WEIGHT,
                              "stable": NANO_WEIGHT,
                              "android os": MAX_WEIGHT,
                              "android developer": MAX_WEIGHT,
                              "android studio": MAX_WEIGHT,
                              "virtual reality": MINI_WEIGHT,
                              "augmented reality": MINI_WEIGHT,
                              "android dev": NANO_WEIGHT,
                              "wear os": NANO_WEIGHT,
                              "app bundle": NANO_WEIGHT,
                              "app bundles": NANO_WEIGHT,
                              "google play": MIDDLE_WEIGHT,
                              "jetpack compose": MAX_WEIGHT,
                              "dev kit": NANO_WEIGHT,
                              "development kit": MINI_WEIGHT,
                              "firebase": MIDDLE_WEIGHT
                              }

    android_rss_feeds = ["https://www.reddit.com/r/Android.rss", "https://www.androidauthority.com/feed/",
                         "http://feeds.feedburner.com/blogspot/hsDu", "https://medium.com/feed/tag/android",
                         "https://www.reddit.com/r/androiddev.rss", "https://proandroiddev.com/feed",
                         "https://medium.com/feed/@ian-alexander",
                         "http://feeds.feedburner.com/FirebaseBlog", "https://blog.jetbrains.com/kotlin/feed/",
                         "http://feeds.feedburner.com/GDBcode"]
    ####################################################################################################################
    # -> 5. apple <-
    ####################################################################################################################
    apple = "apple"
    apple_search_terms = ["ios", "apple", "apple products", "iphone", "macbook", "apple developer"]

    apple_weighted_terms = {"apple": MIDDLE_WEIGHT,
                            "ios": HIGH_WEIGHT,
                            "apple inc": MAX_WEIGHT,
                            "iphone": HIGH_WEIGHT,
                            "mac": MIDDLE_WEIGHT,
                            "macintosh": MIDDLE_WEIGHT,
                            "product release": MIDDLE_WEIGHT,
                            "product releases": MIDDLE_WEIGHT,
                            "new product": MIDDLE_WEIGHT,
                            "road map": LOW_WEIGHT,
                            "apple watches": HIGH_WEIGHT,
                            "new products": MIDDLE_WEIGHT,
                            "m1": LOW_WEIGHT,
                            "imac": HIGH_WEIGHT,
                            "apple tv": HIGH_WEIGHT,
                            "airtag": MIDDLE_WEIGHT,
                            "airtags": MIDDLE_WEIGHT,
                            "ipad": HIGH_WEIGHT,
                            "pro": MINI_WEIGHT,
                            "new": NANO_WEIGHT,
                            "product": NANO_WEIGHT,
                            "products": NANO_WEIGHT,
                            "mac pro": HIGH_WEIGHT, 
                            "macbook": HIGH_WEIGHT,
                            "macbook pro": HIGH_WEIGHT,
                            "app store": HIGH_WEIGHT,
                            "project": MINI_WEIGHT,
                            "tim cook": HIGH_WEIGHT, 
                            "m1 pro chip": HIGH_WEIGHT,
                            "new model": LOW_WEIGHT,
                            "new models": LOW_WEIGHT,
                            "air": MINI_WEIGHT,
                            "m2": LOW_WEIGHT,
                            "m2 chip": LOW_WEIGHT,
                            "apple software": HIGH_WEIGHT,
                            "apples software": MIDDLE_WEIGHT,
                            "conference": MINI_WEIGHT,
                            "peek": NANO_WEIGHT,
                            "airpods": HIGH_WEIGHT,
                            "airpod": HIGH_WEIGHT,
                            "max": MINI_WEIGHT,
                            "silicon chip": MINI_WEIGHT,
                            "silicon chips": MINI_WEIGHT,
                            "apple silicon": MIDDLE_WEIGHT,
                            "steve jobs": HIGH_WEIGHT,
                            "homepod": HIGH_WEIGHT,
                            "series": MINI_WEIGHT,
                            "xcode": MAX_WEIGHT,
                            "rumor": MINI_WEIGHT,
                            "rumors": MINI_WEIGHT,
                            "announced": LOW_WEIGHT,
                            "update": MINI_WEIGHT,
                            "updates": MINI_WEIGHT,
                            "exclusive": MINI_WEIGHT
                            }
    apple_rss_feeds = []
    ####################################################################################################################
    # -> 6. programming <-
    ####################################################################################################################
    programming = "programming"
    programming_search_terms = ["programming", "software development", "computer science", "software engineer",
                                "coding", "computer science", "cyber security"]

    programming_weighted_terms = {"kotlin": MAX_WEIGHT,
                                  "computer science": MAX_WEIGHT,
                                  "java": MAX_WEIGHT,
                                  "javascript": MAX_WEIGHT,
                                  "swift": MAX_WEIGHT,
                                  "python": MAX_WEIGHT,
                                  "jvm": MIDDLE_WEIGHT,
                                  "php": MIDDLE_WEIGHT,
                                  "bash": MIDDLE_WEIGHT,
                                  "scala": MINI_WEIGHT,
                                  "sql": HIGH_WEIGHT,
                                  "nosql": HIGH_WEIGHT,
                                  "mongodb": MAX_WEIGHT,
                                  "mongo": LOW_WEIGHT,
                                  "perl": MIDDLE_WEIGHT,
                                  "c": MIDDLE_WEIGHT,
                                  "c++": MIDDLE_WEIGHT,
                                  "c#": MIDDLE_WEIGHT,
                                  "ruby": MINI_WEIGHT,
                                  "go": LOW_WEIGHT,
                                  "web based applications": LOW_WEIGHT,
                                  "devops": LOW_WEIGHT,
                                  "programming langauge": MINI_WEIGHT,
                                  "programming languages": MIDDLE_WEIGHT,
                                  "apps": MINI_WEIGHT,
                                  "application": MINI_WEIGHT,
                                  "applications": MINI_WEIGHT,
                                  "object oriented": MINI_WEIGHT,
                                  "low level": MINI_WEIGHT,
                                  "gui development": MINI_WEIGHT,
                                  "backend": MINI_WEIGHT,
                                  "lifecycle": MINI_WEIGHT,
                                  "development": MIDDLE_WEIGHT,
                                  "developers": MIDDLE_WEIGHT,
                                  "html": MIDDLE_WEIGHT,
                                  "css": MIDDLE_WEIGHT,
                                  "xml": MIDDLE_WEIGHT,
                                  "script": LOW_WEIGHT,
                                  "scripting language": HIGH_WEIGHT,
                                  "scripting languages": HIGH_WEIGHT, 
                                  "unix": HIGH_WEIGHT,
                                  "shell": LOW_WEIGHT,
                                  "package": MINI_WEIGHT,
                                  "library": MINI_WEIGHT,
                                  "module": MINI_WEIGHT,
                                  "dependency": MINI_WEIGHT,
                                  "high level": MINI_WEIGHT,
                                  "objc": MINI_WEIGHT,
                                  "objective c": HIGH_WEIGHT,
                                  "jetpack": MIDDLE_WEIGHT,
                                  "async": MIDDLE_WEIGHT,
                                  "androiddevsummit": MIDDLE_WEIGHT,
                                  "certification": NANO_WEIGHT,
                                  "beta": MIDDLE_WEIGHT,
                                  "alpha": LOW_WEIGHT,
                                  "canary": LOW_WEIGHT,
                                  "jetbrains": MIDDLE_WEIGHT,
                                  "api": LOW_WEIGHT,
                                  "summit": MINI_WEIGHT,
                                  "stable": MINI_WEIGHT,
                                  "android os": NANO_WEIGHT,
                                  "android developer": MIDDLE_WEIGHT,
                                  "android studio": MIDDLE_WEIGHT,
                                  "android dev": LOW_WEIGHT,
                                  "wear os": MINI_WEIGHT,
                                  "app bundle": MIDDLE_WEIGHT,
                                  "app bundles": NANO_WEIGHT,
                                  "google play": LOW_WEIGHT,
                                  "jetpack compose": MIDDLE_WEIGHT,
                                  "dev kit": MIDDLE_WEIGHT,
                                  "development kit": MIDDLE_WEIGHT,
                                  "firebase": MIDDLE_WEIGHT,
                                  "debugger": MIDDLE_WEIGHT,
                                  "code": MINI_WEIGHT,
                                  "senior": MINI_WEIGHT,
                                  "coding": MINI_WEIGHT,
                                  "programming": HIGH_WEIGHT,
                                  "programmer": HIGH_WEIGHT,
                                  "virtual machine": LOW_WEIGHT, 
                                  "software": MIDDLE_WEIGHT,
                                  "software engineer": MAX_WEIGHT,
                                  "engineer": LOW_WEIGHT,
                                  "app": MINI_WEIGHT,
                                  "gradle": LOW_WEIGHT,
                                  "coroutine": LOW_WEIGHT,
                                  "xcode": MIDDLE_WEIGHT,
                                  "algo": MINI_WEIGHT
                                  }

    programming_rss_feeds = [
        "http://www.thecrazyprogrammer.com/feed", "https://www.sitepoint.com/feed/",
         "https://www.raywenderlich.com/feed", "https://stackabuse.com/rss/",
         "https://blog.jooq.org/feed/", "http://feeds.hanselman.com/ScottHanselman",
         "https://tympanus.net/codrops/feed/", "https://medium.com/feed/better-programming",
         "https://medium.com/feed/a-technologists-pov", "https://blog.codepen.io/feed/",
         "https://hackr.io/programming/rss.xml", "https://www.techiedelight.com/feed/",
         "https://davidwalsh.name/feed", "https://codesignal.com/feed/",
         "https://alistapart.com/site/rss", "https://www.codingdojo.com/blog/feed",
         "https://fueled.com/feed/", "https://www.codewall.co.uk/feed/"
    ]

    @staticmethod
    def get_main_fopic_category_names():
        test = MainCategories.__dict__.keys()
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