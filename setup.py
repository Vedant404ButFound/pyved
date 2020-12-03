from setuptools import find_packages
from distutils.core import setup
long_desc = '''
# pyved

## *def* **birthday_wisher**(*xlsx_file*):

"""

This Function Wish Your Friends,Family Members etc.Bitrhday On Behalf Of You.

`This Function Take One Argument As '*.xlsx' File With An Extension And Without Any Type Of Case And Spelling Mistake`

### In Your xlsx File There Will Be **'Name'** Row,A **'Birthday'**(**DD/MM**) Row ,A 'Year'(**YYYY**) Row And 'Mobile No.'(**with Country Code without '+' And 'Mobile No.' Also Will Be A Whatsapp Number**) Row **Without Any Type Of Spelling Mistake.**

"""

### Example:

![Could't Load Image](https://github.com/Vedant404ButFound/pyved/blob/master/pyved/static/Example.png)

## *def* **send_noti**(*sub*):
"""
### **Send Notification From Wikipedia Artricle**
"""

### Example :

![Could't Load Image](https://github.com/Vedant404ButFound/pyved/blob/master/pyved/static/Notification.png)

## *def* **create_xlsx**(*birthday_counts*,*filename*='data'):
    """
###    Create **'*.xlsx'** File For **'birthday_wisher'** Function And Reduces Work Of Users.This Function Take 2 Arguements As **birthday_counts** As *Integer* And **filename** As *String* **Default filename Is data**.
    """
'''
setup(
    name='pyved',
    version='1.1',
    packages=find_packages(),
    install_requires=['pandas','pywhatkit','xlrd','openpyxl','plyer'],
    author='Vedant Goswami',
    url='https://github.com/Vedant404ButFound/pyved/',
    download_url='https://github.com/Vedant404ButFound/pyved_install/raw/master/pyved-1.1.tar.gz',
    author_email='vedant2904goswami@gmail.com',
    license='MIT',
    description='pyved Is Simple Python Based Library For Begineers',
    long_description=long_desc
)