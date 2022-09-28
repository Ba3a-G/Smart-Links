class createIntents():

    def __init__(self, url):
        body = url.strip().split("/", maxsplit=2)[2]
        self.intentAndroid = self.intentIOS = self.intentWeb = f"https://{body}/"
