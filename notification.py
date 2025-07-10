from ntpy.Notification import *

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