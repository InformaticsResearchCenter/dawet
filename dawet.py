import config
import gspread
from oauth2client.service_account import  ServiceAccountCredentials

class Dawet(object, filename):
    def __init__(self, filename):
	self.filename = filename
        self.opendb()

    def opendb(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open(self.filename)

    def getData(self, rowname, colname, sheetnum):
        # try:
        ambil = self.sheet.get_worksheet(sheetnum).cell(self.sheet.get_worksheet(sheetnum).find(rowname).row, self.sheet.get_worksheet(sheetnum).find(colname).col).value
        # except Exception as e:
        # ambil = e
        return ambil

    def setData(self, rowname, colname, sheetnum, content):
        setv = self.sheet.get_worksheet(sheetnum).update_cell(self.sheet.get_worksheet(sheetnum).find(rowname).row, self.sheet.get_worksheet(sheetnum).find(colname).col, content)
        return setv
