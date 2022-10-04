import re

def twitter(link):
    if f"/status/" in link:
        m = (re.search(r"twitter.com\/[\w\-.]+\/status\/[\d]+", link)).group(0)
        stat = (re.search(r"[\d]+", link)).group(0)
        return {"web": m, "android": f"intent://{m}#Intent;package=com.twitter.android;scheme=https;end", "ios": f"twitter://status?id={stat}"}
    else:
        m = (re.search(r"twitter.com\/[\w\-.]+", link)).group(0)
        return {"web": m, "android": f"intent://{m}#Intent;package=com.twitter.android;scheme=https;end", "ios": f"twitter://user?screen_name={m[12:]}"}
def youtube(link):
    m = (re.search(r"youtube.com\/watch\?v\=[\w\-]+", link)).group(0)
    return {"web": m, "android": f"intent://{m}#Intent;package=com.google.android.youtube;scheme=https;end", "ios": f"vnd.youtube://{m[20:]}"}   
def instagram(link):
    if f"/p/" in link:
        m = (re.search(r"instagram.com\/p\/[\w\-\.]+", link)).group(0)
        return {"web": m, "android": f"intent://{m}#Intent;package=com.instagram.android;scheme=https;end", "ios": f"instagram://media?id={m[16:]}"}
    else:
        m = (re.search(r"instagram.com\/[\w\-\.]+", link)).group(0)
        return {"web": m, "android": f"intent://{m}#Intent;package=com.instagram.android;scheme=https;end", "ios": f"instagram://user?username={m[14:]}"}
def snapchat(link):
    if f"/add/" in link:
        m = (re.search(r"snapchat.com\/add\/[\w\.]+", link)).group(0)
        return {"web": m, "android": f"intent://add/{m[16:]}#Intent;package=com.snapchat.android;scheme=snapchat;end;", "ios": f"snapchat://add/{m[16:]}"}
    else:
        m = (re.search(r"snapchat.com\/discover\/[\w\.]+", link)).group(0)
        return {"web": m, "android": f"intent://discover/{m[22:]}#Intent;package=com.snapchat.android;scheme=snapchat;end;", "ios": f"snapchat://discover/{m[22:]}"}
def messenger(link):
    m = (re.search(r"messenger.com\/t\/[\d\.]+", link)).group(0)
    return {"web": m, "android": f"intent://user/{m[16:]}/#Intent;package=com.facebook.orca;scheme=fb-messenger;end", "ios": f"fb-messenger-public://user-thread/{m[16:]}"}



#return {"web": m, "android": f"", "ios": f""}