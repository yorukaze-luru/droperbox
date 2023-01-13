

class Droperbox:
    def __init__(self, token):
        self.token = token

    def _create_dbx(self):
        token = self.token
        if token != None:
            dbx = Dropbox(token)
            return True, dbx
        else:
            return False, 'Not Token'

    def download(self,file_name:int):
        try:
            check, dbx = Droperbox._create_dbx(self)
            if check == False:
                return False, dbx
            elif check == True:
                with open(file_path, "wb") as f:
                    metadata, res = dbx.files_download(path=f"/{file_name}")
                    f.write(res.content)
                return True, 'Success'
            else:
                return False, 'Error'
        except Exception as e:
            return False, e   
    
    def upload(dropbox,file_name:int):
        try:
            check, dbx = Droperbox._create_dbx(self)
            if check == False:
                return False, dbx
            elif check == True:
                with open(file_name, 'rb') as f:
                    data = f.read()
                    res = dbx.files_upload(f=data, path=f'/{file_name}', mode=dropbox.files.WriteMode.overwrite)
                return True, 'Success'
            else:
                return False, 'Error'
        except Exception as e:
            return False, e
