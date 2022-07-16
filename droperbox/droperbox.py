from dropbox import Dropbox

_token = {
    "token": None
}

def token(token):
    _token["token"] = token

def get_token():
    return _token["token"]

def create_dbx():
    token = get_token()
    if token != None:
        dbx = dropbox.Dropbox()
        dbx.users_get_current_account()
        return dbx

def download(token,file_name):
    try:
        dbx = create_dbx()
        with open(file_name, "wb") as f:
            metadata, res = dbx.files_download(path=f"/{file_name}")
            f.write(res.content)
            return True
    except Exception as e:
        print(e)
        return False
    
    
def upload(file_name):
    try:
        dbx = create_dbx()
        with open(file_name, "rb") as fc:
            dbx.files_upload(fc.read(), f"/{file_name}", mode=dropbox.files.WriteMode.overwrite)
        return True
    except Exception as e:
        print(e)
        return False
