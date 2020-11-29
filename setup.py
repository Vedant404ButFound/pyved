from setuptools import find_packages,setup
def readme():
    with open('README.MD','r') as f:
        content = f.read()
    return content
setup(
    name='pyved',
    version='1.0',
    packages=find_packages(),
    install_requires=['pandas','pywhatkit','bs4','pyfiglet','xlrd','openpyxl','plyer'],
    author='Vedant Goswami',
    url='https://www.github.com/Vedant404ButFound/pyved',
    download_url='https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/Vedant404ButFound/pyved/blob/master/dist/pyved-1.0.tar.gz',
    long_description=readme(),
    

)