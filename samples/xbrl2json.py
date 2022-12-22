
import sys
from ya_python_xbrl.xbrl_parser import XbrlApp

if __name__ == "__main__":
    import json

    xbrl_app : XbrlApp = XbrlApp()

    filename : str = sys.argv[1]
    text = open(filename).read()

    data: dict = {}
    data = xbrl_app.to_json(text)
    print(json.dumps(data))
