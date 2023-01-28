from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']




# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '161L8s6c5VLhIiXPMdZ5JfN_AvFD69BEDaP7mRBhutt8'
SAMPLE_RANGE_NAME = 'Sheet1!A1:C12'
client_secret = 'E:\Daniel\Programacao\Projetos Completos\PaymentReceiptOrganizationAutomation.git\PaymentReceiptOrganizationAutomation\client_secret.json'
GOOGLE_APPLICATION_CREDENTIALS = 'E:\Daniel\Programacao\Projetos Completos\PaymentReceiptOrganizationAutomation.git\token.json'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None


    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secret, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    
def ler_valores():
    credenciais, _ = google.auth.default()
    planilha_id = '161L8s6c5VLhIiXPMdZ5JfN_AvFD69BEDaP7mRBhutt8'
    nome_range = "Sheet1!A:B"

    try:
        service = build('sheets', 'v4', credentials=GOOGLE_APPLICATION_CREDENTIALS)

        result = service.spreadsheets().values().get(
            spreadsheetId = planilha_id, range = nome_range).execute()
        linhas = result.get('values', [])
        print(f"{len(linhas)} rows retrieved")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


# main()
valores_planilha = ler_valores()

print(valores_planilha)


#     try:
#         service = build('sheets', 'v4', credentials=creds)
#         # Call the Sheets API
#         sheet = service.spreadsheets()
#         result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                     range=SAMPLE_RANGE_NAME).execute()
#         values = result.get('values', [])

#         if not values:
#             print('No data found.')
#             return

#         print('Name, Major:')
#         for row in values:
#             # Print columns A and E, which correspond to indices 0 and 4.
#             print('%s, %s' % (row[0], row[2]))
#     except HttpError as err:
#         print(err)

#     valores_adicionar = [ ['A', 'B'], ['C', 'D'], ]
#     body = {
#         'values': valores_adicionar
#     }
#     sheet = service.spreadsheets()
#     result = service.spreadsheets().values().update(
#             spreadsheetId='161L8s6c5VLhIiXPMdZ5JfN_AvFD69BEDaP7mRBhutt8', range='Sheet1!A1:c2',valueInputOption= "USER_ENTERED",body=body).execute()

#     values = result.get('values', [])
#     print(values)

    


#     # result = service.spreadsheets().values().update(
#     #         spreadsheetId='161L8s6c5VLhIiXPMdZ5JfN_AvFD69BEDaP7mRBhutt8', range='Sheet1!A1:C12').execute()

# if __name__ == '__main__':
#     main()