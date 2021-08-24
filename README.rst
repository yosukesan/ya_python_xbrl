Yet Another Python XBRL Parser
###############################################################################

Top down parser for XBRL.

### Sample Code (sample.py)
```
 import sys
 from xbrl_parser import XbrlApp
 
 if __name__ == "__main__":
 
     xbrl_app : XbrlApp = XbrlApp()
 
     filename : str = sys.argv[1]
     text = open(filename).read()
     xbrl_app.to_json(text)
```

### To run
```
    python3 sample.py ${xbrl_file}
```

xbrl files are available from sec, edinet and others.

* SEC (Edger)
https://www.sec.gov/edgar/searchedgar/companysearch.html

* Edinet
https://disclosure.edinet-fsa.go.jp/
