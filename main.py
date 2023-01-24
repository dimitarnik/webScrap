import gspread

gc = gspread.service_account(filename='creds.json')
sh = gc.open('ScrapWebProject').sheet1

sh.update('A1', 'Test update')
