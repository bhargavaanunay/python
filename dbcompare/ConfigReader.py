import json

class ConfigReader:
    """Reads db compare config from file"""

    def __init__(self, key, splitKey):
        self.__key__ = key
        self.__splitKey__ = splitKey

    def getConfigMap(self, absfilepath):
        """Read config file and generate SQL/KEY Map"""

        with open(absfilepath, 'r') as config:
            data = json.load(config)
        self.__enhance__(data)

        return data


    def __enhance__(self, data):
        """Split keys into list"""

        for key in data.keys():
            if data[key].has_key(self.__key__):
                data[key][self.__key__] = data[key][self.__key__].split(self.__splitKey__)

