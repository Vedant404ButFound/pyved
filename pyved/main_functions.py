import os
import platform
import pywhatkit as kit
import webbrowser as web
import wikipedia,time
from plyer import notification


class UnvalidLink_Or_NoInternetConnection(Exception):pass
def watch_video(link):
    try:
        web.open(link)
    except:
        raise UnvalidLink_Or_NoInternetConnection
def clear_output():
    os.system('cls') #clear all previous output
def send_noti(article):
    """
    Send Notification From Wikipedia Artricle
    """
    search = wikipedia.search(article)
    info = wikipedia.summary(search[0])
    notification.notify(
        title=f'About {article}',
        message=info[:256],
        timeout=10,
    )