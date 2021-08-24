
import sys
from xbrl_parser import XbrlApp

if __name__ == "__main__":

    xbrl_app : XbrlApp = XbrlApp()

    filename : str = sys.argv[1]
    text = open(filename).read()

    data: dict = {}
    data = xbrl_app.to_json(text)
    print(data)
