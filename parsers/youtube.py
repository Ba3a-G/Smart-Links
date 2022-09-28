class createIntents():

    def __init__(self, url):
        body = url.strip().split("/", maxsplit=2)[2]
        try:
            vidID = "&v=" + body.split("watch?v=")[1]
        except:
            vidID = ""
        self.intentWeb = f"https://{body}/"
        self.intentAndroid = f"intent://{body}#Intent;package=com.google.android.youtube;scheme=https;end"
        self.intentIOS = f"vnd.youtube://{body}{vidID}"