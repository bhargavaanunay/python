from collections import defaultdict

class ConfigReader:
    """Reads db compare config from file"""

    def __init__(self, linedelim):
        self.__linedelim__ = linedelim

    def readConfigFile(self, absfilepath):
        """Read config file and generate SQL/KEY Map"""

        with open(absfilepath, 'r') as config:
            lines = config.read().splitlines()
        return self.__generateMap__(lines)


    def __generateMap__(self, lines):
        """Generate 2-D Array , x=sno, y=SQL/KEY"""

        d = defaultdict(dict)
        for line in lines:
            cfg = line.split(self.__linedelim__)
            d[cfg[0]][cfg[1]] = cfg[2]
        return d
