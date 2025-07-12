from NtfyPy.Notification import Notification, Ntfy
from sys import argv
from os import system

def run_command():
    # the ntfy client
    ntfy = Ntfy(argv[1])

    # creating the command and running it
    cmd = " ".join(argv[2:])
    system(cmd)

    # creating the notification
    notification = Notification(
        title = "Command finished running",
        message=f"Finished running:\n{cmd}",
        priority="default",
        tags="rotating_light"
    )

    ntfy.send(notification)

def main():
    if len(argv) <= 2:
        print("Usage:")
        print("     ntfypy [topic] [The command to run]")
        exit(1)

    run_command()