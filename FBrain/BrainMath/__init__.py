from F import LIST, DICT, DATE
from F.LOG import Log


#
def add_word_frequency_counts(brain_scores:list, new_scores:dict) -> list:
    """ Add two dicts of word counts together """
    result = []

    """ Part 1. Preparing... """

    # All New Scored Words
    new_score_words = []
    for word in new_scores.keys():
        new_score_words.append(word)

    # All Brain Words
    brain_score_words = []
    for item in brain_scores:
        brain_word = DICT.get("word", item, None)
        brain_score_words.append(brain_word)

    new_words = []
    for new_scored_word in new_score_words:
        if new_scored_word in brain_score_words:
            continue
        new_words.append(new_scored_word)

    """ Part 2. Merging with Brain... """
    for brain_item in Log.ProgressBarYielder(brain_scores, "Calculating brain counts..."):
        brain_word = DICT.get("word", brain_item, None)
        brain_count = DICT.get("count", brain_item, None)
        if new_scores.__contains__(brain_word):
            new_score = int(brain_count) + int(new_scores[brain_word])
            brain_item["count"] = new_score
            brain_item["updatedDate"] = DATE.TODAY
            result.append(brain_item)
            continue
        result.append(brain_item)

    """ Part 3. If new words, add them to brain... """
    if new_words:
        for new_word in Log.ProgressBarYielder(new_words, "Adding new words to brain..."):
            new_item = {"word": new_word, "count": new_scores[new_word], "updatedDate": DATE.TODAY}
            result.append(new_item)

    return result