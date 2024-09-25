import io
import os.path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

CLIENT_SECRET_FILE = r"C:\\Users\\calliel.clerice\\Documents\\TesteAPI\\starlit-granite-436116-f9-d1a169e217dc.json"
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

def create_service():
    creds = None
    if os.path.exists(CLIENT_SECRET_FILE):
        creds = service_account.Credentials.from_service_account_file(CLIENT_SECRET_FILE, scopes=SCOPES)
    service = build(API_NAME, API_VERSION, credentials=creds)
    return service


def downloadFile(service, fileID, file_name):
    try:
        request = service.files().get_media(fileId=fileID)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        done = False

        while not done:
            status, done = downloader.next_chunk()
            print("Download Progress: {0}".format(int(status.progress() * 100)))

        fh.seek(0)

        with open(file_name, 'wb') as f:
            f.write(fh.read())

    except FileNotFoundError:
        return ""

if __name__ == '__main__':
    service = create_service()
    fileID = '1sWObN9tudOhvl2HgeEDtVHzSgVXnUtBRtR_uKphGHgU'  
    file_name = 'teste.docx'  
    downloadFile(service, fileID, file_name)
