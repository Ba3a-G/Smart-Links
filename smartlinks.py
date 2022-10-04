import parsers

class Intent():

    def __init__(self, url):
        anat = url.split("/", maxsplit=3)
        self.domain = anat[2]
        self.service = self.domain.split(".")[-2]
        self.url = f"https://{self.domain}/{anat[3]}"

        # import parser module
        try:
            self.parser = getattr(parsers, self.service)
        except:
            self.parser = getattr(parsers, general)

    def getIntents(self):
        try:
            intents = self.parser(self.url)
        except:
            pass
        return intents