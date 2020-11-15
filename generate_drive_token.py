import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

credentials = None
__G_DRIVE_TOKEN_FILE = "ya29.A0AfH6SMCzFm3emks1TKDz5DwBFSmsTHe9PMU232ncRIKb4x2gd1lDy3qnb9C5toN8lLUKnpcLFwwSLaUUDw4l7Y-Rce2zioLDpEwt7LpxUE3wigVRWHpdMM7DoMvX6oTKVQpGYiTwvMmgmuY0cv4fA8qrPIVLfueh5rlgclkBlY0"
__OAUTH_SCOPE = ["https://www.googleapis.com/auth/drive"]
if os.path.exists(__G_DRIVE_TOKEN_FILE):
    with open(__G_DRIVE_TOKEN_FILE, 'rb') as f:
        credentials = pickle.load(f)
        if credentials is None or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', __OAUTH_SCOPE)
    credentials = flow.run_console(port=0)

# Save the credentials for the next run
with open(__G_DRIVE_TOKEN_FILE, 'wb') as token:
    pickle.dump(credentials, token)
