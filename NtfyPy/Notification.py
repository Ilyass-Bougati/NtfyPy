import requests

class Notification:
    def __init__(self, message: str, title: str, priority="default", tags="") -> None:
        """
        Initializes the Notification object

        Args:
            message (str): The body of the notification
            title (str): The title of the notification
            priority (str): The priority of the notification, changes the imoji and the vibration. Default value is `default`
            tags (str): The tags of the notification, changes its imoji
        """
        self.priority = priority
        self.tags = tags
        self.message = message
        self.title = title

class Ntfy:
    def __init__(self, topic: str, host="localhost", port="80") -> None:
        """
        Initializes a Ntfy object

        Args:
            topic (str): the notification topic, if you are not subscribed to this topic from your mobile you will not receive the notification
            host (str): the Ntfy server host, the default is `localhost`
            port (str): the ntfy server port, the default is `80`
        """

        self.topic = topic
        self.host = host
        self.port = port
    
    def send(self, notification: Notification) -> None:
        """
        Sends a notification to the subscribed mobile devices

        Args:
            notification: The notification data
        """

        requests.post(
            url=f"http://{self.host}:{self.port}/{self.topic}",
            headers={
                "Title": notification.title,
                "Priority": notification.priority,
                "Tags": notification.tags
            },
            data=notification.message
        )