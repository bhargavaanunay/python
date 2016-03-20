from collections import defaultdict
from json import dumps

class JSONDumper:

    def __init__(self):
        pass

    
    def __jsondump__(self, keyheader, key, data):
        ret = {keyheader:key}
        for field in data:
            ret[field[0]] = "||".join(field[1:])
        return dumps(ret)

    
    def getJSONDump(self, data, keyheader):
        ret = "["
        ret += ",".join([self.__jsondump__(keyheader, key, data[key]) for key in data.keys()])
        ret += "]"
        return ret

class Dumper:
    """Dump data in csv/html """

    def __init__(self):
        pass

    def csvdump(self, data, loc, keyheader, src, des):
        
        keys = sorted(data.keys(), key=lambda k: len(data[k]), reverse=True)
        out = []
        for key in keys:
            out.extend([key+","+",".join(field) for field in data[key]])
        
        csvoutput = "\n".join(out)
        
        with open(loc, 'w') as writer:
            writer.write(csvoutput)


    def htmldump(self, data, loc, keyheader):
        jsonDumper = JSONDumper()
        with open('template/app.js', 'r') as app:
            js = app.read()
        js = js.replace("%%data%%", jsonDumper.getJSONDump(data, keyheader))
        
        with open(loc, 'w') as writer:
            writer.write(js)
    

    def jsondump(self, data, loc, keyheader):
        """Dumps data in json format"""

        jsonDumper = JSONDumper()
        with open(loc, 'w') as writer:
            writer.write(jsonDumper.getJSONDump(data, keyheader))


