import dropbox
from dropbox.exceptions import AuthError

# Dropbox API credentials
APP_KEY = 'insert app key here'
APP_SECRET = 'insert app secret here'
ACCESS_TOKEN = 'insert access token here'

def authenticate_dropbox():
    try:
        flow = dropbox.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
        authorize_url = flow.start()
        print(f"1. Go to: {authorize_url}")
        print("2. Click 'Allow' (you might have to log in first)")
        print("3. Copy the authorization code.")
        auth_code = input("Enter the authorization code here: ")

        # Finish the authorization process
        result = flow.finish(auth_code)
        access_token = result.access_token
        return access_token
    except AuthError as e:
        print(f"Error authenticating with Dropbox: {e}")
        return None


def upload_file(file_path, dropbox_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    print("Transferring translate.py to dropbox")

    try:
        with open(file_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path)
        print(f"File uploaded successfully to {dropbox_path}")
    except dropbox.exceptions.ApiError as e:
        print(f"Error uploading file to Dropbox: {e}")

if __name__ == "__main__":
    # Authenticate and obtain access token
    access_token = authenticate_dropbox()

    if access_token:
        # Set the access token for future requests
        ACCESS_TOKEN = access_token

        # Example: Upload a file to Dropbox
        file_to_upload = 'translate.py'
        dropbox_destination = '/translate.py'
        upload_file(file_to_upload, dropbox_destination)
