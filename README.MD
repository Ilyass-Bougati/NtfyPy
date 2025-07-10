# Mobiles notification
Following the [Ntfy documentations](https://docs.ntfy.sh/) we can create a docker container which will take care of all the underlying API for us. We simply run
```
sudo docker run -p 80:80 -itd binwiederhier/ntfy serve
```
You'll have to unstall the [ntfy](https://play.google.com/store/apps/details?id=io.heckel.ntfy&hl=en&pli=1) application, and change the default server to the address of your machine, then subscribe to a topic. Sending notifications can be done with `curl`
```bash
curl -d "Hello" 192.168.0.xxx/topic
```
Keep in mind this won't work for iphone devices.

# Using the package
This is the example code provided in the `notification.py` script
```py
from NtfyPy.Notification import *

# Before using this application the Ntfy server should
# be already running and everything is setup in the phone 
# side. Read the documentation for more informations
# https://docs.ntfy.sh/

# This function creates a Ntfy Client and will send
# notifications to the 'test' topic here
ntfy = Ntfy("test")

# Here we're setting up the notificaiton that we
# will be sending to the user
notification = Notification(
    message = "Your bot has lost 29$ trading today",
    priority = "urgent",
    tags = "warning",
    title = "Oh ooh..."
)

# And with this one line we send a notification to the user
ntfy.send(notification)
```

This code sends a simple notificaiton to your mobile device