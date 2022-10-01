class createIntents():

    def __init__(self, url):
        body = url.strip().split("/", maxsplit=2)[2]
        self.linkType = body.split("/")[1]
        self.content = body.split("/")[2]
        self.generateIntents()

    def generateIntents(self):
        self.intentWeb = f"https://open.spotify.com/{self.linkType}/{self.content}"
        self.intentIOS = self.intentAndroid = f"spotify://{self.linkType}/{self.content}"