import json

SAMPLEPROGRAM = [
    (0, 1),
    (2000, 0),
    (2000, 1),
    (500, 0),
    (500, 1),
    (500, 0),
    (500, 1),
    (500, 0),
    (2000, 1),
    (2000, 0),
    (500, 1),
    (5000, 0),
    (0, 98)
    ]

class Model:
    def __init__(self):
        pass

    def homepage(self, args):
        return "Nothing to see here"

    def test(self, args):
        return str(args)

    def getProgram(self):
        return json.dumps(SAMPLEPROGRAM)
