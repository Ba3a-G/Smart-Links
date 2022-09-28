# Smart Links
Links that open directly in app using intents for Android and iOS. For example, any youtube.com URL will open in the Youtube App only.

*All contributors are welcome.*

## Usage
`git clone "https://github.com/ba3a-g/smart-links"`
```python
# In project directory
from smartlinks import Intents
intents = Intent("https://twitter.com/ba3a_gamzo")
intents.getIntents()
```
```json
{
    "web": "https://twitter.com/ba3a_gamzo/",

    "android": "intent://twitter.com/ba3a_gamzo#Intent;package=com.twitter.android;scheme=https;end",

    "ios": "twitter://user?screen_name=ba3a_gamzo"
}
Type: Python Dict
```