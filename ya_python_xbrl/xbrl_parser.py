
import sys, math
from .xbrl_ast import XbrlAst

def err_msg(message):
    print("Error: @" + __name__ + ' ' + message, file=sys.stderr)

class XbrlToken:

    def __init__(self):
        
        self.__left_bracket = '<'
        self.__right_bracket = '>'
        self.__backslash = '/'
        self.__space = ' '
        self.__equal = '='
        self.__colon = ':'
        self.__nullstr = ''
        self.__dquote = '\"'
        self.__tags_to_be_ignored = {'span'}

    def tags_to_be_ignored(self) -> set:
        return self.__tags_to_be_ignored

    def backslash(self) -> str:
        return self.__backslash

    def left_bracket(self) -> str:
        return self.__left_bracket

    def right_bracket(self) -> str:
        return self.__right_bracket

    def space(self) -> str:
        return  self.__space

    def equal(self) -> str:
        return self.__equal

    def colon(self) -> str:
        return self.__colon

    def nullstr(self) -> str:
        return self.__nullstr

    def dquote(self) -> str:
        return self.__dquote

    def is_digit(self, char) -> bool:
        return True if 48 <= ord(char) and ord(char) <= 57 else False

class XbrlLexer:

    def __init__(self):

        self.pos : int = 0
        self.tree: XbrlAst = XbrlAst()
        self.t: XbrlToken = XbrlToken()


    def __start_tag(self, text: str) -> dict:
        start_pos: int = self.pos + 1

        while text[self.pos] != self.t.right_bracket():
            self.pos += 1
      
        inner_tags = text[start_pos:self.pos].split(self.t.space())

        tags : dict = {}

        for tag in inner_tags:
            i : int = 0

            while i < len(tag): 
                if tag[i] == self.t.space(): 
                    pass
                elif tag[i] == self.t.colon():     
                    key = tag[:i]
                    value = tag[i+1:len(tag)] 
                    tags[key] = value.replace(self.t.dquote(), self.t.nullstr())
                    break
                elif tag[i] == self.t.equal():
                    key = tag[:i]
                    value = tag[i+2:len(tag)-1] 
                    tags[key] = value.replace(self.t.dquote(), self.t.nullstr())
                    break
            
                i += 1

        return {'XBRL_start': tags}

    def __end_tag(self, text: str) -> dict:

        start_pos : int = self.pos
        while text[self.pos] != self.t.right_bracket():
            self.pos += 1
        objs = text[start_pos:self.pos] \
            .replace(self.t.dquote(), self.t.nullstr()) \
            .split(self.t.colon())

        key = objs[0]

        # to avoid non xbrl tag: <span>
        if key in self.t.tags_to_be_ignored():
            value = ''
        else:
            value = objs[1]

        return {'XBRL_end': {key : value}}

    def __value(self, text: str):

        start_pos: int = self.pos + 1 
        while  self.pos < len(text)-1:
            if text[self.pos] == self.t.left_bracket():
                break
            if text[self.pos] == self.t.right_bracket():
                self.pos += 1
                continue
            #if not self.t.is_digit(text[self.pos]):
            #    self.err_msg("not a digit")
            self.pos += 1 

        return text[start_pos:self.pos]

    def lex (self, text: str) -> list:
        """
        construct and return abstract syntax tree by top-down
        """

        ast : list = []
        start_tag: dict = {}
        val: str = ""
        end_tag: dict = {}
        
        while self.pos < len(text):

            # is start tag
            if text[self.pos] == self.t.left_bracket() \
                and text[self.pos+1] != self.t.backslash():
              
                start_tag = self.__start_tag(text)

            # is value
            if text[self.pos] == self.t.right_bracket():
                val = self.__value(text)

            # is close tag
            if text[self.pos] == self.t.left_bracket() \
                and text[self.pos+1] == self.t.backslash():
                self.pos += 2
                end_tag = self.__end_tag(text)
   
                ast.append(start_tag)
                ast.append(val)
                ast.append(end_tag)

                self.tree.left = start_tag
                if val != self.t.nullstr():
                    self.tree.value = val
                self.tree.right = end_tag 
        
            self.pos += 1

        return ast

class XbrlParser:
    """ EBNF: This is unofficial grammer. Back deduced from several exmaples.
    left_bracket := '<'
    right_bracket := '>'
    back_slash := '/'
    space := '\ '
    equal := '='
    colon := ':'
    digit := [0-9]
    char := [a-zA-Z]
    sign := ('-'||'+')
    string := (char || digit)+
    value := digit{1,}digit+
    tag_element = string (equal || colon) (string || value)
    start_tag := <tag_element>
    end_tag := <string colon string>
    tag := (start_tag value end_tag)
    tags := tag+
    """

    def __init__(self):
        self._root = None

    def decimals(self, tag) -> int:
        #if not tag.isdigit():
        #    err_msg('decimal conversion failed. decimal tag could not be detected.')
        #    sys.exit(-1)
        return -int(tag)

    def is_start_tag(self, i: int, tags) -> bool:
        return 'XBRL_start' in tags[i]

    def is_end_tag(self, i: int, tags) -> bool:
        return 'XBRL_end' in tags[i]

    def is_net_sales(self, i: int, tags) -> bool:
        if 'NetSales' in tags:
            return True

    def is_cost_of_sales(self, i: int, tags) -> bool:
        if 'CostOfSales' in tags[i]:
            return True

    def is_COGS(self, i: int, tags):
        pass

    def is_G_and_A(self, i: int, tags):
        pass

    def is_operating_profit(self, i: int, tags):
        pass

    def is_jppfs_cor(self, i: int, tags) -> bool:

        ptag = tags[i-1]['XBRL_start']
        #"<jppfs_cor:NetSales contextRef=\"Prior1YearDuration\" unitRef=\"JPY\" decimals=\"-6\">51683000000</jppfs_cor:NetSales>"

        if 'jppfs_cor' in ptag:   
 
            if self.is_net_sales(i, ptag['jppfs_cor']):
                res = int(tags[i]) * math.pow(10, self.decimals(ptag['decimals']))
                print(value)
                
            if self.is_cost_of_sales(i, ptag['jppfs_cor']):
                print(tags[i])

    def parse(self, text: str):
        lexer : XbrlLexer = XbrlLexer()
        tags: list = lexer.lex(text)

        for i in range(len(tags)-2):

            if isinstance(tags[i], str):
                continue

            #print('TAGS', tags[i])

            # start tag detection
            if self.is_start_tag(i, tags):
             
                # store value  
                self.is_jppfs_cor(i+1, tags)

                # check if end tag matches
                if self.is_end_tag(i+2, tags):
                    continue    
                else:
                    tag_end_err : str = 'end tag unmatch: ' + str(tags[i+2])
                    err_msg(tag_end_err)
                    sys.exit(-1)

class XbrlApp:

    def __init__(self):
        self.__parser : XbrlParser = XbrlParser()

        prefix_edinet = set(\
                            ["jpcrp-esr_cor",\
                            "jppfs_cor",\
                            "jpcrp_cor",\
                            "jpcrp-sbr_cor",\
                            "jpctl_cor",\
                            "jpdei_cor",\
                            "jplvh_cor",\
                            "jpsps-esr_cor",\
                            "jpsps-sbr_cor",\
                            "jpsps_cor",\
                            "jptoi_cor",\
                            "jptoo-pst_cor",\
                            "jptoo-toa_cor",\
                            "jptoo-ton_cor",\
                            "jptoo-tor_cor",\
                            "jpcrp030000-asr_E04426-000",\
                            "jpigp_cor"])
        prefix_sec = set(["currency",\
                        "country",\
                        "dei",\
                        "exch",\
                        "srt",\
                        "stpr",\
                        "us-gaap"])
                            
        self.__prefixies = prefix_edinet
        self.__prefixies |= prefix_sec

    def prefix(self):
        return self.__prefixies

    def to_json(self, text: str) -> dict:
        import json

        ast: list = self.__parser.parse(text)

        data: dict = {}

        for i in range(len(ast)-1):
            #print(tag)
            if type(ast[i]) is not str:
                key: set = self.prefix().intersection(ast[i].keys())
    
                if len(key) == 0:
                    continue

                if len(key) != 1:
                    print(key)
                    err_msg("Multiple keys are defined")
                    sys.exit(1)

                target_key = str(*key)
                if len(ast[i][target_key]) != 2:

                    if type(ast[i+1]) is not str:
                        continue

                    data_key = ast[i][target_key] 
                    context_key = ast[i]["contextRef"]

                    ast[i].pop(target_key)
                    ast[i].pop("contextRef")
                    ast[i]["value"] = ast[i+1]
                   
                    if not data_key in data:
                        data[data_key] = {}

                    data[data_key][context_key] = ast[i]

        return data
