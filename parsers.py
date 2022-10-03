import re

def twitter(link):
    if f"/status/" in link:
        m = (re.search(r"twitter.com\/[\w\-.]{3,}\/status\/[\d]{3,}", link)).group(0)
        stat = (re.search(r"[\d]{3,}", link)).group(0)
        return {"web": m, "android": f"intent://{m}#Intent;package=com.twitter.android;scheme=https;end", "ios": f"twitter://status?id={stat}"}
    else:
        m = (re.search(r"twitter.com\/[\w\-.]{3,}", link)).group(0)
        return {"web": m, "android": f"intent://{m}#Intent;package=com.twitter.android;scheme=https;end", "ios": f"twitter://user?screen_name={m[12:]}"}

def youtube(link):
    m = (re.search(r"youtube.com\/watch\?v\=[\w\-]{3,}", link)).group(0)
    return {"web": m, "android": f"intent://{m}#Intent;package=com.google.android.youtube;scheme=https;end", "ios": f"vnd.youtube://{m[20:]}"}
        
#return {"web": m, "android": f"", "ios": f""}