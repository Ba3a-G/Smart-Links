class createIntents():

    def __init__(self, url):
        body = url.split("/", maxsplit=2)[2]
        self.intentAndroid = self.intentIOS = f"snssdk1233://webview?url={body}"
        self.intentWeb = f"https://{body}"
