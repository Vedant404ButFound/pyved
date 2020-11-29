import wikipedia,time
from plyer import notification
def send_noti(sub):
    """
    Send Notification From Wikipedia Artricle
    """
    searchName = sub
    search = wikipedia.search(searchName)
    info = wikipedia.summary(search[0])
    notification.notify(
        title=f'About {searchName}',
        message=info[:256],
        timeout=10,
        app_icon='pyved/static/noti.ico',
        app_name='VS Code'
    )