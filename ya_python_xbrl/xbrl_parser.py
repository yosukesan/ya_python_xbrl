
import sys, math
from collections import defaultdict
from .xbrl_ast import XbrlAst

def err_msg(message):
    print("Error: @" + __name__ + ' ' + message, file=sys.stderr)

def rdict():
    return defaultdict(rdict)

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
        """ refer ASCII table for 48 and 57 """
        return True if 48 <= ord(char) and ord(char) <= 57 else False

class XbrlLexer:

    def __init__(self):

        self.pos : int = 0
        self.tree: XbrlAst = XbrlAst()
        self.t: XbrlToken = XbrlToken()
        self.xbrl_dict : dict = {}

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
        
            self.pos += 1 

        return text[start_pos:self.pos]

    def lex (self, text: str) -> list:
        """
        construct and return abstract syntax tree by top-down
        """

        ast : list = []
        start_tag: dict = {}
        val: str = ""
        end_tag = rdict()
        
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
        self._mode : str = ''
        self._dict = rdict()
       
        # Profit loss 
        self._sales = {'NetSales',
            'SalesOfProductsIFRS',
            'RevenueIFRS',
            'RevenuesUSGAAPSummaryOfBusinessResults',
            'RevenueIFRSSummaryOfBusinessResults',
            'OperatingRevenue1SummaryOfBusinessResults'}

        self._total_sales = {'TotalNetRevenuesIFRS'}

        self._total_cost_and_expenses = {'TotalCostsAndExpensesIFRS'}

        self._cost_of_goods_sold = {'CostOfSales',
            'CostOfSalesIFRS'}

        self._gross_profit = {'OrdinaryIncomeLossSummaryOfBusinessResults',
            'GrossProfitIFRS',
            'GrossProfit'} 

        self._cost_of_general_admin = {'SellingGeneralAndAdministrativeExpenses',
            'SellingGeneralAndAdministrativeExpensesIFRS'}

        self._operating_profit = {'OperatingProfitLoss',
            'OperatingIncome',
            'OperatingProfitLossIFRS',
            'ComprehensiveIncomeSummaryOfBusinessResults'}

        self._profit_loss = {'ProfitLoss'}
        self._profit_loss_ifrs = {'ProfitLossIRFS'}

        # for cash flow statement
        self._income_before_tax = {'IncomeBeforeIncomeTaxes'}
        self._extra_ordinary_profit = {'ExtraordinaryIncome'}
        self._extra_ordinary_loss = {'ExtraordinaryLoss'}
        self._investiment_loss= {'LossOnValuationOfInvestmentSecuritiesEL'}
        # BL
        self._depriciation = {'AccumulatedDepreciationToolsFurnitureAndFixtures'}
        self._amortisation = {}

        self._account_receivable = {'NotesAndAccountsReceivableTrade',
            'AccountsReceivableTradeNet',
            'AccountsReceivableTrade'}
        self._inventory = {'MerchandiseAndFinishedGoods'}
        self._PPE = {'PropertyPlantAndEquipment'}
        self._account_payable = {'NotesAndAccountsPayableTrade', 'AccountsPayableTrade'}

        
        # Aux

        self._num_of_shares = {'NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc',
            'TotalNumberOfIssuedSharesSummaryOfBusinessResults'}

        self._current_year = {'CurrentYTDDuration',
            'CurrentYearDuration',
            'CurrentYTDDuration_NonConsolidatedMember',
            'CurrentYearDuration_NonConsolidatedMember'}

    def current_year(self, data):

        if 'CurrentYTDDuration' in data:
            return data['CurrentYTDDuration']

        if 'CurrentYearDuration' in data:
            return data['CurrentYearDuration']

        if 'CurrentYTDDuration_NonConsolidatedMember' in data:
            return data['CurrentYTDDuration_NonConsolidatedMember']

        if 'CurrentYearDuration_NonConsolidatedMember' in data:
            return data['CurrentYearDuration_NonConsolidatedMember']

        return
       
    def get_mode(self)->str:
        return self._mode

    def is_start_tag(self, i: int, tags) -> bool:
        return 'XBRL_start' in tags[i]

    def is_end_tag(self, i: int, tags) -> bool:
        return 'XBRL_end' in tags[i]

    def is_net_sales(self, i: int, tags) -> bool:
        if 'NetSales' in tags:
            return True

    def is_cost_goods_sold(self, i: int, tags) -> bool:
        if 'CostOfSales' in tags[i]:
            return True

    def is_decimals(self, tag: dict):
        return True if 'decimals' in tag['XBRL_start'] else False

    def decimals(self, tag: dict):
        if not self.is_decimals(tag):
            Warning('decimals could not be found. {0}'.format(tag['XBRL_start']))
            return None

        # since this always be power of 10, cast it to int
        return int(math.pow(10, -int(tag['XBRL_start']['decimals'])))

    def decompose_tag(self, result: dict, tag: list, i: int):

        d = tag[i]['XBRL_start']
        l = list(d.values())
        v : int = 0
        pw = 1

        # Profit Loss
        if l[0] in self._sales:
            if self.is_decimals(tag[i]):
                pw = self.decimals(tag[i])
            time_stamp : str = d['contextRef']
            result['sales'][time_stamp] = int(tag[i+1]) * pw

        if l[0] in self._cost_of_goods_sold: 
            if self.is_decimals(tag[i]):
                pw = self.decimals(tag[i])
            time_stamp : str = d['contextRef']
            result['COGS'][time_stamp] = int(tag[i+1]) * pw

        if l[0] in self._gross_profit:
            if self.is_decimals(tag[i]):
                pw = self.decimals(tag[i])
            time_stamp : str = d['contextRef']
            result['gross_profit'][time_stamp] = int(tag[i+1]) * pw

        if l[0] in self._cost_of_general_admin:
            if self.is_decimals(tag[i]):
                pw = self.decimals(tag[i])
            time_stamp : str = d['contextRef']
            result['GA_expenses'][time_stamp] = int(tag[i+1]) * pw

        if l[0] in self._operating_profit:
            if self.is_decimals(tag[i]):
                pw = self.decimals(tag[i])
            time_stamp : str = d['contextRef']
            result['operating_profit'][time_stamp] = int(tag[i+1]) * pw

        if l[0] in self._profit_loss:
            if self.is_decimals(tag[i]):
                pw = self.decimals(tag[i])
            time_stamp : str = d['contextRef']
            result['profit_loss'][time_stamp] = int(tag[i+1]) * pw

        # IFRS: Profit loss, overwrite tags
        if l[0] in self._total_sales:
            if self.is_decimals(tag[i]):
                pw = self.decimals(tag[i])
            time_stamp : str = d['contextRef']
            result['sales'][time_stamp] = int(tag[i+1]) * pw
            result['gross_profit'][time_stamp] = int(tag[i+1]) * pw - result['cost_of_sales'][time_stamp]

        if l[0] in self._profit_loss_ifrs:
            if self.is_decimals(tag[i]):
                pw = self.decimals(tag[i])
            time_stamp : str = d['contextRef']
            result['profit_loss'][time_stamp] = int(tag[i+1]) * pw

        # Balance Sheet

        return result

    def parse(self, text: str):
        lexer : XbrlLexer = XbrlLexer()
        tags: list = lexer.lex(text)

        for i in range(len(tags)-2):

            if isinstance(tags[i], str):
                continue

            # start tag detection
            if self.is_start_tag(i, tags):
                if isinstance(tags[i]['XBRL_start'], dict):
                    self._dict = self.decompose_tag(self._dict, tags, i)
                
                # check if end tag matches
                if self.is_end_tag(i+2, tags):
                    continue    
                else:
                    tag_end_err : str = 'end tag unmatch: ' + str(tags[i+2])
                    err_msg(tag_end_err)
                    sys.exit(-1)

        return self._dict

class XbrlApp:

    def __init__(self):
        self._parser : XbrlParser = XbrlParser()

    def parse(self, text: str):
        self._data = self._parser.parse(text)

    def current_year(self, data):
        return self._parser.current_year(data)

    def prefix(self):
        return self.__prefixies

    def data(self):
        return self._data

    def fcf(self):
        import pprint
        pprint.pprint(self._data)

    def to_json(self, text: str) -> dict:
        import json

        ast: list = self.__parser.parse(text)

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
