
from xbrl_parser import XbrlLexer, XbrlApp

def test_lex_edinet_single_tag():

    text : str = "<jpcrp_cor:NetSalesSummaryOfBusinessResults contextRef=\"Prior4YearDuration\" unitRef=\"JPY\" decimals=\"-6\">12256000000</jpcrp_cor:NetSalesSummaryOfBusinessResults>"

    lexer : XbrlLexer = XbrlLexer()
    ast: list = lexer.lex(text)

    # start tag
    assert "jpcrp_cor" in ast[0]
    assert ast[0]["jpcrp_cor"] == "NetSalesSummaryOfBusinessResults"
    assert "contextRef" in ast[0]
    assert ast[0]["contextRef"] == "Prior4YearDuration"
    assert "unitRef" in ast[0]
    assert ast[0]["unitRef"] == "JPY"
    assert "decimals" in ast[0]
    assert ast[0]["decimals"] == "-6"

    ## value    
    assert ast[1] == "12256000000"

    ## end tag
    assert "jpcrp_cor" in ast[2]
    assert ast[2]["jpcrp_cor"] == "NetSalesSummaryOfBusinessResults"

def test_lex_edinet_multiple_tags():

    text = "<jpcrp_cor:NetSalesSummaryOfBusinessResults contextRef=\"Prior4YearDuration\" unitRef=\"JPY\" decimals=\"-6\">12256000000</jpcrp_cor:NetSalesSummaryOfBusinessResults>" \
         + "<jppfs_cor:NetSales contextRef=\"Prior1YearDuration\" unitRef=\"JPY\" decimals=\"-6\">51683000000</jppfs_cor:NetSales>"

    lexer : XbrlLexer = XbrlLexer()
    ast: list = lexer.lex(text)

    print(ast)
    #
    #assert ast[0][0][0] == "jpcrp_cor"
    #assert ast[0][0][1] == "NetSalesSummaryOfBusinessResults"
    #assert ast[0][1][0] == "contextRef"
    #assert ast[0][1][1] == "Prior4YearDuration"
    #assert ast[0][2][0] == "unitRef"
    #assert ast[0][2][1] == "JPY"
    #assert ast[0][3][0] == "decimals"
    #assert ast[0][3][1] == "-6"
    #assert ast[1] == "12256000000"
    #assert ast[2][0] == "jpcrp_cor"
    #assert ast[2][1] == "NetSalesSummaryOfBusinessResults"

    #assert ast[3][0][0] == "jppfs_cor"
    #assert ast[3][0][1] == "NetSales"
    #assert ast[3][1][0] == "contextRef"
    #assert ast[3][1][1] == "Prior1YearDuration"
    #assert ast[3][2][0] == "unitRef"
    #assert ast[3][2][1] == "JPY"
    #assert ast[3][3][0] == "decimals"
    #assert ast[3][3][1] == "-6"
    #assert ast[4] == "51683000000"
    #assert ast[5][0] == "jppfs_cor" 
    #assert ast[5][1] == "NetSales"

def test_lex_edinet_unrequired_tags():

    pass
    #text = "</xbrli:unit>" \
    #          + "   <xbrli:unit id=\"pure\">" \
    #          + "<xbrli:measure>xbrli:pure</xbrli:measure>" \
    #          + "</xbrli:unit>" \
    #          + "   <jpdei_cor:NumberOfSubmissionDEI contextRef=\"FilingDateInstant\" unitRef=\"pure\" decimals=\"0\">1</jpdei_cor:NumberOfSubmissionDEI>" \
    #          + "  <jpcrp_cor:NetSalesSummaryOfBusinessResults contextRef=\"Prior4YearDuration\" unitRef=\"JPY\" decimals=\"-6\">12256000000</jpcrp_cor:NetSalesSummaryOfBusinessResults>"
    #lexer : XbrlLexer = XbrlLexer()
    #ast: list = lexer.lex(text)

def test_lex_sec_multiple_tags():
    
    pass
    #text = "<us-gaap:ProceedsFromStockOptionsExercised contextRef=\"FD2015Q4YTD\" decimals=\"-6\" id=\"Fact-AEA46EECCA06CB405626CA51513F8CA7\" unitRef=\"usd\">393000000</us-gaap:ProceedsFromStockOptionsExercised>" \
	#    + "<us-gaap:ProfitLoss contextRef=\"FD2013Q4YTD_us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeAxis_us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeMember\" decimals=\"-6\" id=\"Fact-26FFDDCAA0BC20EBEA0BA1D6E8A3FB70\" unitRef=\"usd\">222000000</us-gaap:ProfitLoss>" \
	#    + "<us-gaap:ProfitLoss contextRef=\"FD2013Q4YTD_us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeAxis_us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeMember_us-gaap_StatementEquityComponentsAxis_us-gaap_AccumulatedNetGainLossFromDesignatedOrQualifyingCashFlowHedgesMember\" decimals=\"-6\" id=\"Fact-05BB13363FEDFE76AAEAA1D6CD2694A9\" unitRef=\"usd\">60000000</us-gaap:ProfitLoss>"
    #lexer : XbrlLexer = XbrlLexer()
    #ast: list = lexer.lex(text)

    #assert ast[0][0][0] == "us-gaap"
    
def test_parser_to_json():

    xbrl_app : XbrlApp = XbrlApp()

    text = "<jpcrp_cor:NetSalesSummaryOfBusinessResults contextRef=\"Prior4YearDuration\" unitRef=\"JPY\" decimals=\"-6\">12256000000</jpcrp_cor:NetSalesSummaryOfBusinessResults>" \
         + "<jppfs_cor:NetSales contextRef=\"Prior1YearDuration\" unitRef=\"JPY\" decimals=\"-6\">51683000000</jppfs_cor:NetSales>"
    xbrl_app.to_json(text)

if __name__ == "__main__":

    test_lex_edinet_single_tag()
    #test_lex_edinet_multiple_tags()
    #test_lex_sec_multiple_tags()
    #test_unrequired_tags()

    test_parser_to_json()
