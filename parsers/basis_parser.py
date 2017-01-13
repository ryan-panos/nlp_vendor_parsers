
from json_nlp_parser import JSONNlPParser

DATA_DIR = '/Users/ryanpanos/Documents/code/nlp_vendor_parsers/data/'

class BasisParser(JSONNlPParser):

    def __init__(self):
        # print "#> Initing CortParser . .."
        self.root_str = None
        self.root_dict = None
        self._entities = None
        self._sentiments = None

        # self.converted_sentance_w_proform = None
        # self.converted_sentance_only_ent = None
        # self.scorez = None
        super(BasisParser, self).__init__(self)

    def _load_entities(self):
        
        if self._entities is not None:
            print "## Entities already loaded "
            return self._entities
        elif self.root_dict is None:
            print "%% ROOT NOT LOADED in BasisParser s7689h"
            return
        elif "entities" not in self.root_dict:
            print "%% ROOT not None but no entities found"
            return

        self._entities = self.root_dict["entities"]
        return self._entities


    def _load_sentiments(self):

        if self._sentiments is not None:
            print "## Entities already loaded "
            return self._sentiments
        elif self.root_dict is None:
            print "%% ROOT NOT LOADED in BasisParser s7689h"
            return
        elif "document" not in self.root_dict:
            print "%% ROOT not None but no document node found"
            return
        elif "label" not in self.root_dict["document"] and "confidence" not in self.root_dict["document"]:
            print "%% ROOT not None AND document node not None but no confidence/label node found"
            return

        self._sentiments = {
            "senitment_label": self.root_dict["document"]["label"],
            "senitment_confidence": self.root_dict["document"]["confidence"]
        }

        return self._sentiments
        
        
        
        
    def load_data(self, json_str):

        if json_str is not None and len(json_str) > 0:
            self.root_str = super(BasisParser, self).save_data(json_str)

        if self.root_str is not None and len(json_str) > 0:
            self.root_dict = super(BasisParser, self).load_data(self.root_str)
            # print " > 1 > self.root: " + str(self.root_dict)
            self._load_entities()
            self._load_sentiments()
        else:
            print " %% Don't have json_str or saved json_str"


    def save_data(self, json_str, needs_wrapper=False):
        self.root_str = super(BasisParser, self).save_data(json_str, needs_wrapper)
        print " >1----> self.root_str: " + str(self.root_str)
       
    
    def give_sentiment(self):
        if self._sentiments and self._sentiments["senitment_label"]:
            return self._sentiments["senitment_label"]
        else:
            print " MISSING senitment_label ?"
            return None


    def get_entity_node(self, normalized_str):
        if self._entities is None:
            if self._load_entities() is None:
                return None
        print " ES OK! "
        ## Todo - make a version of _finditem that only searches objects in lists - nothing deeper
        return super(BasisParser, self)._find_in_list(self._entities, "normalized", normalized_str)



## KEY ASSUMPTION: all the other servies will be given in an easy to digest format like the below
#   THEREFORE the parser will "try" to find the various services and populate a
#

entity_example_output = {
  "entities": [
    {
      "type": "PERSON",
      "mention": "Bill Murray",
      "normalized": "Bill Murray",
      "count": 1,
      "entityId": "Q29250"
    },
    {
      "type": "PRODUCT",
      "mention": "Ghostbusters",
      "normalized": "Ghostbusters",
      "count": 1,
      "entityId": "Q108745"
    },
    {
      "type": "TITLE",
      "mention": "Dr.",
      "normalized": "Dr.",
      "count": 1,
      "entityId": "T2"
    },
    {
      "type": "PERSON",
      "mention": "Peter Venkman",
      "normalized": "Peter Venkman",
      "count": 1,
      "entityId": "Q2483011"
    },
    {
      "type": "LOCATION",
      "mention": "Boston",
      "normalized": "Boston",
      "count": 1,
      "entityId": "Q100"
    },
    {
      "type": "IDENTIFIER:URL",
      "mention": "http://dlvr.it/BnsFfS",
      "normalized": "http://dlvr.it/BnsFfS",
      "count": 1,
      "entityId": "T5"
    }
  ],
  "responseHeaders": {
    "date": "Fri, 21 Oct 2016 17:46:30 GMT, Fri, 21 Oct 2016 17:46:31 GMT",
    "content-type": "application/json",
    "x-rosetteapi-request-id": "1015dde9-9e79-421e-bc4d-028a8b45a2c0",
    "x-rosetteapi-processedlanguage": "eng",
    "connection": "close",
    "server": "Jetty(9.2.17.v20160517)"
  }
}


def test_basis():
    source = DATA_DIR + 'winograd.csv'


# f = open(DATA_DIR + 'NER/5_basis-ner.json', 'r')
# basis_p1=BasisParser()
# basis_p1.load_data(f.read())
#
# # TODO: does normalized mean . .  lower case when appropriate?
#
# ner_node1 = basis_p1.get_entity_node("LAS CRUCES")
# print " GOT ner_node1: " + str(ner_node1)
#
# ner_node2 = basis_p1.get_entity_node("CRAP")
# print " This should be None: " + str(ner_node2)


def get_basis_sentiement(id):
    source = DATA_DIR + "basis_sentiment_output/" + str(id) + "_basis-sentiment.json"
    f = open(source, 'r')
    basis_p1 = BasisParser()
    basis_p1.load_data(f.read())
    return basis_p1.give_sentiment()


def test_basis_sentiment(print_solution=False):

    source = DATA_DIR + 'semeval-concatenated.csv'
    out_put = DATA_DIR + 'semeval-concatenated_wSent.csv'
    # source = '/Users/ryanpanos/Documents/code/nlp-parsers/data/winograd.csv'
            # /Users/ryanpanos/Documents/code/nlp-parsers/data

    out_f = open(out_put, 'w')
    # for line in
    with open(source, "r") as ins:
        # array = []
        total_success = 0
        tried_cnt = 0
        for idx, line in enumerate(ins):
            line_ls = line.split('","')
            if str(line_ls[0]) != '"ID':
                line_ls[0] = line_ls[0][1:]
                sent = get_basis_sentiement(line_ls[0])
                if sent is None:
                    print " ### NONE? "
                line_ls = [str('"' + sent)] + line_ls
            else:
                line_ls = [str('"ID')] + line_ls   ## FIX THIS!!
            out_f.write('","'.join(line_ls))

test_basis_sentiment()