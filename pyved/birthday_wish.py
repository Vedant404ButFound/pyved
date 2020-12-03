import pandas as pd
import pywhatkit
import os
import datetime
def birthday_wisher(xlsx_file):
    """
    This Function Wish Your Friends,Family Members etc.Bitrhday On Behalf Of You.
    This Function Take One Argument As '*.xlsx' File With An Extension And Without Any Type Of Case And Spelling Mistake. 
    In Your xlsx File There Will Be 'Name' Row,A 'Birthday'(DD/MM) Row ,A 'Year'(YYYY) Row And 'Mobile No.'(with Country Code without '+' And 'Mobile No.' Also Will Be A Whatsapp Number) Row Without Any Type Of Spelling Mistake.
    """
    df = pd.read_excel(xlsx_file)    
    hour = int(datetime.datetime.now().strftime('%H'))
    minute = int(datetime.datetime.now().strftime('%M'))
    today = datetime.datetime.now().strftime('%d-%m')   
    yearNow = datetime.datetime.now().strftime('%Y') 
    writeInd = []  
    for index,item in df.iterrows():
        bday = item['Birthday'].strftime('%d-%m')
        if bday==today and yearNow not in str(item['Year']):
            writeInd.append(index)
            pywhatkit.sendwhatmsg(f'+{item["Mobile No."]}',f'🎂🎂Happy Birthday {item["Name"]}🎂🎂',hour,minute+1,wait_time=30)
    for i in writeInd:
        yr = df.loc[i,'Year']
        df.loc[i,'Year'] = str(yr)+','+str(yearNow)
    df.to_excel(xlsx_file,index=False)
def create_xlsx(birthday_counts,filename='data'):
    """
    Create '*.xlsx' File For 'birthday_wisher' Function And Reduces Work Of Users.This Function Take 2 Arguements As birthday_counts As Integer And filename As String Default filename Is data.
    """
    with open(f'{filename}.csv',mode='w') as f:
        f.write('Name,Birthday,Year,Mobile No.')
    df = pd.read_csv(f'{filename}.csv')
    for row in range(0,birthday_counts):
        print('Enter Data To Create ".xlsx" File')
        df.loc[row,'Name'] = input(f'Enter Name Of {row+1} Column: \n')
        df.loc[row,'Birthday'] = input(f'Enter Birthday Of {row+1} Column In DD/MM Formant : \n')
        df.loc[row,'Year'] = int(input(f'Enter Last Time Wished Year Of {row+1} Column In YYYY Format: \n'))
        df.loc[row,'Mobile No.'] = int(input(f'Enter Whtasapp Mobile No. Of {row+1} Column With Country Code Without "+" : \n'))
    df.to_excel(f'{filename}.xlsx',index=False)
    os.remove(f'{filename}.csv')