from F import LIST
from F.CLASS import FairClass

from FBrain import BrainMath


class BaseBrain(FairClass):

    def merge_model(self, model):
        cm = model
        for var in cm.get_list_of_variables():
            cm_value = cm.get_attribute(var)
            if var in self.get_list_of_variables():
                self_value = self.get_attribute(var)
                result = None
                # create ignore list, like pid.
                if not cm_value or var in ['pid']:
                    continue
                if type(cm_value) in [int]:
                    result = int(cm_value) + int(self_value)
                elif type(cm_value) in [list]:
                    result = LIST.flatten(cm_value, self_value)
                elif type(cm_value) in [dict]:
                    result = BrainMath.add_word_counts(self_value, cm_value)
                self.set_variable(var, result)
            else:
                self.set_variable(var, cm_value)