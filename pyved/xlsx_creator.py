import pandas
import os
def create_xlsx(birthday_counts,filename='data'):
    """
    Create '*.xlsx' File For 'birthday_wisher' Function And Reduces Work Of Users.This Function Take 2 Arguements As birthday_counts As Integer And filename As String Default filename Is data.
    """
    try:
        with open(f'{filename}.csv',mode='w') as f:
            f.write('Name,Birthday,Year,Mobile No.')
        df = pandas.read_csv(f'{filename}.csv')
        for row in range(0,birthday_counts):
            print('Enter Data To Create ".xlsx" File')
            df.loc[row,'Name'] = input(f'Enter Name Of {row+1} Column: \n')
            df.loc[row,'Birthday'] = input(f'Enter Birthday Of {row+1} Column In DD/MM Formant : \n')
            df.loc[row,'Year'] = int(input(f'Enter Last Time Wished Year Of {row+1} Column In YYYY Format: \n'))
            df.loc[row,'Mobile No.'] = int(input(f'Enter Whtasapp Mobile No. Of {row+1} Column With Country Code Without "+" : \n'))
            os.system('cls')
        df.to_excel(f'{filename}.xlsx',index=False)
        os.remove(f'{filename}.csv')
    except Exception as e:
        print(e)