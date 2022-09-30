from FCM.Jarticle.jVirtualWorld import jVirtualWorld
from FCM.Jarticle.jProvider import jPro
from FNLP.Language import Words, Tokenizer


jpro = jPro()
jworld = jVirtualWorld()
WORLD_NAMES = jworld.get_all_world_names()
WORLD_TICKERS = jworld.get_all_world_tickers()


def find_vr_names(content:str):
    content_tokens = Tokenizer.complete_tokenization_v2(content)
    result = Words.matcher(WORLD_NAMES, content_tokens)
    return result
