from agenceGaber.main import MAINMENU
from agenceGaber.classDB.database import DATABASE

DB = DATABASE('localhost', '3308', 'agencegaber', 'root', '')
MAINMENU(DB)
