from droperbox.droperbox import Droperbox

__version__ = '2.0.1'

from os.path import dirname, abspath
import sys

parent_dir = dirname(abspath(__file__)) # 追加
if parent_dir not in sys.path: # 追加
    sys.path.append(parent_dir) # 追加

from dropbox import Dropbox
