import os
import platform
import pyfiglet as fig
import pywhatkit as kit
import webbrowser as web

class UnvalidLink_Or_NoInternetConnection(Exception):pass
def watch_video(link):
    try:
        web.open(link)
    except:
        raise UnvalidLink_Or_NoInternetConnection
def ASCII_Art(string):
    """
    Return ASCII Art Of Given String In Argument
    """
    ascii_art = fig.figlet_format(string)
    return ascii_art

def clear_output():
    os.system('cls')