import importlib

class Intent():

    def __init__(self, url):
        anat = url.split("/", maxsplit=3)
        self.domain = anat[2]
        self.service = self.domain.split(".")[-2]
        self.url = f"https://{self.domain}/{anat[3]}"

        # import parser module
        try:
            self.parser = importlib.import_module(f".{self.service}", package="parsers")
        except:
            print("importing general module")
            self.parser = importlib.import_module(".general", package="parsers")

    def getIntents(self):
        intents = self.parser.createIntents(self.url)
        return {"web": intents.intentWeb, "android": intents.intentAndroid, "ios": intents.intentIOS}