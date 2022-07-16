from dropbox import Dropbox

def download(token,file_name):
    dbx = dropbox.Dropbox(token)
    dbx.users_get_current_account()
    with open(file_name, "wb") as f:
        metadata, res = dbx.files_download(path=f"/{file_name}")
        f.write(res.content)
    
def upload()

