class createIntents():

    def __init__(self, url):
        body = url.strip().split("/", maxsplit=2)[2]
        self.content = body.split("/")[2]
        self.intentAndroid = f"intent://user/{self.content}/#Intent;package=com.facebook.orca;scheme=fb-messenger;end"
        self.intentIOS = f"fb-messenger-public://user-thread/{self.content}"
        self.intentWeb = f"https://www.messenger.com/t/{self.content}"