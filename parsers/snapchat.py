class createIntents():

    def __init__(self, url):
        body = url.strip().split("/", maxsplit=2)[2]
        self.linkType = body.split("/")[1]
        self.content = body.split("/")[2]
        self.generateIntents()

    def generateIntents(self):
        self.intentWeb = f"https://www.snapchat.com/{self.linkType}/{self.content}"
        if self.linkType == "add":
            self.intentAndroid = f"intent://add/{self.content}#Intent;package=com.snapchat.android;scheme=snapchat;end;"
            self.intentIOS = f"snapchat://add/{self.content}"
            self.intentWeb = f"https://www.snapchat.com/add/{self.content}"
        elif self.linkType == "discover":
            self.intentAndroid = f"intent://snapchat.com/discover/{self.content}#Intent;package=com.snapchat.android;scheme=https;end;"
            self.intentIOS = f"snapchat://discover/{self.content}"
            self.intentWeb = f"https://www.snapchat.com/discover/{self.content}"