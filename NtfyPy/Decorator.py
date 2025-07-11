from NtfyPy.Notification import Notification, Ntfy
from NtfyPy.Settings import NtfyConfig


def Notify(topic: str, title: str, message: str, priority = "default", tags = "", host = NtfyConfig.host, port = NtfyConfig.port):
    """
    This decorator will send a custom notification when the function finishes execution
    """
    
    # Creating a client object
    ntfy = Ntfy(topic, host, port)
    
    # Creating the notification object
    notification = Notification(message, title, priority, tags)
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Executing the function
            res = func(*args, **kwargs)

            # Sending the notification
            ntfy.send(notification)
            return res
        return wrapper
    return decorator


def NotifyRes(topic: str, priority = "default", tags = "", host = NtfyConfig.host, port = NtfyConfig.port):
    """
    This decorator will send the result of running a function as a notification when it finishes execution
    """

    # Creating a client object
    ntfy = Ntfy(topic, host, port)
    
    # Creating the notification object
    notification = Notification("", "", priority, tags)
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Executing the function
            res = func(*args, **kwargs)

            # Sending the notification
            notification.title = f"Finished running the function {func.__name__}"
            notification.message = str(res)
            ntfy.send(notification)
            return res
        return wrapper
    return decorator