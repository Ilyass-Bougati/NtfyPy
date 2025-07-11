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