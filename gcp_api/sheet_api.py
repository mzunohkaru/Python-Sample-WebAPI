from dotenv import load_dotenv
import os
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'secret.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
print(gc)

load_dotenv()

SP_SHEET_KEY = os.getenv("SP_SHEET_KEY")
SP_SHEET = 'demo'

sh = gc.open_by_key(SP_SHEET_KEY)
print(sh)

worksheet = sh.worksheet(SP_SHEET)
print(worksheet)

data = worksheet.get_all_values()
print(data)

new_worksheet = sh.add_worksheet(title='new sheet', rows=100, cols=100)
print(new_worksheet)