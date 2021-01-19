from dotenv import load_dotenv, find_dotenv
from libs.google_auth_utils import get_credentials

load_dotenv(find_dotenv())

def main():

    # Set the access scopes (Docs: https://developers.google.com/identity/protocols/oauth2/scopes)
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # Call anytime a function needs to access a user's Google resource
    creds = get_credentials(SCOPES)

    #print(vars(creds))
    print(f'Scopes:\n{creds.scopes}\n')
    print(f'Token expiration:\n{creds.expiry}')

    return

if __name__ == '__main__':
    main()