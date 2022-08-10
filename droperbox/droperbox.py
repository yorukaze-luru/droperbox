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
        dbx.users_get_current_account()
        return True, dbx
    else:
        return False, print('Not Token')

    
def download(dropbox,file_name:int):
    try:
        dbx = create_dbx(dropbox)
        with open(file_name, "wb") as f:
            metadata, res = dbx.files_download(path=f"/{file_name}")
            f.write(res.content)
            return True, 'Success'
    except Exception as e:
        return False, e
    
    
def upload(dropbox,file_name:int):
    try:
        dbx = create_dbx(dropbox)
        with open(file_name, "rb") as fc:
            dbx.files_upload(fc.read(), f"/{file_name}", mode=dropbox.files.WriteMode("overwrite"))
        return True, 'Success'
    except Exception as e:
        return False, e
