# droperbox
Dropbox api の Upload,Downloadを楽にしたい自作ライブラリ

# Version
2.0.1

# Install
```pip install git+https://github.com/8ka1alu/droperbox.git```

# 初めに
Dropboxのapiトークンを取得

# 使い方
```python
from droperbox import Droperbox

file_name = 'hoge.txt' #扱いたい任意のファイル名
dpb = Droperbox(os.environ['DROPBOX_BOT_TOKEN'])

#ダウンロード
status, message = dpb.download(file_name=file_name)
print(status, message)

#アップロード
status, message = dpb.upload(file_name=file_name)
print(status, message)
```
