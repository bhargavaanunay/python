import json

class ConfigReader:
    """Reads db compare config from file"""

    def __init__(self, keys, splitby):
        self.__keys__ = keys
        self.__splitby__ = splitby

    def getConfigMap(self, absfilepath):
        """Read config file and generate SQL/KEY Map"""

        with open(absfilepath, 'r') as config:
            data = json.load(config)
        self.__enhance__(data)

        return data


    def __enhance__(self, data):
        """Split keys into list"""

        for key in data.keys():
            for splitkey in self.__keys__:
                if data[key].has_key(splitkey):
                    data[key][splitkey] = data[key][splitkey].split(self.__splitby__)
