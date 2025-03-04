import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up Google Docs API credentials
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('docs', 'v1', credentials=credentials)

def extract_document_id(url):
    # Extract the document ID from the URL
    start = url.find('/d/') + 3
    end = url.find('/', start)
    return url[start:end]

def get_document_content(document_id):
    doc = service.documents().get(documentId=document_id).execute()
    return doc.get('body').get('content')

def parse_document_content(content):
    data = []
    for element in content:
        if 'table' in element:
            for row in element['table']['tableRows']:
                cells = row['tableCells']
                x = int(cells[0]['content'][0]['paragraph']['elements'][0]['textRun']['content'].strip())
                char = cells[1]['content'][0]['paragraph']['elements'][0]['textRun']['content'].strip()
                y = int(cells[2]['content'][0]['paragraph']['elements'][0]['textRun']['content'].strip())
                data.append((x, y, char))
    return data

def construct_grid(data):
    max_x = max([x for x, y, char in data])
    max_y = max([y for x, y, char in data])
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, char in data:
        grid[y][x] = char
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def decode_secret_message(doc_url):
    document_id = extract_document_id(doc_url)
    content = get_document_content(document_id)
    data = parse_document_content(content)
    grid = construct_grid(data)
    print_grid(grid)


if __name__ == "__main__":
# Example usage
    doc_url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
    decode_secret_message(doc_url)

