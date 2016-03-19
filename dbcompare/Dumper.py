class Dumper:
    """Dump data in csv/html """

    def __init__(self):
        pass

    def csvdump(self, data, loc):
        
        out = ""
        for key in data.keys():
            out += str(key) + ","
            out += ",".join(data[key])
            out += "\n"

        with open(loc, 'w') as writer:
            writer.write(out)


