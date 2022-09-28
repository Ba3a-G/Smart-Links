class createIntents():

    def __init__(self, url):
        body = url.strip().split("?")[0]
        body = body.split("/", maxsplit=2)[2]
        parts = body.split("/")

        if len(parts) == 4 and parts[2]=="status":
            statusId = parts[3]
            self.intentIOS = f"twitter://status?id={statusId}"
        elif len(parts) == 2:
            username = parts[1]
            self.intentIOS = f"twitter://user?screen_name={username}"
        else:
            self.intentIOS = f"https://{body}"
        
        self.intentAndroid = f"intent://{body}#Intent;package=com.twitter.android;scheme=https;end"
        self.intentWeb = f"https://{body}/"
