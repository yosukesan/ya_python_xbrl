
from ya_python_xbrl import XbrlLexer, XbrlApp, XbrlParser, XbrlApp

def test_lex_edinet_single_tag():

    def jpcrp_cor():
        """ test for jpcrp_cor ://www.google.com/aclk?sa=L&ai=DChcSEwjm-oLd4P3yAhVCJSsKHSqUD9AYABA2GgJzZg&sig=AOD64_3qCDUzpYJAG3r1ec2MUmA5mSWSOw&ctype=5&q=&ved=0ahUKEwjypfzc4P3yAhUaet4KHWJMA84QwzwIxwI&adurl= tag
        """
        text : str = "<jpcrp_cor:NetSalesSummaryOfBusinessResults" \
                   + " contextRef=\"Prior4YearDuration\"" \
                   + " unitRef=\"JPY\"" \
                   + " decimals=\"-6\">" \
                   + "12256000000" \
                   + "</jpcrp_cor:NetSalesSummaryOfBusinessResults>"

        lexer : XbrlLexer = XbrlLexer()
        ast: list = lexer.lex(text)

        # start tag 
        assert "jpcrp_cor" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["jpcrp_cor"] == "NetSalesSummaryOfBusinessResults"
        assert "contextRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["contextRef"] == "Prior4YearDuration"
        assert "unitRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["unitRef"] == "JPY"
        assert "decimals" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["decimals"] == "-6"
        ## value    
        assert ast[1] == "12256000000"
        ## end tag
        assert "jpcrp_cor" in ast[2]['XBRL_end']
        assert ast[2]['XBRL_end']["jpcrp_cor"] == "NetSalesSummaryOfBusinessResults"

    def jpdei_cor():
        """ test for jpdei_cor tag
        """

        text: str = "<jpdei_cor:NumberOfSubmissionDEI"\
                + " contextRef=\"FilingDateInstant\""\
                + " unitRef=\"pure\""\
                + " decimals=\"0\">"\
                + "1"\
                + "</jpdei_cor:NumberOfSubmissionDEI>"

        lexer : XbrlLexer = XbrlLexer()
        ast: list = lexer.lex(text)

        #start tag
        assert "jpdei_cor" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["jpdei_cor"] == "NumberOfSubmissionDEI"
        assert "contextRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["contextRef"] == "FilingDateInstant"
        assert "unitRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["unitRef"] == "pure"
        assert "decimals" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["decimals"] == "0"
        # value
        assert ast[1] == "1"
        # end tag
        assert "jpdei_cor" in ast[2]['XBRL_end']
        assert ast[2]['XBRL_end']["jpdei_cor"] == "NumberOfSubmissionDEI"

    def jpcrp030000():
        text : str = "<jpcrp030000-asr_E34064-000:ClassAPreferredSharesTotalNumberOfIssuedSharesSummaryOfBusinessResults"\
                + " contextRef=\"Prior4YearInstant_NonConsolidatedMember\""\
                + " unitRef=\"shares\""\
                + " decimals=\"0\">"\
                + "1500000"\
                + "</jpcrp030000-asr_E34064-000:ClassAPreferredSharesTotalNumberOfIssuedSharesSummaryOfBusinessResults>"
        lexer : XbrlLexer = XbrlLexer()
        ast: list = lexer.lex(text)

        # start tag
        assert "jpcrp030000-asr_E34064-000" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["jpcrp030000-asr_E34064-000"] == "ClassAPreferredSharesTotalNumberOfIssuedSharesSummaryOfBusinessResults"
        assert "contextRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["contextRef"] == "Prior4YearInstant_NonConsolidatedMember"
        assert "unitRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["unitRef"] == "shares"
        assert "decimals" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["decimals"] == "0"
        # value
        assert ast[1] == "1500000"
        # end tag
        assert "jpcrp030000-asr_E34064-000" in ast[2]['XBRL_end']
        assert ast[2]['XBRL_end']["jpcrp030000-asr_E34064-000"] == "ClassAPreferredSharesTotalNumberOfIssuedSharesSummaryOfBusinessResults"

    def jppfs_cor():
        text : str = "<jppfs_cor:OtherCL contextRef=\"Prior1YearInstant\" unitRef=\"JPY\" decimals=\"-6\">1352000000</jppfs_cor:OtherCL>"
        lexer : XbrlLexer = XbrlLexer()
        ast: list = lexer.lex(text)

        # start tag
        assert "jppfs_cor" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["jppfs_cor"] == "OtherCL"
        assert "contextRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["contextRef"] == "Prior1YearInstant"
        assert "unitRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["unitRef"] == "JPY"
        assert "decimals" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["decimals"] == "-6"
        # value
        assert ast[1] == "1352000000"
        # end tag
        assert "jppfs_cor" in ast[2]['XBRL_end']
        assert ast[2]['XBRL_end']["jppfs_cor"] == "OtherCL"

    def jpdei_cor(): 
        text : str = "<jpdei_cor:FilerNameInJapaneseDEI"\
                + " contextRef=\"FilingDateInstant\">"\
                + "株式会社メルカリ"\
                + "</jpdei_cor:FilerNameInJapaneseDEI>"
        lexer : XbrlLexer = XbrlLexer()
        ast: list = lexer.lex(text)
       
        # start tag 
        assert "jpdei_cor" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["jpdei_cor"] == "FilerNameInJapaneseDEI"
        assert "contextRef" in ast[0]['XBRL_start']
        assert ast[0]['XBRL_start']["contextRef"] == "FilingDateInstant"
        # value
        assert "株式会社メルカリ" in ast[1]
        # end tag
        assert "jpdei_cor" in ast[2]['XBRL_end']
        assert ast[2]['XBRL_end']["jpdei_cor"] == "FilerNameInJapaneseDEI"

    jpcrp_cor()
    jpdei_cor()
    jpcrp030000()
    jppfs_cor()

def test_lex_edinet_multiple_tags():

    text = "<jpcrp_cor:NetSalesSummaryOfBusinessResults contextRef=\"Prior4YearDuration\" unitRef=\"JPY\" decimals=\"-6\">12256000000</jpcrp_cor:NetSalesSummaryOfBusinessResults>" \
         + "<jppfs_cor:NetSales contextRef=\"Prior1YearDuration\" unitRef=\"JPY\" decimals=\"-6\">51683000000</jppfs_cor:NetSales>"

    lexer : XbrlLexer = XbrlLexer()
    ast: list = lexer.lex(text)

    # start tag 
    assert "jpcrp_cor" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start']["jpcrp_cor"] == "NetSalesSummaryOfBusinessResults"
    assert "contextRef" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start']["contextRef"] == "Prior4YearDuration"
    assert "unitRef" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start']["unitRef"] == "JPY"
    assert "decimals" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start']["decimals"] == "-6"

    # value
    assert ast[1] == "12256000000"

    # end tag
    assert "jpcrp_cor" in ast[2]['XBRL_end']
    assert ast[2]['XBRL_end'] ["jpcrp_cor"] == "NetSalesSummaryOfBusinessResults"

    # start tag
    assert "jppfs_cor" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["jppfs_cor"] == "NetSales"
    assert "contextRef" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["contextRef"] == "Prior1YearDuration"
    assert "unitRef" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["unitRef"] == "JPY"
    assert "decimals" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["decimals"] == "-6"

    # value 
    assert ast[4] == "51683000000"

    # end tag
    assert "jppfs_cor" in ast[5]['XBRL_end']
    assert ast[5]['XBRL_end']["jppfs_cor"] == "NetSales"

def test_lex_sec_multiple_tags():
    
    pass
    text = "<us-gaap:ProceedsFromStockOptionsExercised contextRef=\"FD2015Q4YTD\" decimals=\"-6\" id=\"Fact-AEA46EECCA06CB405626CA51513F8CA7\" unitRef=\"usd\">393000000</us-gaap:ProceedsFromStockOptionsExercised>" \
	    + "<us-gaap:ProfitLoss contextRef=\"FD2013Q4YTD_us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeAxis_us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeMember\" decimals=\"-6\" id=\"Fact-26FFDDCAA0BC20EBEA0BA1D6E8A3FB70\" unitRef=\"usd\">222000000</us-gaap:ProfitLoss>"

    lexer : XbrlLexer = XbrlLexer()
    ast: list = lexer.lex(text)

    # start tag
    assert "us-gaap" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start'] ["us-gaap"] == "ProceedsFromStockOptionsExercised"
    assert "contextRef" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start'] ["contextRef"] == "FD2015Q4YTD"
    assert "decimals" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start'] ["decimals"] == "-6"
    assert "id" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start'] ["id"] == "Fact-AEA46EECCA06CB405626CA51513F8CA7"
    assert "unitRef" in ast[0]['XBRL_start']
    assert ast[0]['XBRL_start'] ["unitRef"] == "usd"
    # value
    assert ast[1] == "393000000"
    #end
    assert "us-gaap" in ast[2]['XBRL_end']
    assert ast[2]['XBRL_end']["us-gaap"] == "ProceedsFromStockOptionsExercised"

    #start tag
    assert "us-gaap" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["us-gaap"] == "ProfitLoss"
    assert "contextRef" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["contextRef"] == "FD2013Q4YTD_us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeAxis_us-gaap_ReclassificationOutOfAccumulatedOtherComprehensiveIncomeMember"
    assert "decimals" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["decimals"] == "-6"
    assert "id" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["id"] == "Fact-26FFDDCAA0BC20EBEA0BA1D6E8A3FB70"
    assert "unitRef" in ast[3]['XBRL_start']
    assert ast[3]['XBRL_start']["unitRef"] == "usd"
    # value
    assert ast[4] == "222000000"
    # end tag
    assert "us-gaap" in ast[5]['XBRL_end']
    assert ast[5]['XBRL_end']["us-gaap"] == "ProfitLoss"

def test_sales():

    text = '<jpcrp_cor:NetSalesSummaryOfBusinessResults contextRef=\"Prior4YearDuration\" unitRef=\"JPY\" decimals=\"-6\">12256000000</jpcrp_cor:NetSalesSummaryOfBusinessResults>'\
         + '<jppfs_cor:NetSales contextRef=\"Prior1YearDuration\" unitRef=\"JPY\" decimals=\"3\">-51683000000</jppfs_cor:NetSales>'
         #+ '<jppfs_cor:NetSales xsi:nil=\"true\" contextRef=\"CurrentYTDDuration_NonConsolidatedMember_jpcrp040300-q3r_E32620-000InvestmentBusinessReportableSegmentsMember\" unitRef=\"JPY\"/>'

    xbrl_parser : XbrlParser = XbrlParser()
    lexer : XbrlLexer = XbrlLexer()
    lexed: list = lexer.lex(text)
    parsed: dict = xbrl_parser.parse(text)

    assert isinstance(lexed[0]['XBRL_start']['jpcrp_cor'], str)
    assert lexed[0]['XBRL_start']['jpcrp_cor'] == 'NetSalesSummaryOfBusinessResults'
    assert lexed[0]['XBRL_start']['contextRef'] == 'Prior4YearDuration'
    assert lexed[0]['XBRL_start']['unitRef'] == 'JPY'
    assert isinstance(lexed[0]['XBRL_start']['decimals'], str)
    assert lexed[0]['XBRL_start']['decimals'] == '-6'
    assert isinstance(lexed[1], str)
    assert lexed[1] == '12256000000' # stored value check
    assert lexed[2]['XBRL_end']['jpcrp_cor'] == lexed[0]['XBRL_start']['jpcrp_cor'] # closing tag check

    assert isinstance(lexed[3]['XBRL_start']['jppfs_cor'], str)
    assert lexed[3]['XBRL_start']['jppfs_cor'] == 'NetSales'
    assert lexed[3]['XBRL_start']['contextRef'] == 'Prior1YearDuration'
    assert lexed[3]['XBRL_start']['unitRef'] == 'JPY'
    assert lexed[3]['XBRL_start']['decimals'] == '3'
    assert lexed[4] == '-51683000000' # stored value check
    assert lexed[5]['XBRL_end']['jppfs_cor'] == lexed[3]['XBRL_start']['jppfs_cor']

    #assert isinstance(lexed[6]['XBRL_start']['jpcrp_cor'], str)

    # parser test
    #assert isinstance(parsed['sales']['Prior4YearDuration'], int)
    assert isinstance(parsed['sales']['Prior1YearDuration'], int)
    #assert parsed['sales']['Prior4YearDuration'] == 12256000000000000
    assert parsed['sales']['Prior1YearDuration'] == -51683000

  
def test_decimals():
    """
    https://github.com/yosukesan/ya_python_xbrl/issues/18
    """

    text = '<jppfs_cor:ProfitLoss contextRef="Prior1YTDDuration" decimals="-3" unitRef="JPY">787137000</jppfs_cor:ProfitLoss>'\
         + '<jppfs_cor:ProfitLoss contextRef="CurrentYTDDuration" decimals="-3" unitRef="JPY">-500846000</jppfs_cor:ProfitLoss>'

    xbrl_parser : XbrlParser = XbrlParser()
    data = xbrl_parser.parse(text)
    assert isinstance(data['profit_loss']['Prior1YTDDuration'], int)
    assert isinstance(data['profit_loss']['CurrentYTDDuration'], int)
    assert data['profit_loss']['Prior1YTDDuration'] == 787137000000
    assert data['profit_loss']['CurrentYTDDuration'] == -500846000000

def test_BS():

    text = '<jppfs_cor:PropertyPlantAndEquipment contextRef=\"Prior1YearInstant_NonConsolidatedMember\" unitRef=\"JPY\" decimals=\"-3\">41272000</jppfs_cor:PropertyPlantAndEquipment>'\
         + '<jppfs_cor:PropertyPlantAndEquipment contextRef=\"CurrentYearInstant_NonConsolidatedMember\" unitRef=\"JPY\" decimals=\"-3\">60422000</jppfs_cor:PropertyPlantAndEquipment>'

    xbrl_parser : XbrlParser = XbrlParser()
    data = xbrl_parser.parse(text)

    assert data['PPE']['Prior1YearInstant_NonConsolidatedMember'] == 41272000000
    assert data['PPE']['CurrentYearInstant_NonConsolidatedMember'] == 60422000000

    xbrl_app: XbrlApp = XbrlApp()
    xbrl_app.parse(text)
    xbrl_app.current_year(data['PPE']) == data['PPE']['CurrentYearInstant_NonConsolidatedMember'] 

def test_read_cashflow():

    text = '<jppfs_cor:NetCashProvidedByUsedInOperatingActivities contextRef=\"Prior1YearDuration_NonConsolidatedMember\" unitRef=\"JPY\" decimals=\"-3\">12488774000</jppfs_cor:NetCashProvidedByUsedInOperatingActivities>'
    xbrl_parser : XbrlParser = XbrlParser()
    data = xbrl_parser.parse(text)
    assert data['cashflow_from_operation']['Prior1YearDuration_NonConsolidatedMember'] == 12488774000000

if __name__ == "__main__":

    # check lexer
    test_lex_edinet_single_tag()
    test_lex_edinet_multiple_tags()
    test_lex_sec_multiple_tags()

    # check app
    test_decimals()
    test_sales()
    test_BS()
    test_read_cashflow()
