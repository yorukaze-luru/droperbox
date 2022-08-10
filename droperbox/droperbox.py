_token = {
    "token": None
}

def token(token):
    _token["token"] = token

def get_token():
    return _token["token"]

def create_dbx(dropbox):
    token = get_token()
    if token != None:
        dbx = dropbox.Dropbox()
        return True, dbx
    else:
        return False, 'Not Token'

    
def download(dropbox,file_name:int):
    try:
        dbx = create_dbx(dropbox)
        dbx.files_download_to_file(f'{file_name}', f'/{file_name}')
        return True, 'Success'
    except Exception as e:
        return False, e
    
    
def upload(dropbox,file_name:int):
    try:
        dbx = create_dbx(dropbox)
        dbx.files_upload(open(f'{file_name}', 'rb').read(), f'/{file_name}')
        return True, 'Success'
    except Exception as e:
        return False, e
