import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/documents']

def upload_markdown(markdown_file, title=None):
    # Read the markdown content
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('docs', 'v1', credentials=creds)
    if not title:
        title = os.path.splitext(os.path.basename(markdown_file))[0]
    doc = service.documents().create(body={'title': title}).execute()
    doc_id = doc.get('documentId')

    # Insert content as plain text
    requests = [
        {
            'insertText': {
                'location': {'index': 1},
                'text': content
            }
        }
    ]
    service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
    doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
    print(f"Created Google Doc: {doc_url}")
    return doc_id 