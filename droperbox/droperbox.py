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
        dbx = dropbox.Dropbox(token)
        return True, dbx
    else:
        return False, 'Not Token'

    
def download(dropbox,file_name:int):
    try:
        check, dbx = create_dbx(dropbox)
        if check == False:
            return False, dbx
        elif check == True:
            with open(file_name, "wb") as f:
                metadata, res = dbx.files_download(path=f"/{file_name}")
                f.write(res.content)
            return True, 'Success'
        else:
            return False, 'Error'
    except Exception as e:
        return False, e
    
    
def upload(dropbox,file_name:int):
    try:
        check, dbx = create_dbx(dropbox)
        if check == False:
            return False, dbx
        elif check == True:
            with open(file_name, 'rb') as f:
                data = f.read()
                res = dbx.files_upload(data=data, path=f'/{file_name}', mode=dropbox.files.WriteMode.overwrite)
            return True, 'Success'
        else:
            return False, 'Error'
    except Exception as e:
        return False, e
