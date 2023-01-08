from FBrain.JHelpers import ART
from FA.JEngines import VRNameEngine


def find_vr_world_names(article):
    content = ART.get_content(article)
    vr_worlds = VRNameEngine.find_vr_names(content)
    article["vr_worlds"] = vr_worlds
    return article


""" 
    -> [MASTER]
"""
def enhance_article(article):
    article = find_vr_world_names(article)
    return article