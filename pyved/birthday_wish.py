def birthday_wisher(xlsx_file):
    """
    This Function Wish Your Friends,Family Members etc.Bitrhday On Behalf Of You.
    This Function Take One Argument As '*.xlsx' File
    In Your xlsx File There Will Be 'Name' Row,A 'Birthday'(DD/MM) Row ,A 'Year'(YYYY) Row And 'Mobile No.'(with Country Code without '+' And 'Mobile No.' Also Will Be A Whatsapp Number) Row Without Any Type Of Spelling Mistake.
    """
    import pandas as pd
    import pywhatkit
    import datetime
    df = pd.read_excel('data.xlsx')
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
    df.to_excel('data.xlsx',index=False)