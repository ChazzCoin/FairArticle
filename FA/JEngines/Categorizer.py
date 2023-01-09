from FNLP.Language import Tokenizer, Words
from F import DICT, LIST

""" DO NOT USE THIS
    -> USE TOPIC.MAIN_CATEGORIZER
"""
UNKNOWN = "Unknown"
UNSURE = "Unsure"
UNCATEGORIZED = [UNSURE, UNKNOWN]


def score_sentences(sentences, weighted_words):
    scored_sentences = []
    highest_s = 0
    for sentence in sentences:
        temp_score = score_content(content=sentence, weighted_words=weighted_words)
        score = LIST.get(0, temp_score)
        scored_sentences.append([score, sentence])
        if score > highest_s:
            highest_s = score

    only_scored = []
    for scored_s in scored_sentences:
        score = LIST.get(0, scored_s)
        if score == 0:
            continue
        if len(scored_sentences) <= 6 and score < highest_s - 10:
            continue
        only_scored.append(scored_s)
    return only_scored


def score_content(content, weighted_words):
    word_list = Tokenizer.complete_tokenization_v2(content)
    temp = private_run_matcher(word_list, weighted_words)
    return temp

def categorizer_layer2(content, categories: {}):
    # -> 1. Convert String into Token List
    word_list = private_content_to_wordList(content)
    # -> 2.
    cater = categorize(word_list, categories)
    highest_main_cat_name = LIST.get(0, cater)
    highest_main_score = LIST.get(1, cater)
    highest_main_matches = LIST.get(2, cater)
    if highest_main_cat_name == UNSURE or highest_main_cat_name == UNKNOWN:
        return cater
    # -> 3.
    secondary_weighted_terms = DICT.get("secondary_weighted_terms", categories[highest_main_cat_name], default=False)
    caterLayer2 = private_run_matcher(word_list, secondary_weighted_terms)
    second_score = LIST.get(0, caterLayer2, 0)
    final_score = highest_main_score + second_score
    return highest_main_cat_name, final_score, highest_main_matches

def categorizer_layer2_db_models(content):
    from FBrain.BrainModels import Models
    models = Models.get_all_models_to_dict()
    # -> 1. Convert String into Token List
    word_list = private_content_to_wordList(content)
    # -> 2.
    cater = categorize(word_list, models)
    highest_main_cat_name = LIST.get(0, cater)
    highest_main_score = LIST.get(1, cater)
    highest_main_matches = LIST.get(2, cater)
    if highest_main_cat_name == UNSURE or highest_main_cat_name == UNKNOWN:
        return cater
    # -> 3.
    secondary_weighted_terms = DICT.get("secondary_weighted_terms", models[highest_main_cat_name], default=False)
    caterLayer2 = private_run_matcher(word_list, secondary_weighted_terms)
    second_score = LIST.get(0, caterLayer2, 0)
    final_score = highest_main_score + second_score
    return highest_main_cat_name, final_score, highest_main_matches


def private_content_to_wordList(content):
    # FAIR -> Completely Tokenize Words/Phrases
    word_list = Tokenizer.complete_tokenization_v2(content)
    return word_list

""" PUBLIC -> Master Function <- """
def categorize(word_list, categories: {}):
    """
    -> Matcher_v3 under the hood, but now categorizes each topic based on topic score.
        - Loops through each topic, scoring the article against each topic.
        - It will return a dict of every score/result per topic.

        :param content -> Raw String of Words.
                            - They will be tokenized.
        :param categories -> All Topics and their Attributes. (search_terms, weighted_terms...)
                            - Categorizer will extract what it needs.

        ::return -> tuple("str: top cat", "int: top cat score", "dict: all scored, no empties")
    """
    # FAIR -> Completely Tokenize Words/Phrases
    # word_list = Language.complete_tokenization_v2(content)
    # -> Setup
    return_dict = {}  # { "category_name": ( score, { "weighted_term": "match_count", "weighted_term": "match_count" } ) }
    # 1. -> Loop Each Category
    for category_name in categories.keys():
        # -> Extract Weighted Terms from Category/SubCategory
        weighted_terms = DICT.get("weighted_terms", categories[category_name], default=False)
        secondary_weighted_terms = DICT.get("secondary_weighted_terms", categories[category_name], default=False)
        if not weighted_terms:
            weighted_terms = categories[category_name]
        # -> Run Matcher <- #
        return_dict[category_name] = private_run_matcher(word_list, weighted_terms)
    no_empty_scores = private_remove_empty_scores(categories, return_dict)
    return no_empty_scores

""" PRIVATE """
def private_run_matcher(word_list, weighted_terms):
    """ PRIVATE """
    # 2. -> Loop Each Category Weighted Term
    temp_dict = {}  # { "weighted_term": "match_count" }
    score = 0  # "weighted_term" Score * "match_count"
    for w_term in weighted_terms:
        # Stay Safe People
        if not w_term and w_term == "" or w_term == " ":
            continue
        # -> Expand Weighted Term
        expanded_key_list = Words.expand_word(w_term)
        # 3. -> Loop All Tokens AND MATCH!!
        for token in word_list:
            # Stay Safe People
            if not token or token == "" or token == " ":
                continue
            # MATCHER! -> if content word is in expanded weighted term list...
            if is_match(token, expanded_key_list):
                # -> We have a match!
                key_score = weighted_terms[w_term]
                score += key_score
                temp_dict = DICT.add_matched_word_to_result(w_term, temp_dict)
    # -> 4. Finish Up
    return score, temp_dict  # ( score, { "weighted_term": "match_count", "weighted_term": "match_count" } )

def is_match(word:str, word_list:list):
    word = str(word).lower() # Make LowerCase
    word_list = [str(item).lower() for item in word_list] # Make All Lowercase
    if word in word_list:
        return True
    return False

""" PRIVATE -> Helper Function. """
def private_remove_empty_scores(cats, all_scores):
    """ PRIVATE
        -> Removes all empty scores from the categorizer to remove bloat data.
    """
    highest_score = 0
    cat_scores = {}
    highest_topic_name = ""
    for topic_name in cats:
        result = all_scores[topic_name]
        score = LIST.get(0, result)
        if score and score > 1:
            if score > highest_score:
                highest_score = score
                highest_topic_name = topic_name
            cat_scores[topic_name] = result
    if highest_score < 200:
        highest_topic_name = UNKNOWN
    elif highest_score < 500:
        highest_topic_name = UNSURE
    return highest_topic_name, highest_score, cat_scores