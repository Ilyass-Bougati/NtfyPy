import requests

class Notification:
    def __init__(self, message: str, title: str, priority="default", tags="") -> None:
        self.priority = priority
        self.tags = tags
        self.message = message
        self.title = title

class Ntfy:
    def __init__(self, topic: str, host="localhost", port="80") -> None:
        self.topic = topic
        self.host = host
        self.port = port
    
    def send(self, notification: Notification) -> None:
        requests.post(
            url=f"http://{self.host}:{self.port}/{self.topic}",
            headers={
                "Title": notification.title,
                "Priority": notification.priority,
                "Tags": notification.tags
            },
            data=notification.message
        )