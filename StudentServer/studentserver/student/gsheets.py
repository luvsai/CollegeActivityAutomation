from __future__ import print_function
import pandas as pd
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

gsheets = ['S1: Student Journal Pub',
 'S2: Student Conference Publication', 
 'S3: Student Internships',
  'S4: Student Certifications',
   'S5: Student Workshops/Conf attended', 'S6: Student NPTEL', 
#    'S7: Student Workshops Organized',
    'S8: Student Events Organized',
     'S9: Student Guest Lectures Organized',
      'S10: Student Prof. Body', 
      'S11: Student Awards',
       'S12: Student capabilities enhancement', 
       'S13: Students Higher Edu.', 
       'S14: Students Competitive Exams',
 'S15: Students Industry Visit',
  'S16: Students Social Service Programs',
   'S17: Students Leadership & Volunteering Activities', 
   'S18: Students Placements']



# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1EYRfu4z0mw_j6wW3Y1eoq2K0G99pvaX0P6axRAu2wlI'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E' 

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

datasheets = {}

# SAMPLE_RANGE_NAME =   SAMPLE_RANGE_NAME + '!A:Z'
# gsheet_name = 'S1 Studen Journal Pub'

# If there are no (valid) credentials available, let the user log in.
def getSheetdf(sheetname):
    global datasheets
    # print("Getting sheet data : ", sheetname,"------------------")
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()

        rows = sheet.values().get(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=sheetname ,
            ).execute().get('values')
        no_of_cols = len(rows[0])
        for row in rows:
            if len(row) < no_of_cols:
                row 
        drows = rows[1:]
        if len(rows ) == 2 and len(rows[1]) == 1:
            drows = [[None for i in range(no_of_cols)]]
        #     print(row)
        new_df = pd.DataFrame(columns=rows[0], data=drows)
        #print(new_df)
        datasheets[sheetname] = new_df
        print("--------------------- > Completed data parsed  : ",sheetname)
        return new_df
    except Exception as e:
        print("xxxxxxxxxxxxxxxxxxxxxx > Failed  data parsed : ",sheetname)
        print(e)
        pass
    #new_df = pd.DataFrame(columns=['nodata'], data=["0"])
    #datasheets[sheetname] = None
    return None