from collections import defaultdict

class Comparer:
    """Compare data between two list of tuples"""

    def __init__(self, delim):
        """Takes key delimiter to avoid false collisions"""
        
        self.__headers__= []
        self.__keys__ = []
        self.__delim__= delim

    
    def __gettuplediffindex__(self, source, dest):
        """Generate indices at which tuples have diff"""
        
        return [idx for idx in range(len(source)) if source[idx]!= dest[idx]]


    def getDataDiff(self, source, dest):
        """Generate diff between list of tuples (i.e. cursor data)"""

        indices = self.__generateIndex__()
        sourceMap = self.__generateMap__(source, indices)
        destMap = self.__generateMap__(dest, indices)
        allKeys = set(sourceMap.keys()).union(set(destMap.keys()))
        commonKeys = set(sourceMap.keys()).intersection(set(destMap.keys()))
        onlySourceKeys = set(sourceMap.keys()) - set(destMap.keys())
        onlyDestKeys = set(destMap.keys()) - set(sourceMap.keys())
        
        diff = {}
        for key in commonKeys:
            src = sourceMap[key]
            des = destMap[key]
            diff[key] = [(self.__headers__[idx], src[idx], des[idx]) for idx in self.__gettuplediffindex__(src, des)]
        for key in onlySourceKeys:
            diff[key] = ("Only in src", key)

        for key in onlyDestKeys:
            diff[key] = ("Only in dest", key)

        return diff


    def __generateMap__(self, obj, indices):
        d = defaultdict()
        for element in obj:
            keyList = [str(element[idx]) for idx in indices]
            d[self.__delim__.join(keyList)] = element
        return d

    
    def __generateIndex__(self):
        return [self.__headers__.index(element) for element in self.__keys__]

    
    def setheaders(self, headers):
        self.__headers__ = headers

    
    def getheaders(self):
        return self.__headers__

    
    def setkeys(self, keys):
        self.__keys__ = keys

    
    def getkeys(self):
        return self.__keys__