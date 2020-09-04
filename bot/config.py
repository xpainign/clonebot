import os
from distutils.util import strtobool as stb

# --------------------------------------
BOT_TOKEN = "1386889761:AAHkaIYloSQx7fLYlX459VvcCGQLRGVal0E"
GDRIVE_FOLDER_ID = "0AGkpbJZyyYMZUk9PVA"
OWNER_ID = 310260910
# Example: OWNER_ID = 619418070
INDEX_URL = "https://xpainteamdrive.albinmaniparambil.workers.dev"
IS_TEAM_DRIVE = True
USE_SERVICE_ACCOUNTS = True
# --------------------------------------

# dont edit below this >



BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', GDRIVE_FOLDER_ID)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
INDEX_URL = os.environ.get('INDEX_URL', INDEX_URL)
IS_TEAM_DRIVE = stb(os.environ.get('IS_TEAM_DRIVE', str(IS_TEAM_DRIVE)))
USE_SERVICE_ACCOUNTS = stb(os.environ.get('USE_SERVICE_ACCOUNTS', str(USE_SERVICE_ACCOUNTS)))
