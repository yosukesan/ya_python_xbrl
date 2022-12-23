Yet Another Python XBRL Parser
###############################################################################

![example branch parameter](https://github.com/github/docs/actions/workflows/main.yml/badge.svg?branch=main)

Top down parser for XBRL.

Sample Code (sample.py)
===============================================================================

This is a sample to read and convert a xbrl file to json.::

 import sys
 from xbrl_parser import XbrlApp
 
 if __name__ == "__main__":
 
     xbrl_app : XbrlApp = XbrlApp()
 
     filename : str = sys.argv[1]
     text = open(filename).read()
     xbrl_app.to_json(text)

To run
===============================================================================
::

    python3 sample.py ${xbrl_file}

xbrl files are available from sec, edinet and others.

* SEC (Edger), USA
https://www.sec.gov/edgar/searchedgar/companysearch.html

* Edinet, JAPAN
https://disclosure.edinet-fsa.go.jp/
