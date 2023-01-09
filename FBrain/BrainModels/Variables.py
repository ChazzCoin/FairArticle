from FNLP.Models.Variables import BaseVariables


class BrainVariables(BaseVariables):
    # Internal Only
    webpage_models = []
    original_webpage_models = []
    original_brain_counts = []
    original_analyzed_counts = []
    original_brain_stop_counts = []
    original_analyzed_stop_counts = []
    # The Brain
    brain_counts = []
    new_analyzed_counts = []
    brain_stop_counts = []
    new_analyzed_stop_counts = []