class createIntents():

    def __init__(self, url):
        raw = url.strip().split("/", maxsplit=3)[3]
        raw = raw.split("?", maxsplit=1)
        self.body = raw[0].strip("/")

        self.intentWeb = url
        self.intentAndroid = f"intent://www.instagram.com/{self.body}/#Intent;package=com.instagram.android;scheme=https;end"
        self.intentWeb = f"https://www.instagram.com/{self.body}/"
        self.generateIntentIOS()

    def codeToMediaID(self, code):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
        media_id = 0;
        for letter in  code:
            media_id = (media_id*64) + alphabet.index(letter)

        return media_id

    def generateIntentIOS(self):
        parts = self.body.split("/")
        if len(parts) == 1:
            self.intentIOS = f"instagram://user?username={parts[0]}"
        else:
            self.intentIOS = f"instagram://media?id={str(self.codeToMediaID(parts[1]))}"
