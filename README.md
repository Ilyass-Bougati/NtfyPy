# NtfyPy ![python version](https://img.shields.io/badge/python-3-blue) ![pydantic version](https://img.shields.io/badge/pydantic_settings-2.10.1-blue) ![requests version](https://img.shields.io/badge/requests-2.25.1-blue)

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
from NtfyPy.Notification import Ntfy, Notification
from NtfyPy.Decorator import NotifyRes, Notify

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

# For convenience you can you the @Notify decorator to skip the 
# initilization of the objects
@Notify("test", "The the training is done", "Your AI model has finished training", "high")
def train():
    pass

train()

# And for even more convenience you can use @NotifyRes which
# Which notifies you about the result of running your function
@NotifyRes("test", "high")
def sum(a: int, b: int):
    return a + b

sum(5, 3)
```

To change the default `host` and `port` you can modify the `.env` file following the example provided
```env
NTFY_HOST=localhost
NTFY_PORT=333
```


## Use Case: Notify When Build or Deployment Finishes

You can integrate NtfyPy into your deployment script to get a phone notification when the process completes. Note here that the `notify.py` and `error.py` are the ones using the `NtfyPy` package

Example Bash snippet:
```bash
# Run your deployment process
your_deploy_command
DEPLOY_STATUS=$?

# Notify via ntfy
if [[ "$*" == *"--ntfy"* ]]; then
    if [[ "$DEPLOY_STATUS" == "0" ]]; then
        ./utils/notify.py my_topic
    else
        ./utils/error.py my_topic
    fi
fi
```

The `error.py` file
```py
#!/usr/bin/python3

from NtfyPy.Notification import Notification, Ntfy
from sys import argv

# Checking if a topic was provided
if len(argv) != 2:
    print("Wrong usage of the script")
    print("usage : ")
    print("     ./notify.py [topic]")
    exit(1)


TOPIC = argv[1]
ntfy = Ntfy(TOPIC)

# Sending the notification
notification = Notification(
    message = "Error building the images",
    priority = "high",
    tags = "rotating_light",
    title = "Alexandre"
)
ntfy.send(notification)
```

You can also use the cli tool
```bash
ntfypy [topic] [command]
```