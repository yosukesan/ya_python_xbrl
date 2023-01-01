
from ya_python_xbrl import XbrlLexer, XbrlApp, XbrlParser

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

def test_parser_to_json():

    xbrl_app : XbrlApp = XbrlApp()

    text = "<jpcrp_cor:NetSalesSummaryOfBusinessResults contextRef=\"Prior4YearDuration\" unitRef=\"JPY\" decimals=\"-6\">12256000000</jpcrp_cor:NetSalesSummaryOfBusinessResults>" \
         + "<jppfs_cor:NetSales contextRef=\"Prior1YearDuration\" unitRef=\"JPY\" decimals=\"-6\">51683000000</jppfs_cor:NetSales>"
    #data = xbrl_app.to_json(text)

    #assert "JPY" == data['XBRL_start']['jpdei_cor']["NetSalesSummaryOfBusinessResults"]["Prior4YearDuration"]["unitRef"]
    #assert "-6" == data["NetSalesSummaryOfBusinessResults"]["Prior4YearDuration"]["decimals"]
    #assert "12256000000" == data["NetSalesSummaryOfBusinessResults"]["Prior4YearDuration"]["value"]

def test_parser():

    text = "<jpcrp_cor:NetSalesSummaryOfBusinessResults contextRef=\"Prior4YearDuration\" unitRef=\"JPY\" decimals=\"-6\">12256000000</jpcrp_cor:NetSalesSummaryOfBusinessResults>" \
         + "<jppfs_cor:NetSales contextRef=\"Prior1YearDuration\" unitRef=\"JPY\" decimals=\"-6\">51683000000</jppfs_cor:NetSales>"
    xbrl_parser : XbrlParser = XbrlParser()
    data = xbrl_parser.parse(text)

if __name__ == "__main__":

    test_lex_edinet_single_tag()
    test_lex_edinet_multiple_tags()
    test_lex_sec_multiple_tags()
    #test_unrequired_tags()

    #test_parser_to_json()

    test_parser()
