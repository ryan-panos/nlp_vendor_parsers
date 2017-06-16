
from json_nlp_parser import JSONNlPParser

class AlchemyParser(JSONNlPParser):
    def __init__(self):
        # print "#> Initing CortParser . .."
        self.root_str = None
        self.root_dict = None
        self._entities = None
        self._sentiments = None

        # self.converted_sentance_w_proform = None
        # self.converted_sentance_only_ent = None
        # self.scorez = None
        super(AlchemyParser, self).__init__(self)

    # def _load_entities(self):
    #
    #     if self._entities is not None:
    #         print "## Entities already loaded "
    #         return self._entities
    #     elif self.root_dict is None:
    #         print "%% ROOT NOT LOADED in BasisParser s7689h"
    #         return
    #     elif "entities" not in self.root_dict:
    #         print "%% ROOT not None but no entities found"
    #         return
    #
    #     self._entities = self.root_dict["entities"]
    #     return self._entities
    #
    # def _load_sentiments(self):
    #
    #     if self._sentiments is not None:
    #         print "## Entities already loaded "
    #         return self._sentiments
    #     elif self.root_dict is None:
    #         print "%% ROOT NOT LOADED in BasisParser s7689h"
    #         return
    #     elif "document" not in self.root_dict:
    #         print "%% ROOT not None but no document node found"
    #         return
    #     elif "label" not in self.root_dict["document"] and "confidence" not in self.root_dict["document"]:
    #         print "%% ROOT not None AND document node not None but no confidence/label node found"
    #         return
    #
    #     self._sentiments = {
    #         "senitment_label": self.root_dict["document"]["label"],
    #         "senitment_confidence": self.root_dict["document"]["confidence"]
    #     }
    #
    #     return self._sentiments
    #
    # def load_data(self, json_str):
    #
    #     if json_str is not None and len(json_str) > 0:
    #         self.root_str = super(BasisParser, self).save_data(json_str)
    #
    #     if self.root_str is not None and len(json_str) > 0:
    #         self.root_dict = super(BasisParser, self).load_data(self.root_str)
    #         # print " > 1 > self.root: " + str(self.root_dict)
    #         self._load_entities()
    #         self._load_sentiments()
    #     else:
    #         print " %% Don't have json_str or saved json_str"
    #
    # def save_data(self, json_str, needs_wrapper=False):
    #     self.root_str = super(BasisParser, self).save_data(json_str, needs_wrapper)
    #     print " >1----> self.root_str: " + str(self.root_str)
    #
    # def give_sentiment(self):
    #     if self._sentiments and self._sentiments["senitment_label"]:
    #         return self._sentiments["senitment_label"]
    #     else:
    #         print " MISSING senitment_label ?"
    #         return None
    #
    # def get_entity_node(self, normalized_str):
    #     if self._entities is None:
    #         if self._load_entities() is None:
    #             return None
    #     print " ES OK! "
    #     ## Todo - make a version of _finditem that only searches objects in lists - nothing deeper
    #     return super(BasisParser, self)._find_in_list(self._entities, "normalized", normalized_str)