from ArticleResources.Sources import Sources
import os
import re
import pandas
import feedparser
import random

from FList import LIST

TRENDING_URL = 'http://www.google.com/trends/hottrends/atom/feed?pn=p1'

def google_trends():
    """Returns a list of hit terms via google trends
    """
    try:
        listing = feedparser.parse(TRENDING_URL)['entries']
        trends = [item['title'] for item in listing]
        return trends
    except Exception as e:
        print('ERR hot terms failed!', str(e))
        return None

# if __name__ == '__main__':
#     print(google_trends())

GOOGLESOURCES = os.path.join(os.path.dirname(__file__), 'google_sources.txt')
POPULARSOURCES = os.path.join(os.path.dirname(__file__), 'popular_sources.txt')
RSSSOURCES = os.path.join(os.path.dirname(__file__), 'rss_sources.txt')
STOCKTICKERS = os.path.join(os.path.dirname(__file__), 'stocks.csv')
METAVERSESOURCES = os.path.join(os.path.dirname(__file__), 'metaverse_sources.txt')

class Resource:
    GOOGLE_SOURCES = GOOGLESOURCES
    POPULAR_SOURCES = POPULARSOURCES
    RSS_SOURCES = RSSSOURCES
    METAVERSE_SOURCES = METAVERSESOURCES

def get_resource(resource):
    """Uses generator to return next useragent in saved file
    """
    with open(resource, 'r') as f:
        urls = ['http://' + u.strip() for u in f.readlines()]
        return LIST.scramble(urls)

def get_random(items):
    selection = random.randint(0, len(items) - 1)
    return items[selection]

def get_google_sources():
    return get_resource(Resource.GOOGLE_SOURCES)

def get_popular_sources():
    return get_resource(Resource.POPULAR_SOURCES)

def get_rss_sources():
    return get_resource(Resource.RSS_SOURCES)

def get_metaverse_sources():
    return get_resource(Resource.METAVERSE_SOURCES)

def get_random_metaverse_source():
    m_urls = get_metaverse_sources()
    m_count = len(m_urls)
    ran_dom = random.randint(0, m_count)
    url = m_urls[ran_dom]
    return url

# Load Stock Ticker List from CSV File
def read_stock_csv():
    df = pandas.read_csv(STOCKTICKERS)
    return df

def read_stock_csv_to_dict():
    df = pandas.read_csv(STOCKTICKERS)
    df_dict = df.to_dict()
    return df_dict

def build_list_of_companies(dic):
    companies_list = []
    # keys = Symbol, Name...
    tickers = dic['Symbol']
    names = dic['Name']
    ipo_years = dic['IPO Year']
    sectors = dic['Sector']
    industries = dic['Industry']
    countries = dic['Country']
    market_caps = dic['Market Cap']

    # 'IPO Year' 'Sector' 'Industry' 'Country' 'Market Cap'
    index_count = 0
    while index_count <= len(tickers):
        ticker = LIST.get(index_count, tickers)
        name = LIST.get(index_count, names)
        ipo_year = LIST.get(index_count, ipo_years)
        sector = LIST.get(index_count, sectors)
        industry = LIST.get(index_count, industries)
        country = LIST.get(index_count, countries)
        market_cap = LIST.get(index_count, market_caps)

        single_company = {
            "ticker": ticker,
            "name": name,
            "ipo_year": ipo_year,
            "sector": sector,
            "industry": industry,
            "country": country,
            "market_cap": market_cap,
        }
        companies_list.append(single_company)
        index_count += 1
    return companies_list


# Parse Stock Ticker List from CSV File
def get_stock_tickers():
    df = read_stock_csv()
    list_of_tickers = []
    for ticker in df['Symbol']:
        list_of_tickers.append(ticker)
    return list_of_tickers

def get_company_names_from_csv():
    df = read_stock_csv()
    list_of_companies = []
    for name in df['Name']:
        name = to_tokens(name)
        one = name[0] if len(name) > 0 else ""
        two = name[1] if len(name) > 1 else ""
        new_name = one + " " + two
        list_of_companies.append((one, new_name))
    return list(set(list_of_companies))

# if __name__ == '__main__':
#     test = read_stock_csv_to_dict()
#     list_of_companies = build_list_of_companies(test)
#     from Jarticle.jCompany import jCompany
#     jc = jCompany.constructor_jcompany()
#     jc.add_companies(list_of_companies)
#     print(test)

def to_tokens(text):
    """ ALTERNATIVE: Split a string into array of words. """
    try:
        text = re.sub(r'[^\w ]', '', text)  # strip special chars
        return [x.strip('.').lower() for x in text.split()]
    except TypeError:
        return None